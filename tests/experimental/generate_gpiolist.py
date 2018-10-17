from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import json
import subprocess

# README: Copy this file over to target and run from /tmp/gpiosnames"

def gen_gpio_json():
    '''
    Following method will read every gpio for contents and publish a json file
    at /tmp/gpiolist.json
    '''
    result = {}
    presult = {}
    cmd = "ls -1"
    gpio_list = subprocess.check_output(cmd, shell=True).decode().splitlines()
    for item in gpio_list:
        cmd = "cat /tmp/gpionames/" + item + "/" + "direction"
        result['direction'] = subprocess.check_output(cmd, shell=True).decode().strip('\n')
        cmd = "cat /tmp/gpionames/" + item + "/" + "active_low"
        result['active_low'] = subprocess.check_output(cmd, shell=True).decode().strip('\n')
        cmd = "cat /tmp/gpionames/" + item + "/" + "edge"
        result['edge'] = subprocess.check_output(cmd, shell=True).decode().strip('\n')
        cmd = "cat /tmp/gpionames/" + item + "/" + "value"
        result['value'] = subprocess.check_output(cmd, shell=True).decode().strip('\n')
        presult[item] = result
        result = {}
    fresult = {
                "gpios": presult
              }
    handle = open("/tmp/gpiolist.json", "a+")
    handle.write(json.dumps(fresult))
    handle.close()

if __name__ == "__main__":
    gen_gpio_json()
