# ESP32 Plant Health Monitor Rover


I built this to sample soil health from my garden and this is just a prototype, not the real version yet, I will build another iteration but this is what I have currently. It is a fun educational toy to play with though.

## Features

* Autonomous
* Two-servo tank drive
* Seven servos total
  * Two continuous-rotation drive servos
  * Four arm position servos
  * One sample chamber closing servo
* Soil electrical conductivity measurement
* Temperature, humidity, pressure, and light measurements
* Ultrasound distance measurement


## Proof Pictures

Here is the demo video I have on the robot:

https://www.youtube.com/shorts/W9_TdJyh92A

### CAD Prototype

![CAD Prototype](Pictures/CAD-prototype.png)


### Circuit Schematic

![Updated Circuit Schematic](Schematics/UpdatedCircuitSchematicV2.png)


### Real-Life Prototype

![Real-Life Prototype](Pictures/real-life-prototype.png)


## Hardware Description

The rover utilizes ESP32 microcontroller. Tank drive is controlled using two PWM outputs, acting as continuous-rotation servos. Soil collection uses five additional PWM outputs to actuate servos of the arm and close the sample chamber.

Sensors include a BH1750 light sensor, a BME280 environmental sensor, an HC-SR04 ultrasound distance sensor, and an analog soil electrical conductivity sensor. Both BH1750 and BME280 are on the same I2C bus.

## Bill of materials


