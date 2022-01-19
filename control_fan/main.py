
# -*- coding: utf-8 -*-

from gpiozero import OutputDevice
import time

ON_FAN_TEMP = 55
OFF_FAN_TEMP = 45
SLEEP_INTERVAL = 5
GPIO_PIN = 7

def log(origin, value):
    print(f'[{time.asctime()}]:[{origin}]: {value}')

def get_temperature():
    f = open("/sys/class/thermal/thermal_zone0/temp", "r")
    temp = f.read()
    f.close()
    temperature = temp[:2]
    log('get_temperature', )
    return int(temp[:2])


def main():
    fan = OutputDevice(GPIO_PIN)
    while True:
        temp = get_temperature()

        if(temp >= ON_FAN_TEMP and temp.value == 0):
            log('main', 'fan on')
            fan.on()

        if(temp <= OFF_FAN_TEMP and temp.value == 1):
            log('main', 'fan off')
            fan.off()

        time.sleep(SLEEP_INTERVAL)


if __name__ == '__main__':
    main()