from machine import Pin, PWM
import time

button = Pin(27, Pin.IN, Pin.PULL_DOWN)
buzzer1 = PWM(Pin(16, Pin.OUT))
buzzer2 = PWM(Pin(18, Pin.OUT))

# 使用する音の周波数を宣言しておく。
C5 = 523.2511 #高いド
D5 = 587.3295 #高いレ
E5 = 659.2511 #高いミ

B4 = 493.8883
A4s = 466.1638
A4 = 440.0
G4 = 391.9954

F5 = 698.4565
D5s = 622.2540
F5 = 698.4565
G5 = 783.9909
volume1 = 0x0400
volume2 = 0x0200

print("Press button to SATRT!!")
while True:
    if button.value() == 1:
        buzzer1.duty_u16(0) #duty 0にして音を消す
        
        time.sleep_ms(100)
        buzzer1.freq(int(F5)) # 周期 1kHz
        buzzer2.freq(int(C5)) # 周期 1kHz
        buzzer1.duty_u16(volume1) # duty 音量 0-65535
        buzzer2.duty_u16(volume2) # duty 音量 0-65535
        time.sleep_ms(100)
        buzzer1.duty_u16(0) #duty 0にして音を消す
        buzzer2.duty_u16(0) #duty 0にして音を消す

        time.sleep_ms(50)
        buzzer1.freq(int(F5)) # 周期 1kHz
        buzzer2.freq(int(B4)) # 周期 1kHz
        buzzer1.duty_u16(volume1) # duty 音量 0-65535
        buzzer2.duty_u16(volume2) # duty 音量 0-65535
        time.sleep_ms(100)
        buzzer1.duty_u16(0) #duty 0にして音を消す
        buzzer2.duty_u16(0) #duty 0にして音を消す

        time.sleep_ms(50)
        buzzer1.freq(int(F5)) # 周期 1kHz
        buzzer2.freq(int(A4s)) # 周期 1kHz
        buzzer1.duty_u16(volume1) # duty 音量 0-65535
        buzzer2.duty_u16(volume2) # duty 音量 0-65535
        time.sleep_ms(100)
        buzzer1.duty_u16(0) #duty 0にして音を消す
        buzzer2.duty_u16(0) #duty 0にして音を消す

        time.sleep_ms(50)
        buzzer1.freq(int(F5)) # 周期 1kHz
        buzzer2.freq(int(A4)) # 周期 1kHz
        buzzer1.duty_u16(volume1) # duty 音量 0-65535
        buzzer2.duty_u16(volume2) # duty 音量 0-65535
        time.sleep_ms(200)
        buzzer1.duty_u16(0) #duty 0にして音を消す
        buzzer2.duty_u16(0) #duty 0にして音を消す

        time.sleep_ms(50)
        buzzer1.freq(int(D5s)) # 周期 1kHz
        buzzer2.freq(int(G4)) # 周期 1kHz
        buzzer1.duty_u16(volume1) # duty 音量 0-65535
        buzzer2.duty_u16(volume2) # duty 音量 0-65535
        time.sleep_ms(200)
        # buzzer1.duty_u16(0) #duty 0にして音を消す
        # buzzer2.duty_u16(0) #duty 0にして音を消す

        time.sleep_ms(25)
        buzzer1.freq(int(G5)) # 周期 1kHz
        buzzer2.freq(int(A4s)) # 周期 1kHz
        buzzer1.duty_u16(volume1) #duty 0にして音を消す
        buzzer2.duty_u16(volume2) # duty 音量 0-65535
        time.sleep_ms(200)
        buzzer1.duty_u16(0) #duty 0にして音を消す
        buzzer2.duty_u16(0) #duty 0にして音を消す

        time.sleep_ms(50)
        buzzer1.freq(int(F5)) # 周期 1kHz
        buzzer2.freq(int(A4)) # 周期 1kHz
        buzzer1.duty_u16(volume1) # duty 音量 0-65535
        buzzer2.duty_u16(volume2) # duty 音量 0-65535
        time.sleep_ms(200)
        buzzer1.duty_u16(0) #duty 0にして音を消す
        buzzer2.duty_u16(0) #duty 0にして音を消す

        # time.sleep_ms(100)
        buzzer1.freq(int(F5)) # 周期 1kHz
        buzzer2.freq(int(A4)) # 周期 1kHz
        buzzer1.duty_u16(volume1) # duty 音量 0-65535
        buzzer2.duty_u16(volume2) # duty 音量 0-65535
        time.sleep_ms(500)
        buzzer1.duty_u16(0) #duty 0にして音を消す
        buzzer2.duty_u16(0) #duty 0にして音を消す