| Category | Quantity | Part | Link | Price |
|---|---:|---|---|---:|
| Electronics | 1 | ESP32 development board | [AliExpress](https://www.aliexpress.us/item/3256812360578716.html) | $4.67 |
| Actuator | 2 | Continuous-rotation drivetrain servo | [AliExpress](https://www.aliexpress.us/item/3256804365417662.html) | $9.28 (2-pack) |
| Actuator | 1 | Main arm pitch servo | [AliExpress](https://www.aliexpress.us/item/3256804365417662.html) | $4.64 used (1 of 2-pack at $9.28) |
| Actuator | 5 | Micro servo | [AliExpress](https://www.aliexpress.us/item/3256806107378152.html) | $4.95 used (5 at $0.99 each) |
| Sensor | 1 | Ambient light sensor | [AliExpress](https://www.aliexpress.us/item/3256809513329235.html) | $3.00 |
| Sensor | 1 | Environmental sensor | [AliExpress](https://www.aliexpress.us/item/3256812547404758.html) | $5.85 |
| Sensor | 1 | Ultrasonic distance sensor | [AliExpress](https://www.aliexpress.us/item/3256810017345486.html) | $1.25 |
| Sensor | 1 | Soil electrical conductivity sensor | [AliExpress](https://www.aliexpress.us/item/3256811685769454.html) | $13.29 |
| Power | 1 | Buck converter | [AliExpress](https://www.aliexpress.us/item/3256806558389509.html) | $1.46 |
| Power | 2 | Lithium-ion cell | [AliExpress](https://www.aliexpress.us/item/3256811867524654.html) | $3.35 used (2 of 16-pack at $26.77) |
| Power | 1 | 2S battery holder | [AliExpress](https://www.aliexpress.us/item/3256809135366720.html) | $0.99 |
| Power | 1 | Power switch | [AliExpress](https://www.aliexpress.us/item/3256807619399290.html) | $0.16 used (1 of 10-pack at $1.64) |
| Power | 1 | 2S battery charger | [AliExpress](https://www.aliexpress.us/item/3256805668198456.html) | $0.99 |
| Protection | 1 | Ultrasonic echo level shifter | [AliExpress](https://www.aliexpress.us/item/3256810490396292.html) | $0.24 used (1 of 5-pack at $1.19) |
| Mechanical | 5 | Ball bearing | [AliExpress](https://www.aliexpress.us/item/3256805609422387.html) | $8.06 (5-pack) |
| Mechanical | As needed | M3 fasteners | [AliExpress](https://www.aliexpress.us/item/3256809672273859.html) | $14.88 assortment kit |
| Mechanical | Included with servos | Servo horns and screws | [AliExpress](https://www.aliexpress.us/item/3256804365417662.html) | $0.00 (included with servos) |
| Fabricated | 1 | Base structure | [PLA filament](https://www.aliexpress.us/item/3256806989098121.html) | $1.75 estimated (173 g solid PLA) |
| Fabricated | 2 | Drivetrain wheel | [PLA filament](https://www.aliexpress.us/item/3256806989098121.html) | $2.12 estimated (209 g solid PLA) |
| Fabricated | 1 | Front caster wheel | [PLA filament](https://www.aliexpress.us/item/3256806989098121.html) | $0.02 estimated (2.4 g solid PLA) |
| Fabricated | 1 | Front wheel hinge | [PLA filament](https://www.aliexpress.us/item/3256806989098121.html) | $0.06 estimated (5.8 g solid PLA) |
| Fabricated | 1 | Arm yaw servo holder | [PLA filament](https://www.aliexpress.us/item/3256806989098121.html) | $0.27 estimated (26.2 g solid PLA) |
| Fabricated | 1 | Arm yaw horn attachment | [PLA filament](https://www.aliexpress.us/item/3256806989098121.html) | $0.03 estimated (2.5 g solid PLA) |
| Fabricated | 1 | Arm pitch servo holder | [PLA filament](https://www.aliexpress.us/item/3256806989098121.html) | $0.18 estimated (17.8 g solid PLA) |
| Fabricated | 1 | Arm pitch horn attachment | [PLA filament](https://www.aliexpress.us/item/3256806989098121.html) | $0.17 estimated (16.8 g solid PLA) |
| Fabricated | 1 | Arm pitch adapter | [PLA filament](https://www.aliexpress.us/item/3256806989098121.html) | $0.03 estimated (2.9 g solid PLA) |
| Fabricated | 1 | Main arm | [PLA filament](https://www.aliexpress.us/item/3256806989098121.html) | $0.01 estimated (1.3 g solid PLA) |
| Fabricated | 1 | Second-pitch horn attachment | [PLA filament](https://www.aliexpress.us/item/3256806989098121.html) | $0.07 estimated (6.9 g solid PLA) |
| Fabricated | 1 set | General output attachment | [PLA filament](https://www.aliexpress.us/item/3256806989098121.html) | $0.05 estimated (5.0 g solid PLA) |
| Fabricated | 1 | Shovel output attachment | [PLA filament](https://www.aliexpress.us/item/3256806989098121.html) | $0.02 estimated (2.2 g solid PLA) |
| Fabricated | 1 | Soil container | [PLA filament](https://www.aliexpress.us/item/3256806989098121.html) | $0.20 estimated (19.5 g solid PLA) |
| Fabricated | 1 | Soil container lid | [PLA filament](https://www.aliexpress.us/item/3256806989098121.html) | $0.05 estimated (5.3 g solid PLA) |
| Consumable | As needed | Hookup wire | [AliExpress](https://www.aliexpress.us/item/3256808061834409.html) | $4.69 allowance |
| Consumable | As needed | Assembly consumables | [AliExpress](https://www.aliexpress.us/item/3256805494059216.html) | $3.30 allowance |

## GPIO Mapping

| Component             | Purpose                                    | ESP32 GPIO |
| --------------------- | ------------------------------------------ | ---------: |
| Left drive motor      | Drivetrain                                 |         14 |
| Right drive motor     | Drivetrain                                 |         12 |
| Base yaw motor        | Collection arm rotation                    |         13 |
| Base pitch motor      | Main collection arm lift                   |         15 |
| Second pitch motor    | Secondary collection arm                   |         26 |
| Shovel rotation motor | Soil collector/collector                   |          4 |
| Sample chamber motor  | Opens/closes sample chamber                |         25 |
| Soil EC sensor        | Analog soil electrical conductivity sensor |         39 |
| BH1750                | I2C SDA                                    |         21 |
| BH1750                | I2C SCL                                    |         22 |
| BME280                | I2C SDA                                    |         21 |
| BME280                | I2C SCL                                    |         22 |
| HC-SR04 ultrasonic    | Trigger                                    |         16 |
| HC-SR04 ultrasonic    | Echo                                       |         17 |

### BH1750 Light Sensor

Wired through I2C

| Pin | Connection |
| --- | ---------- |
| VCC | 3.3 V      |
| GND | GND        |
| SDA | GPIO21     |
| SCL | GPIO22     |

### BME280 Temp/Humidity/Air Pressure Sensor

Wired through I2C

| Pin | Connection |
| --- | ---------- |
| VCC | 3.3 V      |
| GND | GND        |
| SDA | GPIO21     |
| SCL | GPIO22     |

### HC-SR04 Ultrasonic Sensor

Distance sensor for navigation

| Pin     | Connection   |
| ------- | ------------ |
| VCC     | 3.3 V        |
| GND     | GND          |
| Trigger | GPIO16 / RX2 |
| Echo    | GPIO17 / TX2 |

### Analog Soil EC Sensor

Analog 

| Pin        | Connection  |
| ---------- | ----------- |
| VCC        | 3.3 V       |
| GND        | GND         |
| Analog out | GPIO39 / VN |

## Servos

Seven servos in rover.

| Servo            | Function                               | ESP32 GPIO |
| ---------------- | -------------------------------------- | ---------: |
| Left drivetrain  | Left drive motor for tank driving      |         14 |
| Right drivetrain | Right drive motor for tank driving     |         12 |
| Yaw              | Collection arm rotation                |         13 |
| Pitch base       | Collection arm lifting                 |         15 |
| Pitch secondary  | Collection arm second joint            |         26 |
| Shovel rotation  | Soil collector arm rotation            |          4 |
| Chamber          | Open/closes the soil collector chamber |         25 |

## Power System

2S battery pack charged using 2S charger, with XL4005 for buck conversion

```text
2S 18650 battery pack
        |
        |
      Switch
        |
        |
   XL4005 buck converter
        |
        |
   Regulated 5 V rail
        |
        |---- Servo power rail
        |---- ESP32 5 V/VIN input, if used regulated 5 V
        |---- Sensor power, if the sensor requires 5 V
```

## Soil Sampling Movement Sequence

| Step | Action                                            |
| ---: | ------------------------------------------------- |
|    1 | Base yaw to 500 µs                                |
|    2 | Second pitch to 1050 µs                           |
|    3 | Base pitch to 520 µs                              |
|    4 | Shovel rotation to 500 µs                         |
|    5 | Second pitch to 2330 µs                           |
|    6 | Shovel rotation to 2500 µs                        |
|    7 | Second pitch to 1080 µs                           |
|    8 | Chamber seal to 1000 µs                           |
|    9 | Base pitch to 1600 µs and second pitch to 2000 µs |
|   10 | Base yaw to 2500 µs                               |
|   11 | Base pitch to 1000 µs                             |
|   12 | Shovel rotation to 550 µs                         |
|   13 | Jittering shovel between 500 and 750 µs           |
|   14 | Base pitch to 1600 µs and chamber seal to 2180 µs |

## Assembly Instructions

Note that these are approximate instructions for replicating the rover. Tolerances across printers vary and reprinting may be required with custom slicer settings.

### Parts and Tools

Print all of the parts in [`SOURCE CAD/Individual Parts`](SOURCE%20CAD/Individual%20Parts) before beginning assembly. The editable Fusion archive and STEP assembly are available in [`SOURCE CAD/Source CAD`](SOURCE%20CAD/Source%20CAD). You will also need:

* 3 MG996 or equivalent servos: two continuous-rotation units for the drivetrain and one positional unit for the main arm pitch axis
* 5 SG90 or equivalent micro servos (the current seven-servo layout uses four, so the fifth can be kept as a spare)
* ESP32 development board
* XL4005 buck converter
* Two 18650 lithium-ion cells in a protected 2S holder or a pre-tabbed protected 2S pack
* Toggle power switch
* BH1750 light sensor
* BME280 temperature, humidity, and pressure sensor
* HC-SR04 ultrasonic distance sensor
* Analog soil EC sensor, such as the Soil EC Sensor V1.2 used in the prototype
* 608 bearings for supporting the arm joints and caster assembly
* M3 screws and nuts, including 20 mm M3 screws for retaining the drivetrain wheels
* Servo horns and the M2 self-tapping screws supplied with the servos
* Soldering iron, solder, heat-shrink tubing or electrical tape, zip ties, and thin 26 AWG or similar hookup wire
* Multimeter, suitable 2S lithium-ion charger, and basic hand tools


### Individual Printable Parts

* [`base_structure.stl`](SOURCE%20CAD/Individual%20Parts/base_structure.stl) - main baseplate and chassis
* [`wheel.stl`](SOURCE%20CAD/Individual%20Parts/wheel.stl) - rear drivetrain wheel; print two
* [`front_caster_wheel.stl`](SOURCE%20CAD/Individual%20Parts/front_caster_wheel.stl) - front caster wheel
* [`front_wheel_hinge.stl`](SOURCE%20CAD/Individual%20Parts/front_wheel_hinge.stl) - caster holder/hinge
* [`arm_yaw_servo_holder.stl`](SOURCE%20CAD/Individual%20Parts/arm_yaw_servo_holder.stl) - yaw-axis servo holder
* [`arm_yaw_servo_horn_attachment.stl`](SOURCE%20CAD/Individual%20Parts/arm_yaw_servo_horn_attachment.stl) - yaw horn adapter
* [`arm_pitch_servo_holder.stl`](SOURCE%20CAD/Individual%20Parts/arm_pitch_servo_holder.stl) - MG996 main-pitch holder
* [`arm_pitch_servo_horn_attachment.stl`](SOURCE%20CAD/Individual%20Parts/arm_pitch_servo_horn_attachment.stl) - main-pitch horn adapter
* [`arm_pitch_adapter.stl`](SOURCE%20CAD/Individual%20Parts/arm_pitch_adapter.stl) - adapter between the yaw and pitch sections
* [`arm.stl`](SOURCE%20CAD/Individual%20Parts/arm.stl) - main printed arm section
* [`Arm_2nd_pitch_Horn_attachment.stl`](SOURCE%20CAD/Individual%20Parts/Arm_2nd_pitch_Horn_attachment.stl) - second-pitch horn adapter
* [`arm_output_attachment_part1.stl`](SOURCE%20CAD/Individual%20Parts/arm_output_attachment_part1.stl) and [`arm_output_attachment_part2.stl`](SOURCE%20CAD/Individual%20Parts/arm_output_attachment_part2.stl) - two-part general output attachment
* [`arm_output_shovel_attachment.stl`](SOURCE%20CAD/Individual%20Parts/arm_output_shovel_attachment.stl) - shovel output attachment
* [`Soil_container.stl`](SOURCE%20CAD/Individual%20Parts/Soil_container.stl) - soil sample container
* [`Soil_container_lid.stl`](SOURCE%20CAD/Individual%20Parts/Soil_container_lid.stl) - servo-operated container lid

The current folder does not include a separately named yaw-axis cover. Refer to the complete [Fusion archive](SOURCE%20CAD/Source%20CAD/autonomous-soil-sampler-prototype.f3z) or [STEP assembly](SOURCE%20CAD/Source%20CAD/autonomous-soil-sampler-prototype.step) for that feature and its placement.

### 1. Print and Prepare the Parts

1. Print every required STL with enough wall thickness and infill to support the servos and arm. The base, drivetrain wheels, arm joints, and horn adapters experience the most load.
2. Remove supports and clean the screw holes, servo pockets, bearing seats, and shaft openings.
3. Test-fit all servos, horns, bearings, screws, and adapters before final assembly. Lightly sand tight holes rather than forcing a servo or bearing into place.
4. Center each positional servo with a simple ESP32 or servo-tester program before attaching its horn. This prevents a joint from being assembled outside its usable range.

### 2. Assemble the Base and Drivetrain

1. Begin with [`base_structure.stl`](SOURCE%20CAD/Individual%20Parts/base_structure.stl), the large baseplate.
2. Mount one continuous-rotation MG996 servo on each side of the chassis using M3 screws and nuts. Keep both output shafts aligned and leave access to the servo cables.
3. Print two copies of [`wheel.stl`](SOURCE%20CAD/Individual%20Parts/wheel.stl). Fasten each drivetrain wheel to an MG996 horn with the self-tapping screws supplied with the servo. Attach the horn to the servo output, then use a 20 mm M3 screw as the center retainer. Do not overtighten the center screw or strip the output spline.
4. Check that both wheels rotate without rubbing the base. Use glue only after the alignment has been tested; screws should carry the drivetrain load wherever possible.
5. Press a 608 bearing into the front caster opening. If the fit is loose, use a small amount of suitable adhesive around the outside of the bearing without allowing glue to enter the bearing.
6. Install [`front_wheel_hinge.stl`](SOURCE%20CAD/Individual%20Parts/front_wheel_hinge.stl), then fit a 608 bearing and [`front_caster_wheel.stl`](SOURCE%20CAD/Individual%20Parts/front_caster_wheel.stl) into the caster assembly. Confirm that the caster can roll and swivel freely.

### 3. Build the Arm Yaw and Main Pitch Axes

1. Mount an SG90 in the base yaw position with the M2 self-tapping screws supplied with it.
2. Attach [`arm_yaw_servo_horn_attachment.stl`](SOURCE%20CAD/Individual%20Parts/arm_yaw_servo_horn_attachment.stl) to the centered SG90 horn. Fit the matching yaw cover/support shown in the complete CAD assembly, using a 608 bearing on the opposite side of the axis to reduce wobble.
3. Secure [`arm_yaw_servo_holder.stl`](SOURCE%20CAD/Individual%20Parts/arm_yaw_servo_holder.stl) above the yaw mechanism with M3 hardware. Rotate the joint by hand and confirm that the servo wire is not pinched; wire clearance was one of the issues corrected during prototyping.
4. Fit [`arm_pitch_adapter.stl`](SOURCE%20CAD/Individual%20Parts/arm_pitch_adapter.stl) to adapt the yaw output to the larger main-pitch shaft.
5. Install the positional MG996 in [`arm_pitch_servo_holder.stl`](SOURCE%20CAD/Individual%20Parts/arm_pitch_servo_holder.stl) and fasten the holder to the yaw assembly.
6. Attach [`arm_pitch_servo_horn_attachment.stl`](SOURCE%20CAD/Individual%20Parts/arm_pitch_servo_horn_attachment.stl) to the MG996 horn. Seat a 608 bearing in the support on the opposite side of the pitch axis, then install [`arm.stl`](SOURCE%20CAD/Individual%20Parts/arm.stl). Check that the joint moves smoothly before tightening everything fully.

### 4. Add the Second Pitch Joint and Tool Output

1. Mount an SG90 for the second pitch axis using its two self-tapping screws.
2. Place a 608 bearing on the opposite side of the joint for support. Fasten [`Arm_2nd_pitch_Horn_attachment.stl`](SOURCE%20CAD/Individual%20Parts/Arm_2nd_pitch_Horn_attachment.stl) to the servo horn, connect it to the printed arm, and verify the full motion range without binding.
3. Mount another SG90 at the end of the arm for output rotation. Route its wire along the arm with enough slack for both pitch joints, securing it with small zip ties.
4. Attach either the two-part output made from [`arm_output_attachment_part1.stl`](SOURCE%20CAD/Individual%20Parts/arm_output_attachment_part1.stl) and [`arm_output_attachment_part2.stl`](SOURCE%20CAD/Individual%20Parts/arm_output_attachment_part2.stl), or use [`arm_output_shovel_attachment.stl`](SOURCE%20CAD/Individual%20Parts/arm_output_shovel_attachment.stl) for the soil-shovel configuration.

### 5. Install the Soil Container and Lid

1. Position [`Soil_container.stl`](SOURCE%20CAD/Individual%20Parts/Soil_container.stl) behind the arm on the chassis. Confirm that the arm can deposit soil into it before gluing the container in place.
2. Mount an SG90 in the container's servo slot using the supplied self-tapping screws.
3. Attach an SG90 horn to [`Soil_container_lid.stl`](SOURCE%20CAD/Individual%20Parts/Soil_container_lid.stl), then attach the horn to the centered servo. Test the open and closed positions and make sure the lid seals without forcing the servo against its mechanical stop.

### 6. Install the Power System and Wiring

1. Mount the 2S battery pack low on the chassis and secure it so it cannot move into the wheels or arm.
2. Wire the battery positive lead through the toggle switch and then to the XL4005 input. Connect battery negative directly to the XL4005 input negative. Insulate every exposed joint with heat-shrink tubing or electrical tape and add strain relief with zip ties.
3. Before connecting electronics, use a multimeter to set the XL4005 output to approximately 6.0 V for the servo power rail. Connect all servo red power wires to this rail and all servo ground wires to the common ground rail.
4. Power ESP32 through VIN utilizing its linear regulator for 6v input.
5. Join the ESP32 ground, XL4005 output ground, servo grounds, and sensor grounds. A common ground is required for the PWM and sensor signals to work correctly.
6. Connect the servo PWM signal wires to the GPIO pins in the GPIO Mapping table: left drive GPIO14, right drive GPIO12, yaw GPIO13, main pitch GPIO15, second pitch GPIO26, output/shovel rotation GPIO4, and container lid GPIO25.
7. Connect the BH1750 and BME280 to 3.3 V and ground, with SDA on GPIO21 and SCL on GPIO22. These two modules share the same I2C bus.
8. Connect the analog soil EC sensor output to GPIO39 and power the module only at a voltage supported by the exact sensor board.
9. Connect the HC-SR04 trigger to GPIO16 and echo to GPIO17. A standard HC-SR04 echo can output 5 V, which is too high for an ESP32 GPIO; use a resistor divider or logic-level shifter on the echo line unless your exact module provides a 3.3 V-safe output.
10. Mount the sensors where the arm and wheels cannot strike them. The ultrasonic sensor should face forward with a clear view, while the environmental sensors should remain exposed to air and protected from direct soil contact.

### 7. Final Checks

1. With the wheels raised off the ground, inspect for shorts, reversed polarity, loose screws, pinched wires, and joints that cannot move freely.
2. Turn the system on briefly and confirm the regulated voltages before connecting every servo and sensor.
3. Test one servo at a time with conservative motion limits. Confirm the two drivetrain servos rotate in the expected directions and that no arm joint hits the chassis, soil container, or its own wiring.
4. Upload the firmware as described below, then run the robot on a clear floor away from people, pets, stairs, and loose objects. Keep the power switch within reach during the first autonomous test.

## Setting Up Firmware

1. Download and install [Thonny](https://thonny.org/), a beginner-friendly Python IDE that can be used to install and run MicroPython code on an ESP32.
2. If you are new to Thonny or MicroPython, follow the [Getting Started with Thonny MicroPython guide for ESP32 and ESP8266](https://randomnerdtutorials.com/getting-started-thonny-micropython-python-ide-esp32-esp8266/) to learn how to connect your ESP32 and upload code to it.
3. Once you are familiar with Thonny, open the `main.py` file located in the repository's `SOURCE CODE` folder.
4. Connect your ESP32 to your computer, upload `main.py` to the ESP32, and save it on the board as `main.py`.

When you toggle the robot's power button, the autonomous sequence will run automatically. After completing the sequence, the robot will enter roaming mode and move around until a randomly selected time, when it will run the autonomous sequence again.

## Repository Structure

* `BOM.csv` - bill of materials for the rover
* `SOURCE CODE/main.py` - compact autonomous MicroPython firmware
* `README.md` - project overview and instructions for setup
* `SOURCE CAD` - CAD step files for building it yourself
* `Pictures` - All pictures of schematic/prototype/cad

