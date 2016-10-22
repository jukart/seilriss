========
Seilriss
========

Installation
============

Mac-OS
------

Install pygame::

    $ sudo port install pygame

Create a virtual python::

    $ mkvirtualenv seilriss --system-site-packages


Additional Packages
-------------------


Run on the MAC
==============

Commands to run the app on the mac::

    $ workon seilriss
    $ pip install -e .
    $ seilriss


Raspberry Pi 3
==============

Setup SD-Card
-------------

Write image to sd-card::

    $ diskutil list
    $ diskutil unmount /dev/disk<x>s1
    $ sudo dd if=<file>.img of=/dev/rdisk2 bs=1m


Setup wlan
----------

    $ sudo iwlist wlan0 scan
    $ sudo vi /etc/wpa_supplicant/wpa_supplicant.conf

Add this to the end of the file::

    network={
      ssid="<network name (ESSID)>"
      psk="<password>"
    }

    $ sudo ifdown wlan0
    $ sudo ifup wlan0

Permanently switch off power management of wlan interfaces::

    $ sudo vi /etc/network/interfaces

Add this line::

    wireless-power off

Manually switch off power management::

    $ sudo iwconfig wlan0 power off

Scan for raspberry ip::

    $ nmap -p 22 --open -sV 192.168.1.0/24


Node RED
--------

On a fresh jessie run::

    $ update-nodejs-and-nodered

See also: http://nodered.org/docs/hardware/raspberrypi

Enable autostart for node RED::

    $ sudo systemctl enable nodered.service


Display
-------

Documentation: https://cdn-learn.adafruit.com/downloads/pdf/adafruit-2-4-pitft-hat-with-resistive-touchscreen-mini-kit.pdf

Use this jessie image for Raspberry Pi3 with 2.4" display: http://adafru.it/mA9

Disable boot screen::

    $ sudo vi /boot/cmdline.txt

remove: `fbcon=map:10 fbcon=font:VGA8x8`


Setup Python
------------

    $ sudo apt-get install python-pygame
