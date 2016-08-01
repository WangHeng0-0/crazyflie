#!/usr/bin/env python3

import yaml
import subprocess

with open("../ros_ws/src/crazyswarm/launch/crazyflies.yaml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

for crazyflie in cfg["crazyflies"]:
    id = "{0:02X}".format(crazyflie["id"])
    uri = "radio://0/{}/2M/E7E7E7E7{}".format(crazyflie["channel"], id)
    print(crazyflie["id"])
    subprocess.call(["rosrun crazyflie_tools reboot --uri " + uri], shell=True)