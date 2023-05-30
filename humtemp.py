import lib.dht as dht
import machine
import utime

pin = machine.Pin(20)
data_dht = dht.DHT11(pin)

print('Start program')
while True:
    utime.sleep(2)
    
    data_dht.measure()
    print()
    print ( f" temperature (C) :{data_dht.temperature}")
    print ( f" humidity (%): {data_dht.humidity} ") 