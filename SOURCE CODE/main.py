from machine import ADC, I2C, Pin, time_pulse_us
from time import sleep_ms, sleep_us, ticks_ms
import os


LOG_FILE = "sensor_log.csv"
LOG_INTERVAL_MS = 60000

i2c = I2C(0, sda=Pin(21), scl=Pin(22), freq=100_000)
trigger = Pin(16, Pin.OUT, value=0)
echo = Pin(17, Pin.IN)
soil = ADC(Pin(39))
soil.atten(ADC.ATTN_11DB)


def u16(data, offset):
    return data[offset] | data[offset + 1] << 8


def s16(data, offset):
    value = u16(data, offset)
    return value - 65536 if value & 0x8000 else value


class BME280:
    def __init__(self, address):
        self.address = address
        c1 = i2c.readfrom_mem(address, 0x88, 26)
        c2 = i2c.readfrom_mem(address, 0xE1, 7)
        self.t = (u16(c1, 0), s16(c1, 2), s16(c1, 4))
        self.p = (u16(c1, 6),) + tuple(s16(c1, i) for i in range(8, 24, 2))
        h4 = c2[3] << 4 | c2[4] & 15
        h5 = c2[5] << 4 | c2[4] >> 4
        if h4 & 0x800:
            h4 -= 4096
        if h5 & 0x800:
            h5 -= 4096
        h6 = c2[6] - 256 if c2[6] & 0x80 else c2[6]
        self.h = (c1[25], s16(c2, 0), c2[2], h4, h5, h6)
        i2c.writeto_mem(address, 0xF2, b"\x01")
        i2c.writeto_mem(address, 0xF4, b"\x27")

    def read(self):
        data = i2c.readfrom_mem(self.address, 0xF7, 8)
        raw_p = data[0] << 12 | data[1] << 4 | data[2] >> 4
        raw_t = data[3] << 12 | data[4] << 4 | data[5] >> 4
        raw_h = data[6] << 8 | data[7]

        t1, t2, t3 = self.t
        a = (raw_t / 16384 - t1 / 1024) * t2
        b = (raw_t / 131072 - t1 / 8192) ** 2 * t3
        fine = a + b
        temperature = fine / 5120

        p1, p2, p3, p4, p5, p6, p7, p8, p9 = self.p
        a = fine / 2 - 64000
        b = a * a * p6 / 32768 + a * p5 * 2
        b = b / 4 + p4 * 65536
        a = (p3 * a * a / 524288 + p2 * a) / 524288
        a = (1 + a / 32768) * p1
        pressure = 0
        if a:
            pressure = (1048576 - raw_p - b / 4096) * 6250 / a
            pressure += (p9 * pressure * pressure / 2147483648 + p8 * pressure / 32768 + p7) / 16

        h1, h2, h3, h4, h5, h6 = self.h
        humidity = fine - 76800
        humidity = (raw_h - (h4 * 64 + h5 / 16384 * humidity)) * (
            h2 / 65536 * (1 + h6 / 67108864 * humidity * (1 + h3 / 67108864 * humidity))
        )
        humidity *= 1 - h1 * humidity / 524288
        return temperature, max(0, min(100, humidity)), pressure / 100


devices = i2c.scan()
bh1750 = 0x23 if 0x23 in devices else 0x5C if 0x5C in devices else None
bme_address = 0x76 if 0x76 in devices else 0x77 if 0x77 in devices else None
bme = BME280(bme_address) if bme_address else None

if bh1750:
    i2c.writeto(bh1750, b"\x10")
    sleep_ms(180)


def read_light():
    data = i2c.readfrom(bh1750, 2)
    return (data[0] << 8 | data[1]) / 1.2


def read_distance():
    trigger.value(1)
    sleep_us(10)
    trigger.value(0)
    pulse = time_pulse_us(echo, 1, 30_000)
    return pulse / 58 if pulse > 0 else None


def value_or_blank(function):
    try:
        value = function()
        return "" if value is None else "{:.2f}".format(value)
    except Exception:
        return ""


try:
    os.stat(LOG_FILE)
except OSError:
    with open(LOG_FILE, "w") as file:
        file.write("uptime_ms,light_lux,temp_c,humidity_pct,pressure_hpa,distance_cm,soil_raw\n")


while True:
    if bme:
        try:
            temperature, humidity, pressure = bme.read()
            environment = tuple("{:.2f}".format(x) for x in (temperature, humidity, pressure))
        except Exception:
            environment = ("", "", "")
    else:
        environment = ("", "", "")

    soil_raw = soil.read_u16() if hasattr(soil, "read_u16") else soil.read()
    row = [
        str(ticks_ms()),
        value_or_blank(read_light) if bh1750 else "",
        environment[0],
        environment[1],
        environment[2],
        value_or_blank(read_distance),
        str(soil_raw),
    ]
    line = ",".join(row)
    with open(LOG_FILE, "a") as file:
        file.write(line + "\n")
    print(line)
    sleep_ms(LOG_INTERVAL_MS)
