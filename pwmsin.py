from machine import Pin, PWM
import utime
import math

# PWMの設定
pwm_pin = Pin(16, Pin.OUT)  # PWM出力ピンの指定
pwm = PWM(pwm_pin)  # PWMオブジェクトの作成
pwm.freq(1000)  # PWM周波数の設定

# Sin波形を生成するための変数
SAMPLE_RATE = 100  # サンプリング周波数
SINE_LENGTH = 100  # Sin波形の長さ
sine_table = []  # Sin波形のデータを格納する配列

# Sin波形のデータを生成する
for i in range(SINE_LENGTH):
    # 0~1の範囲でSin波形のデータを生成する
    value = (math.sin((2 * math.pi * i) / SINE_LENGTH) + 1) / 2
    # PWMデューティサイクルに変換する
    duty_cycle = int(value * 1023)
    sine_table.append(duty_cycle)

# Sin波形を生成する
while True:
    for i in range(SINE_LENGTH):
        pwm.duty_u16(sine_table[i])
        # サンプリング周波数に応じて待機する
        utime.sleep_us(int(1000000 / SAMPLE_RATE))