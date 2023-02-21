#! /usr/bin/env python3
#SHEBANG
from flask import Blueprint, render_template
import napalm, re, datetime, os

Getconfig = Blueprint("Getconfig", __name__, static_folder='static', template_folder="templates")

@Getconfig.route('/home')
@Getconfig.route('/')
def home():
    return render_template('index.html')

def backup():
       
    path = os.getcwd()

    try:
            os.stat(path+'/Lab4_backup')
    except:
            os.mkdir(path+'/Lab4_backup')

    driver = napalm.get_network_driver('ios')

    ### device list to backup configuration
    device_list = ['198.51.100.1']

    ### username and password
    user = 'dinesh'
    passwd = 'cisco123'
    optional_args={'secret': 'cisco123'}


    for ip in device_list:

            device = driver(hostname=ip, username=user, password=passwd,optional_args=optional_args)
            device.open()
            config = device.get_config(retrieve='running')
            facts = device.get_facts()

            run_conf = config['running']
            #erase lines with "Building configuration", "Current Configuration" and "end"
            run_config = re.sub(r'Building configuration.*|Current configuration.*|end','',run_conf)

            date = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
            hostname = facts['hostname']

            ### create file with running config in backup_config folder
            file = open(path+'/Lab4_backup/'+hostname+'_'+date+'_'+'running-config','w')
            file.write(run_config)
            file.close()
            device.close()


backup()

    
