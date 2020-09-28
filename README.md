At the time of writing you have to opt in to the Alpha channel of OpenTrons to update your robot to one with `screen`.

## Installation

Go to Jupyter notebook on the OT2. Create a terminal.

Go to the notebooks directory:
```
cd /var/lib/jupyter/notebooks/
```

Get this package:
```
git clone https://github.com/theosanderson/OTWebControl
```

Copy the launcher script to the boot-up directory:
```
cp /var/lib/jupyter/notebooks/OTWebControl/startup  /data/boot.d/
```

Reboot:
```
reboot
```

## Usage

You should now be able to access a web server at `http://[YOUR ROBOT IP]`. If you click the Launch web control you should be presented with a menu of commands to run.

To add commands to this menu simply create python files in the `commands` directory. Anything you put in the `web` directory can be accessed at the web server.



