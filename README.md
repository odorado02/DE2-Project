# DE2-Project

### Team members

- **David Corrionero**: Responsible for WiFi connection and syncronization with network time servers
- **Aitana del Carmen**: Responsible for converting current time from decimal to binary
- **Oier Dorado**: Responsible for alarms and its additional features (such as sounds, confirmation via led)

## Theoretical description and explanation

*Task: Digital clock Max 2 groups. Design and implement a digital clock using the MicroPython programming language on the ESP32 microcontroller. The clock will not only display the current time in both decimal and binary formats but will also include additional features such as alarms and synchronization with network time servers*

The digital clock is firstly connected to the network in order to get the current time as fast as possible. This process is repeated every second using a timer. Next, the display shows the current time in binary and in normal format and they are updated every second also.

Apart from that, alarms can be set as soon as the digital clock gets the current time. On the one hand, there is a keypad with which you can write the alarm time and the value is saved automatically in the code; Furthermore, whenever the hour written is not coherent, a red light is turned on with a view to warn you about the error and the value is eliminated. On the other hand, there is a buzzer that starts working when the alarm set matches the current time and button to stop such alarm.

## Hardware description and demo application

Insert descriptive text and schematic(s) of your implementation.

![IMG_2538](https://github.com/odorado02/DE2-Project/assets/147071596/64031a4d-3fd3-4cf4-825a-d9b72c0b244e)

The hardware is composed by 7 components:

- ESP32 microcontroller: The component which runs all the program and coordinates all the other components. Also is the ono which connects to the network in order to get the hour.

Keypad: 
LCD screen module:
LED display:
Red LED:
Multi-function shield:
Resistance:
Button???????????

##Software description

Put flowchats of your algorithm(s) and direct links to source files.

##Instructions

Write an instruction manual for your application, including photos and a link to a short app video.

In binary, for the values that equal 1 in the hour on binary, the display shows black blocks, and similarly, for the values that equal zero, the display leaves the blocks in blank.

SETTING ALARM → Keypad
Press x
Write your alarm by pressing 4 numbers (correct form: HHmm), otherwise there will be an error
If necessary, press x to repeat step 2
Press x to save the alarm
If you want to set more alarms, repeat 1 2 3 steps again.


