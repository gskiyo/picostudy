from machine import Pin, PWM
import time

# button = Pin(20, Pin.IN, Pin.PULL_DOWN)
button = Pin(27, Pin.IN, Pin.PULL_DOWN)
speaker = PWM(Pin(16, Pin.OUT))




while True:
    if button.value() == 1:
        speaker.duty_u16(0) #duty 0にして音を消す
        speaker.freq(2000) # 周期 1kHz
        speaker.duty_u16(0x0800) # duty 音量 0-65535
        time.sleep_ms(100)
        speaker.duty_u16(0) #duty 0にして音を消す
        speaker.freq(1000) # 周期 1kHz
        speaker.duty_u16(0x0800) # duty 音量 0-65535
        time.sleep_ms(100)
        speaker.duty_u16(0) #duty 0にして音を消す



