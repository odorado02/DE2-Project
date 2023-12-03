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

![DFR0478_pinout](https://github.com/odorado02/DE2-Project/assets/147071596/2956e84d-94d4-4496-9a73-d8aec0ac8f43)

- Keypad: Used to set the alarm configuration.

![SW-KEYPAD-MEM-4X4-800x800](https://github.com/odorado02/DE2-Project/assets/147071596/71590375-a94c-4f7e-bc0c-013cf2f32011)

- LCD screen module: Display used to show the time in binary.

![pmod_clp_vetsi](https://github.com/odorado02/DE2-Project/assets/147071596/3980f3cf-db62-42bc-9afa-33a6c91bd2a3)

- 7 segment LED display module: Display used to show the time in normal format.

![TM1637-7segment_over-965x676](https://github.com/odorado02/DE2-Project/assets/147071596/3863e896-ed7a-43d6-9130-6c2febf03244)

- Red LED: This led will turn on when the alarm set is incorrect.

![5mm red-800x800](https://github.com/odorado02/DE2-Project/assets/147071596/f71aac22-09a5-40e8-a4d9-aef7ff05a5c9)

- Multi-function shield: Although this module has a lot of different functions we only used the buzzer from it. When time reaches the alarm hour the buzzer will turn on.

![71UdT2Dw40L](https://github.com/odorado02/DE2-Project/assets/147071596/1b4324a8-233a-4bef-a492-47ee81762e16)

- Resistance:

![31j9N+LKvIL _AC_UF894,1000_QL80_](https://github.com/odorado02/DE2-Project/assets/147071596/aa801cf2-aa3d-4b31-8ce6-42dd8f21281d)

- Button: Used to stop the alarm.

![interruptor-push-button-botones-con-tapa-capucha-de-colores](https://github.com/odorado02/DE2-Project/assets/147071596/033e2776-20c4-4a4b-9f6e-74076d80a5df)


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


