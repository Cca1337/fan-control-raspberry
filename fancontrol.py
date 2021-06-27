#!/usr/bin/env python3

import subprocess
import time
import os
import re
import signal

ON_THRESHOLD = 65  # (degrees Celsius) Fan kicks on at this temperature.
OFF_THRESHOLD = 49  # (degress Celsius) Fan shuts off at this temperature.
SLEEP_INTERVAL = 100  # (seconds) How often we check the core temperature.

def get_temp():
   """Get the core temperature.
    Run a shell script to get the core temp and parse the output.
    Raises:
        RuntimeError: if response cannot be parsed.
    Returns:
        float: The core temperature in degrees Celsius.
    """
    cpuTempFile = open("/sys/class/thermal/thermal_zone0/temp", "r")
    cpu_temp = float(cpuTempFile.read()) / 1000
    print(cpu_temp)
    cpuTempFile.close()
    try:
        return cpu_temp
    except (IndexError, ValueError):
        raise RuntimeError('Could not parse temperature output.')

if __name__ == '__main__':
    # Validate the on and off thresholds
    if OFF_THRESHOLD >= ON_THRESHOLD:
        raise RuntimeError('OFF_THRESHOLD must be less than ON_THRESHOLD')


    while True:
        temp = get_temp()

        bezi_proces = subprocess.run(['pgrep', 'gpio'], capture_output=True)
        line = bezi_proces.stdout.decode('utf-8')
        # Start the fan if the temperature has reached the limit and the fan
        # isnt already running
        if temp > ON_THRESHOLD and not line:
            print("ZAPINAM")
            a = subprocess.run(['sudo', 'gpioset', '--mode=signal','--background', '0', '21=1'], capture_output=True)
        # Stop the fan if the fan is running and the temperature has dropped
        # to off threshold.
        elif temp < OFF_THRESHOLD and line:
            print("VYPINAM")
            try:
                pid_number = subprocess.run(['pgrep', 'gpio'], capture_output=True)
                pokracujeme = pid_number.stdout
                if pokracujeme:
                    pid_value = re.findall('\d+', str(pokracujeme))
                    pid_value = str(pid_value[0])
                    print(pid_value)
                    os.kill(int(pid_value), signal.SIGKILL)
                    print("process terminated")
            except (IndexError, ValueError):
                raise RuntimeError('Something went wrong.')
        time.sleep(SLEEP_INTERVAL)
