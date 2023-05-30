from machine import Pin, I2C, UART, PWM
from lib.ssd1306 import SSD1306_I2C
import time
import utime
import framebuf

WIDTH  = 128                                            # oled display width
HEIGHT = 32                                             # oled display height


i2c = I2C(0)                                            # Init I2C using I2C0 defaults, SCL=Pin(GP9), SDA=Pin(GP8), freq=400000
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config


oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  # Init oled display

button = Pin(20, Pin.IN, Pin.PULL_DOWN)
led = Pin(18, Pin.OUT)
ledOnboard = Pin(25, Pin.OUT)

# School Emblem 32x32
buffer = bytearray(b"\x00\x01\x00\x00\x00\x03\x80\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x08\x01\x00\x20\x04\x03\x80\x40\x03\x03\x81\x80\x03\x83\x83\x80\x01\xE7\xCF\x00\x00\xE7\xCE\x00\x00\xE6\xCE\x00\x00\x01\x00\x00\x00\x04\x40\x00\x00\xE9\x2E\x00\x07\xE7\xCF\xC0\x7F\xD2\x97\xFC\x07\xE1\x0F\xC0\x00\xEA\xAE\x00\x00\x00\x00\x00\x00\x05\x40\x00\x00\xE6\xCE\x00\x00\xE7\xCE\x00\x01\xE7\xCF\x00\x03\x83\x83\x80\x03\x03\x81\x80\x04\x03\x80\x40\x08\x01\x00\x20\x00\x01\x00\x00\x00\x01\x00\x00")

# Load the image into the framebuffer (the image is 32x32)
fb = framebuf.FrameBuffer(buffer, 32, 32, framebuf.MONO_HLSB)

# Clear the oled display in case it has junk on it.
oled.fill(0)

# Blit the image from the framebuffer to the oled display
oled.blit(fb, 10,0)

# Add some text
oled.text("NIT,TOBA",42,5)
oled.text("KIYOSHIGE",42,15)
oled.text("Yasushi",42,25)

# Finally update the oled display so the image & text is displayed
oled.show()
i = 0
while i < 5:
    #oled.scroll(1,0)
    oled.invert(1)
    ledOnboard.value(0)
    time.sleep(0.1)
    oled.invert(0)
    ledOnboard.value()
    time.sleep(0.1)
    i+=1

#uart test
# uart0 = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

# txData =b'hello world\n\r'
# uart0.write(txData)
# time.sleep(0.1)
# rxData = bytes()

servo = PWM(Pin(16, Pin.OUT))
servo.freq(50)  #PWM 50Hz(20ms)


angle = 90
max_pulse_width = 2500
min_pulse_width = 500
angle = max(0,min(180, angle))
pulse_width = angle / 180.0 * (max_pulse_width - min_pulse_width) + min_pulse_width
duty = pulse_width / (1000000.0 / servo.freq())
dutyint = int(duty*65535)

print(servo.freq())
print(angle)
print(pulse_width)
print(duty)
print(dutyint)

servo.duty_u16(1638)
time.sleep(2)
servo.duty_u16(4915)
time.sleep(2)
servo.duty_u16(8191)
time.sleep(2)
servo.duty_u16(dutyint)
time.sleep(2)

#servo.duty_u16(int(pulse_width / (1000000.0 / servo.freq()))



# while True:
#     #button read & #LEDO ON/OFF
#     # led.value(1)
#     led.value(button.value())
#     #servo test
#     # servo.freq(50)
#     # servo.duty_u16(int(duty))
#     time.sleep(2)
#     # servo.duty_u16(62260)
#     time.sleep(2)
#     #time.sleep(1)
