# The following is the UDEV rules file I made to create symbolic links for the motor and lidar usb ports based on their serial numbers so that MOTOR0 is always motor zero, regardless if of whether or not it was registered as USB0

<b>To Use These Rules:</b>
1. Copy the contents of the bottommost code block into `/etc/udev/rules.d/79-robot.rules`

2. Set permissions for rules:
```sh
sudo chmod 644 79-robot.rules
sudo chown root:root 79-robot.rules
```

3. Restart the computer:
`sudo shutdown now -r`

4. Check devices to see if the rule worked:
`ls /dev | grep tty*`

<b>Contents of rules file:</b>

```rules
# using info from: https://gist.github.com/edro15/1c6cd63894836ed982a7d88bef26e4af
# and https://stackoverflow.com/questions/67123997/how-to-find-reasons-why-an-udev-rule-is-not-applied
# and https://unix.stackexchange.com/questions/39370/how-to-reload-udev-rules-without-reboot

ACTION=="add", SUBSYSTEM=="tty", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6015", ATTRS{serial}=="DT04KMKB", SYMLINK+="ttyMOTOR0"

ACTION=="add", SUBSYSTEM=="tty", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6015", ATTRS{serial}=="DT04KMK5", SYMLINK+="ttyMOTOR1"

ACTION=="add",, SUBSYSTEM=="tty", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6015", ATTRS{serial}=="DT04KMKD", SYMLINK+="ttyMOTOR2"

ACTION=="add",, SUBSYSTEM=="tty", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6015", ATTRS{serial}=="DT04KMK1", SYMLINK+="ttyMOTOR3"

ACTION=="add",, SUBSYSTEM=="tty", ATTRS{idVendor}=="10c4", ATTRS{idProduct}=="ea60", SYMLINK+="ttyLIDAR"
```
