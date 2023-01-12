'''
Example of how set vaiable on a channel.

MAKE SURE A TEST WITH A VARIABLE IS SET ON CHANNEL
'''
import json
import pymacnet 
import time
import sys

config_path = 'example_config_1.json'
with open(config_path, 'r') as file:
    config_dict = json.load(file)
    
maccor_interface = pymacnet.MaccorInterface(config_dict)
if not maccor_interface.start():
    sys.exit("failed to create connection!")

set_current = 0.01

for i in range(0,5):
    print(maccor_interface.set_channel_variable(var_num = 1, var_value = set_current))
    print(set_current)
    set_current += set_current
    time.sleep(5)