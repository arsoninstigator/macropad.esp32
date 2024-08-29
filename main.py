from machine import Pin, I2C
import ssd1306
import time

def handle_button1():
    oled.fill(0)
    oled.text('Button 1 Pressed', 0, 0)
    oled.show()

def handle_button2():
    oled.fill(0)
    oled.text('Button 2 Pressed', 0, 0)
    oled.show()

def handle_button3():
    oled.fill(0)
    oled.text('Button 3 Pressed', 0, 0)
    oled.show()

def handle_button4():
    oled.fill(0)
    oled.text('Button 4 Pressed', 0, 0)
    oled.show()

def handle_button5():
    oled.fill(0)
    oled.text('Button 5 Pressed', 0, 0)
    oled.show()

def handle_button6():
    oled.fill(0)
    oled.text('Button 6 Pressed', 0, 0)
    oled.show()

def handle_button7():
    oled.fill(0)
    oled.text('Button 7 Pressed', 0, 0)
    oled.show()

def handle_button8():
    oled.fill(0)
    oled.text('Button 8 Pressed', 0, 0)
    oled.show()

def handle_button9():
    oled.fill(0)
    oled.text('Button 9 Pressed', 0, 0)
    oled.show()


def handle_joystick_button():
    oled.fill(0)
    oled.text('Joystick Pressed', 0, 0)
    oled.show()

def handle_joystick_move():
    x = joystick_x.value()
    y = joystick_y.value()
    oled.fill(0)
    oled.text(f'Joystick X: {x}', 0, 0)
    oled.text(f'Joystick Y: {y}', 0, 10)
    oled.show()


# Define each button with individual variables
button1 = Pin(2, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(3, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(4, Pin.IN, Pin.PULL_DOWN)
button4 = Pin(5, Pin.IN, Pin.PULL_DOWN)
button5 = Pin(6, Pin.IN, Pin.PULL_DOWN)
button6 = Pin(7, Pin.IN, Pin.PULL_DOWN)
button7 = Pin(8, Pin.IN, Pin.PULL_DOWN)
button8 = Pin(9, Pin.IN, Pin.PULL_DOWN)
button9 = Pin(10, Pin.IN, Pin.PULL_DOWN)

# Define the joystick
joystick_x = Pin(26, Pin.IN, Pin.PULL_DOWN)
joystick_y = Pin(27, Pin.IN, Pin.PULL_DOWN)
joystick_button = Pin(28, Pin.IN, Pin.PULL_DOWN)

# Setup I2C for OLED display
i2c = I2C(0, scl=Pin(21), sda=Pin(20))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Display initial message
oled.text('Welcome to Macropad', 0, 0)
oled.show()
time.sleep(2)
oled.fill(0)
oled.show()

while True:
    if button1.value():
        handle_button1()
    elif button2.value():
        handle_button2()
    elif button3.value():
        handle_button3()
    elif button4.value():
        handle_button4()
    elif button5.value():
        handle_button5()
    elif button6.value():
        handle_button6()
    elif button7.value():
        handle_button7()
    elif button8.value():
        handle_button8()
    elif button9.value():
        handle_button9()

    if joystick_button.value():
        handle_joystick_button()
    else:
        handle_joystick_move()
    
    time.sleep(0.1)
