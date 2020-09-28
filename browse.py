#! /bin/python
import http.server
import socketserver




import urwid
import os

base_dir =  "/var/lib/jupyter/notebooks/OTWebControl"
os.chdir(base_dir)

choices = os.listdir(base_dir+"/commands")
choices = [x for x in choices if x.endswith(".py")]
tocall = ""
import subprocess
import re



def get_ips():
    output=subprocess.check_output("ifconfig -a", shell=True).decode("utf-8") .split(u"\n")
    ips = []
    for line in output:

        ip_match = re.search("inet addr:([^ ]+) ", line)

        if ip_match:
            ips.append(ip_match.group(1) )
    return ips

def format_command_file(x):
    return x.replace("command_","").replace("_"," ").replace(".py","")
    
def menu(title, choices):
    body = [urwid.Text(""),urwid.Text(title), urwid.Divider()]
    body.append(urwid.Text(u"Which command would you like to run?"))
    body.append(urwid.Text(u""))
    for c in choices:
        button = urwid.Button(format_command_file(c))
        urwid.connect_signal(button, 'click', item_chosen, c)
        body.append(urwid.AttrMap(button, None, focus_map='reversed'))
    body.append(urwid.Divider())
    body.append(urwid.Divider())
    import socket
    #ips = [i[4][0] for i in socket.getaddrinfo(socket.gethostname(), None)]
    #links = ["http://{}:82".format(x) for x in get_ips() if x != "127.0.0.1"]
    #link= " or ".join(links)
    #body.append(urwid.Text(u"To access log files please click on: {}".format(link)))
    #body.append(urwid.Text(""))
    return urwid.ListBox(urwid.SimpleFocusListWalker(body))

def item_chosen(button, choice):
    response = urwid.Text([u'Confirmation: do you want to start ', choice, u'?\n'])
    done = urwid.Button(u'Yes')
    urwid.connect_signal(done, 'click', launch_program, user_args=[choice])
    no = urwid.Button(u'No')
    urwid.connect_signal(no, 'click', exit_program)
    main.original_widget = urwid.Filler(urwid.Pile([response,
        urwid.AttrMap(done, None, focus_map='reversed'),urwid.AttrMap(no, None, focus_map='reversed')]))

import os
def launch_program(selected, button):
    global tocall
    tocall = os.path.join(base_dir,"commands", selected)
    subprocess.call(["clear"])
    
    #subprocess.call(["sh -c '/bin/python {}; read;'".format(tocall)],)
    #os.system("sh -c \"export RUNNING_ON_PI=1;export OT_SMOOTHIE_ID=AMA; python "+tocall+ "\"")
    raise urwid.ExitMainLoop()
    
def exit_program(button):
    main.original_widget =  urwid.Padding(menu(u'OT WEB CONTROL', choices), left=2, right=2)
    
main = urwid.Padding(menu(u'OT WEB CONTROL', choices), left=2, right=2)



top = urwid.Overlay(main, urwid.SolidFill(u'^'),
    align='center', width=('relative', 90),
    valign='middle', height=('relative', 90),
    min_width=20, min_height=9)



urwid.MainLoop(top, palette=[('reversed', 'standout', '')]).run()
print(tocall)
subprocess.call(["python","{}".format(tocall)],env={'OT_SMOOTHIE_ID':"AMA","RUNNING_ON_PI":"1"})
print("returned")

