#! /bin/python
import http.server
import socketserver


import os
import subprocess
def launch_server():
    FNULL = open(os.devnull, 'w')
    retcode = subprocess.call(['python', '-m', 'http.server','--directory', '/var/lib/jupyter/notebooks/OTWebControl/web','80'], stdout=FNULL, stderr=subprocess.STDOUT)
    
def launch_server2():
    os.system('/var/lib/jupyter/notebooks/OTWebControl/ttyd -p 82 sh -c "screen -qxR -m /var/lib/jupyter/notebooks/OTWebControl/browse.py"')

     
from threading import Thread


thread = Thread(target = launch_server)
thread.start()


from threading import Thread


thread = Thread(target = launch_server2)
thread.start()


input()