from machine import Pin, PWM
from random import randint
from time import sleep_ms


def w(p, u):
    p.duty(max(0, min(1023, u * 1023 // 20000)))


def servo(n):
    x = [PWM(Pin(n), freq=50), 1500]
    w(x[0], 1500)
    return x


def put(a, x):
    a[1] = max(500, min(2500, x))
    w(a[0], a[1])


def step(a, x):
    d = x - a[1]
    put(a, a[1] + max(-20, min(20, d)))


def move(a, x):
    while a[1] != x:
        step(a, x)
        sleep_ms(12)
    sleep_ms(200)


def move2(a, x, b, y):
    while a[1] != x or b[1] != y:
        if a[1] != x:
            step(a, x)
        if b[1] != y:
            step(b, y)
        sleep_ms(12)
    sleep_ms(250)


def jitter(a, x, y):
    for i in range(12):
        move(a, y if i & 1 else x)


def drive(l, r):
    w(left, 1500 + l * 5)
    w(right, 1500 - r * 5)


def mv(l, r, t):
    return l, r, t


def make_random_drive_actions():
    a = []
    lo = max(10, min(60, 10 + auton_speed_level * 3))
    hi = max(lo + 5, min(80, 18 + auton_speed_level * 5))
    for _ in range(RANDOM_MOVE_SEGMENTS):
        s, t, c = randint(lo, hi), randint(550, 1150), randint(0, 3)
        if c == 0:
            a.append(mv(s, s, t))
        elif c == 1:
            a.append(mv(-s, s, t))
        elif c == 2:
            a.append(mv(s, -s, t))
        else:
            a.append(mv(s, int(s * .45), t))
    a.append(mv(0, 0, 300))
    return a


left, right = PWM(Pin(14), freq=50), PWM(Pin(12), freq=50)
base_yaw = servo(13)
base_pitch = servo(15)
chamber_seal = servo(25)
second_pitch = servo(26)
shovel_rotation = servo(4)
auton_speed_level = 5
RANDOM_MOVE_SEGMENTS = 5

pickup_actions = [
    (move, base_yaw, 500),
    (move, second_pitch, 1050),
    (move, base_pitch, 520),
    (move, shovel_rotation, 500),
    (move, second_pitch, 2330),
    (move, shovel_rotation, 2500),
    (move, second_pitch, 1080),
    (move, chamber_seal, 1000),
    (move2, base_pitch, 1600, second_pitch, 2000),
    (move, base_yaw, 2500),
    (move, base_pitch, 1000),
    (move, shovel_rotation, 550),
    (jitter, shovel_rotation, 500, 750),
    (move2, base_pitch, 1600, chamber_seal, 2180),
]

drive(0, 0)
for a in pickup_actions:
    a[0](*a[1:])
for l, r, t in make_random_drive_actions():
    drive(l, r)
    sleep_ms(t)
drive(0, 0)
while 1:
    sleep_ms(1000)
