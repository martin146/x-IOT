# Pin definition table for IoT Board based on RP2040
# constants define pin_numbers without GP reference
# !!! all pins are fixed by board design !!!,
#    only DOUT and ADC pins can be assigned to specific roles
# ***********************************************************
# IF ANY QUESTION, SEE PROVIDED SCHEMATIC
# ***********************************************************

# ***********************************************************
# SECTION FOR DEFINITIONS OF USER CONNECTORS
# ***********************************************************
# GROVE ADC
# GROVE UART
# GROVE I2C
# GROVE DI/DO
# SENSOR 1
# SENSOR 1
# USR BUTTON 0
# USER BUTTON 1 (aka ADC2)

# ***********************************************************
# SECTION WITH DEFINITIONS FOR RP2040 MCU PINS
# ***********************************************************
# UART CP - Comm. board stats measurement on Core 1
CP_TX_PIN = 5
CP_RX_PIN = 4

# UART0 - Communication with modules etc.
UART_TX_PIN = 0
UART_RX_PIN = 1

# I2C for modules, OLED etc.
I2C_SCL_PIN = 13
I2C_SDA_PIN = 12

# SPI for communication modules, SD card etc.
SPI_CLK_PIN = 6
SPI_MOSI_PIN = 7
SPI_MISO_PIN = 8
SPI_CS_PIN = 9

# Range select for current measurement circuit
RANGE_SEL0_PIN = 2
RANGE_SEL1_PIN = 3

# Enable/disable output for communication module
MOD_EN_PIN = 25

# simple LED
LED_PIN = 15

# WS2812B RGB LEDs (3pcs by-default)
RGB_PIN = 16

# ADC pins (analog inputs)
ADC_0_PIN = 26
ADC_1_PIN = 27
ADC_2_PIN = 28
ADC_3_PIN = 29

# Digital output/input (DO/DI)
DIGITAL_0_PIN = 19
DIGITAL_1_PIN = 20
DIGITAL_2_PIN = 21
DIGITAL_3_PIN = 23

# Wake and reset pins for expansion connector (communication boards)
M2_RESET_PIN = 10
M2_WAKE_PIN = 11
M2_UART_WAKE_PIN = 18
PCI_WAKE_PIN = 22
PCI_W_DISABLE_PIN = 24
M2_W_DISABLE_PIN = 17

# User Button input
USR_BUT0_PIN = 14
