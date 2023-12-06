# DE2-Project

### Team members

- **David Corrionero**: Responsible for WiFi connection and syncronization with network time servers
- **Aitana del Carmen**: Responsible for converting current time from decimal to binary
- **Oier Dorado**: Responsible for alarms and its additional features (such as sounds, confirmation via led)

## Theoretical description and explanation

*Task: Digital clock Max 2 groups. Design and implement a digital clock using the MicroPython programming language on the ESP32 microcontroller. The clock will not only display the current time in both decimal and binary formats but will also include additional features such as alarms and synchronization with network time servers*

The digital clock is firstly connected to the network in order to get the current time as fast as possible. The process of taking the time is repeated every second using a timer. Next, the display shows the current time in binary and in normal format and they are updated every second also.

Apart from that, alarms can be set as soon as the digital clock gets the current time. On the one hand, there is a keypad with which you can write the alarm time and the value is saved automatically in the code; Furthermore, whenever the hour written is not coherent, a red light is turned on with a view to warn you about the error and the value is eliminated. On the other hand, there is a buzzer that starts working when the alarm set matches the current time and the blue button needs to be pressed to stop such alarm.

## Hardware description and demo application

In the next image you can see our hole composition:

![IMG_2538](https://github.com/odorado02/DE2-Project/assets/147071596/64031a4d-3fd3-4cf4-825a-d9b72c0b244e)

The hardware is composed by 7 components:

- ESP32 microcontroller: The component which runs all the program and coordinates all the other components. Also is the ono which connects to the network in order to get the hour.

<img src="https://github.com/odorado02/DE2-Project/assets/147071596/2956e84d-94d4-4496-9a73-d8aec0ac8f43" width="450" height="350">

- Keypad: Used to set the alarm configuration.

<img src="https://github.com/odorado02/DE2-Project/assets/147071596/71590375-a94c-4f7e-bc0c-013cf2f32011" width="450" height="350">

- LCD screen module: Display used to show the time in binary.

<img src="https://github.com/odorado02/DE2-Project/assets/147071596/3980f3cf-db62-42bc-9afa-33a6c91bd2a3" width="450" height="350">

- 7 segment LED display module: Display used to show the time in normal format.

<img src="https://github.com/odorado02/DE2-Project/assets/147071596/3863e896-ed7a-43d6-9130-6c2febf03244" width="450" height="350">

- Red LED: This led will turn on when the alarm set is incorrect.

<img src="https://github.com/odorado02/DE2-Project/assets/147071596/f71aac22-09a5-40e8-a4d9-aef7ff05a5c9" width="450" height="350">

- Multi-function shield: Although this module has a lot of different functions we only used the buzzer from it. When time reaches the alarm hour the buzzer will turn on.

<img src="https://github.com/odorado02/DE2-Project/assets/147071596/1b4324a8-233a-4bef-a492-47ee81762e16" width="450" height="350">

- Resistance:

<img src="https://github.com/odorado02/DE2-Project/assets/147071596/aa801cf2-aa3d-4b31-8ce6-42dd8f21281d" width="450" height="350">

- Button: Used to stop the alarm.

<img src="https://github.com/odorado02/DE2-Project/assets/147071596/033e2776-20c4-4a4b-9f6e-74076d80a5df" width="450" height="350">

## Software description

Conceptual flowchart:

![Conceptual flowchart drawio](https://github.com/odorado02/DE2-Project/assets/147071596/4b1f3d78-3855-4ed2-99ea-07d8a36d94fa)

List of codes:

1. `main.py`: This is the main program to run. This program configures the timers, the global variables, updates the displays and sets the alarm.

1. `BinaryHourDisplay.py`: This program is the one in charge of displaying the binary time in the LCD display.

1. `wifiConnection.py`: This program connects the ESP32 to the wifi network and there are also functions to ask for the current time. `tm1367`is the respective library.

1. `DecimalHourDisplay.py`: This code is the one in charge of displaying the decimal hour in the seven segment module display. We downloaded a library `tm1637` for the display.

1. `ScanMatrixKeypad.py`: This function scans the key pressed in the matrix keypad and returns its value.

*All flowcharts of the respective codes and functions have been added into the repository*

## Instructions

*Short video*

https://drive.google.com/file/d/1OMqX3RkZyKgxi6WhY67Ui5PE5L0LpFwY/view?usp=drive_link

**Binary Clock**

In binary, for the values that equal 1 in the hour on binary, the display shows black blocks, and similarly, for the values that equal zero, the display leaves the blocks in blank.

**Setting Alarm**

1. Press "*" to start.
1. Write your alarm by pressing 4 numbers (correct form: HHmm), otherwise there will be an error and the red led will turn on.
1. Press "A" (Accept) if the alarm time is the one you want. Otherwise press "C" (Cancel) and repeat step 2.
1. If you want to change the alarm set, repeat steps 1 2 3 again.
1. The alarm buzzer will sound when the alarm time is the same as the current time.
1. To stop the alarm buzzer the blue button needs to be pressed.
1. To delete the alarm you can press "*" to set a new alarm or you can press "D" to delete the current alarm and not to configure another alarm.

## References

- Code:
    -  mcauser, "micropython-tm1637" [Online]. Available: https://github.com/mcauser/micropython-tm1637.git
    -  T. Fryza, “MicroPython on ESP32/ESP8266 microcontollers.” [Online]. Available: https://github.com/tomas-fryza/esp-micropython
