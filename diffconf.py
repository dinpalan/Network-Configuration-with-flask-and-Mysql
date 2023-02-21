#! /usr/bin/env python3
#SHEBANG
from flask import Blueprint, render_template
import napalm
import csv

Diffconfig = Blueprint("Diffconfig", __name__, static_folder='static', template_folder="templates")

@Diffconfig.route('/home')
@Diffconfig.route('/')
def home():   
    with open("validdetails.txt","r") as f:
        lines = f.readlines()
    driver = napalm.get_network_driver('ios')
    device_list = ['198.51.100.1','198.51.100.4','198.51.100.5','198.51.100.3']
    user = lines[0].strip()
    passwd = lines[1].strip()
    optional_args={'secret': lines[1].strip()}
    for ip in device_list:
        if ip == '198.51.100.1':
            device = driver(hostname=ip, username=user, password=passwd,optional_args=optional_args)
            device.open()
            device.load_replace_candidate(filename='/home/netman/Desktop/LAB4/Lab4_backup/R1_Palanivelu_2022-02-14_21:21:48_running-config')
            print("Device R1 config difference:")
            print(device.compare_config())
        if ip == '198.51.100.4':
            device = driver(hostname=ip, username=user, password=passwd,optional_args=optional_args)
            device.open()
            device.load_replace_candidate(filename='/home/netman/Desktop/LAB4/Lab4_backup/R2_Palanivelu_2022-02-14_20:39:33_running-config')
            print("Device R2 config difference:")
            print(device.compare_config())
        if ip == '198.51.100.5':
            device = driver(hostname=ip, username=user, password=passwd,optional_args=optional_args)
            device.open()
            device.load_replace_candidate(filename='/home/netman/Desktop/LAB4/Lab4_backup/R3_Palanivelu_2022-02-14_21:08:01_running-config')
            print("Device R3 config difference:")
            print(device.compare_config())
        if ip == '198.51.100.3':
            device = driver(hostname=ip, username=user, password=passwd,optional_args=optional_args)
            device.open()
            device.load_replace_candidate(filename='/home/netman/Desktop/LAB4/Lab4_backup/R4_Palanivelu_2022-02-14_21:27:22_running-config')
            print("Device R4 config difference:")
            print(device.compare_config())
    return lines
        
