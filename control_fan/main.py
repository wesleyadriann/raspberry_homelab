
# -*- coding: utf-8 -*-

from gpiozero import OutputDevice, CPUTemperature
import time
import logging as log

ON_FAN_TEMP = 55
OFF_FAN_TEMP = 45
SLEEP_INTERVAL = 5
GPIO_PIN = 4

def logConfig(tag, value):
   log.basicConfig(level=log.INFO)

def main():
    fan = OutputDevice(GPIO_PIN)
    while True:
        temp = CPUTemperature().temperature
        log.info(f'temperature - {temp} C')

        if(temp >= ON_FAN_TEMP and fan.value == 0):
            log.info('main - fan on')
            fan.on()

        if(temp <= OFF_FAN_TEMP and fan.value == 1):
            log.info('main - fan off')
            fan.off()

        time.sleep(SLEEP_INTERVAL)


if __name__ == '__main__':
    logConfig()
    main()