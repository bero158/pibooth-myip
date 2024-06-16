
==============
pibooth-myip
==============

|PythonVersions|

``pibooth-myip`` is a plugin for the `pibooth`_ application.

This plugin adds display of IP addresses associated to the computer at the first (waiting) screen.
If debug mode is on plugin displays IP address on every waiting screen.
IP addresses are re-evaluated every wait state entry.
It adds detected IP addresses as info to start messages.

Install
-------

Install netifaces (pip3 install netifaces)
Upload the plugin somewhere and appent the absolute path to your pibooth.cfg (~/.config/pigooth/pibooth.cfg) to parameter 'plugins'
aka: plugins = "/home/pi/pibooth/pibooth-myip/pibooth_myip.py"

Configuration
-------------

The plugin has no configuration. The only option here is you can enable/disable it

Example
-------

Here is an example of the rendering you can get with this plugin on the wait screen:

.. --- Links ------------------------------------------------------------------

.. _`pibooth`: https://pypi.org/project/pibooth

.. |PythonVersions| image:: https://img.shields.io/badge/python-3.6+-red.svg
   :target: https://www.python.org/downloads
   :alt: Python 3.6+

