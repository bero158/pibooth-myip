
==============
pibooth-myip
==============

|PythonVersions|

``pibooth-myip`` is a plugin for the `pibooth`_ application.

This plugin makes installation of the photobooth without attached keyboard and mouse on the site easier.
The idea is to show IP address of the ``pibooth`` computer after installation of the photobooth on the site for easier remote access.

This plugin adds display of IP addresses associated to the computer at the first (waiting) screen.
If debug mode is on plugin displays IP address on every waiting screen.
IP addresses are re-evaluated every wait state entry and then every ten seconds.
It adds detected IP addresses to start messages with 'INFO' level.

Install
-------

Install netifaces (pip3 install netifaces)
Upload the plugin somewhere and append the absolute path to your pibooth.cfg (~/.config/pibooth/pibooth.cfg) to parameter 'plugins'::
   plugins = "/home/pi/pibooth/pibooth-myip/pibooth_myip.py"

Configuration
-------------

The plugin has no configuration. The only option here is you can enable/disable it

Example
-------

Here is an example of the rendering you can get with this plugin on the wait screen:

.. image:: https://github.com/bero158/pibooth-myip/blob/main/docs/images/waitscreen.png
   :align: center
   :alt: Example screenshot

.. --- Links ------------------------------------------------------------------

.. _`pibooth`: https://pypi.org/project/pibooth

.. |PythonVersions| image:: https://img.shields.io/badge/python-3.6+-red.svg
   :target: https://www.python.org/downloads
   :alt: Python 3.6+
