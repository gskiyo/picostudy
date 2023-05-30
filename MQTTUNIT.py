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


#servo test
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

# servo.duty_u16(1638)
# time.sleep(0.5)
# servo.duty_u16(4915)
# time.sleep(0.5)
# servo.duty_u16(8100)
# time.sleep(0.5)
servo.duty_u16(dutyint)
# time.sleep(0.5)

#servo.duty_u16(int(pulse_width / (1000000.0 / servo.freq()))

#UART TEST
u = UART(1, 9600)
time.sleep(5)
# u.write('AT+MQAUTO=0\r\n')
#u.write('AT+SAVE\r\n')
# u.write('AT+BAUD?\r\n')

# u.write("AT+BAUD?\r\n")

#ATコマンドの送信と応答を読み込む関数
string = (u.read())      
print(string)

def SendATcommand(command):
    u.write(command+"\r\n")
    print(command)

    while True:
        if u.any() > 0:
            recive_bytes = (u.read())      
            recive_strings = recive_bytes.decode('ascii', 'ignore').replace('\\"','"')    
            print(recive_strings)
            break

#MQTT UNITの設定
# atcom = 'AT+MQSERVER="10.3.5.237",1883\r\n'
# # atcom = "AT+MQSERVER=\"pi02broker.local\",1883\r\n"
# # atcom = 'AT+MQSERVER="mqtt://test.mosquitto.org:1883",1883\r\n'
# u.write(atcom)
# print(atcom)
# while True:
#     if u.any() > 0:
#         string = (u.read())      
#         print(string)
#         break

# atcom = "AT+MQCLIENTID=\"NITTOBA\"\r\n"
# u.write(atcom)
# print(atcom)
# while True:
#     if u.any() > 0:
#         string = (u.read())      
#         print(string)
#         break


# # atcom = 'AT+MQUSERPWD="nittoba","g310gs"\r\n'
# atcom = 'AT+MQUSERPWD="",""\r\n'
# u.write(atcom)
# print(atcom)
# while True:
#     if u.any() > 0:
#         string = (u.read())      
#         print(string)
#         break

# #unit factory reset

# u.write("AT+MQRESETCFG\r\n")
# print("AT+MQRESETCFG\r\n")


# while True:
#     if u.any() > 0:
#         string = (u.read())      
#         print(string)
#         break

# SendATcommand('AT+SAVE')
# time.sleep(5)
# SendATcommand("AT+RESET")
# time.sleep(5)

# SendATcommand("AT+\"MQSERVER=pi02broker.local\"",1883)

#MQTT Unitの現在の設定の確認
SendATcommand('AT+BAUD?')
SendATcommand('AT+NETIP?')
SendATcommand('AT+NETMAC?')
SendATcommand('AT+MQAUTO?')
SendATcommand('AT+NETDHCPEN?')
SendATcommand('AT+MQSERVER?')
SendATcommand('AT+MQCLIENTID?')
SendATcommand('AT+MQUSERPWD?')
SendATcommand('AT+VERSION?')




SendATcommand('AT+MQSTATUS?')
time.sleep(10)
SendATcommand('AT+MQSTATUS?')
time.sleep(10)
SendATcommand('AT+NETIP?')
time.sleep(10)


#受信待ち
while True:
    # u.write(buff)
    if u.any() > 0:
        # string = (u.read(12))
        recive_bytes = (u.read())      
        recive_strings = recive_bytes.decode('ascii', 'ignore').replace('\\"','"')
        print(recive_strings)


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
#     #time.sleep(1)P
