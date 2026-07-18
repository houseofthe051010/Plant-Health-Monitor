# ESP32 Plant Health Monitor Rover

A self-driving ESP32-based soil sampling rover consisting of a tank-drive chassis, a multi-servo soil collector arm, and a small environmental sensors suite. Upon powering on, the rover will run its complete soil sampling routine, do a randomized drive sequence, stop, and idle.

I built this to sample soil health from my garden and this is just a prototype, not the real version yet, I will build another iteration but this is what I have currently.

## Features

* Autonomous start-up and work
* Two-servo tank drive
* Seven servos total

  * Two continuous-rotation drive servos
  * Four arm position servos
  * One sample chamber closing servo
* Smooth servo movement
* Simultaneous two-servos action
* Shovel shaking to dump collected soil
* Random forward, turning, and curved driving segments
* Autonomous drive stop after the sequence execution
* Soil electrical conductivity measurement
* Temperature, humidity, pressure, and light measurements support
* Front ultrasound distance measurement
* 2S 18650 battery-based power supply with a step-down converter
* No extra Python packages required for the core autonomous work

## Proof Pictures

Here is the demo video I have on the robot:

https://www.youtube.com/shorts/W9_TdJyh92A

### CAD Prototype

![CAD Prototype](Pictures/CAD-prototype.png)

The CAD prototype shows the planned rover structure, including the tank-drive chassis and the soil collection mechanism layout.

### Circuit Schematic

![Updated Circuit Schematic](Schematics/UpdatedCircuitSchematicV2.png)

The circuit schematic shows how the ESP32 connects to the drivetrain, servo arm system, sensors, and power system.

### Real-Life Prototype

![Real-Life Prototype](Pictures/real-life-prototype.png)

The real-life prototype shows the current physical version of the rover built for testing garden soil sampling, sensor integration, and servo-controlled soil collection.

## Hardware Description

The rover utilizes ESP32 microcontroller. Tank drive is controlled using two PWM outputs, acting as continuous-rotation servos. Soil collection uses five additional PWM outputs to actuate servos of the arm and close the sample chamber.

Sensors include a BH1750 light sensor, a BME280 environmental sensor, an HC-SR04 ultrasound distance sensor, and an analog soil electrical conductivity sensor. Both BH1750 and BME280 are on the same I2C bus.

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

BH1750 detects the ambient light level. Sensor is wired via I2C bus, which is shared with BME280.

| Pin | Connection |
| --- | ---------- |
| VCC | 3.3 V      |
| GND | GND        |
| SDA | GPIO21     |
| SCL | GPIO22     |

### BME280 Environmental Sensor

BME280 measures temperature, humidity, and air pressure. It is also wired via I2C bus, shared with BME280.

| Pin | Connection |
| --- | ---------- |
| VCC | 3.3 V      |
| GND | GND        |
| SDA | GPIO21     |
| SCL | GPIO22     |

### HC-SR04 Ultrasonic Sensor

HC-SR04 is used as a front distance sensor for obstacle detection.

| Pin     | Connection   |
| ------- | ------------ |
| VCC     | 3.3 V        |
| GND     | GND          |
| Trigger | GPIO16 / RX2 |
| Echo    | GPIO17 / TX2 |

### Analog Soil EC Sensor

Soil Electrical Conductivity sensor is connected to VN/GPIO39 of the ESP32.

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

The rover is powered from a 2S 18650 battery pack. 2S lithium-ion battery pack provides about 7.4V nominally and 8.4V at full charge. This voltage level is too much for standard 5V servos and ESP32 GPIO pins, so the rover uses an XL4005 buck converter to step-down the voltage.

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

These are approximate instructions for assembling the current prototype. The design was adjusted and reprinted several times during the build, so test-fit every printed part before using glue and check the completed CAD model if a part's orientation is unclear.

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

## License

This project is licensed under the [MIT License](LICENSE). Copyright (c) 2026 Aditya Verma.
