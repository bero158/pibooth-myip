# -*- coding: utf-8 -*-

"""Pibooth plugin to display IP addresses at first run"""

import time
import pygame
import pibooth
import getips
from pibooth.view.background import multiline_text_to_surfaces
from pibooth.utils import LOGGER
SECTION = 'MY IP'
IP_LBL = 'IP:'


__version__ = "1.0.0"

def show_texts(texts, win):
    for text, rect in texts:
        win.surface.blit(text, rect)

def place_text(text_color, win):
    win_rect = win.get_rect()
    text = "IP Addresses:\n" + getips.getIPStr(sep = "\n")
    if text:
        text_rect = pygame.Rect(win_rect.width*2 // 3,win_rect.width // 10,win_rect.width // 4, win_rect.height // 2)
        texts = multiline_text_to_surfaces(text,
                                           text_color,
                                           text_rect, 'bottom-left'
                                           )
        show_texts(texts,win)
        return texts

@pibooth.hookimpl
def pibooth_startup(cfg):
    
    LOGGER.info("pibooth-myip - Hello from pibooth-myip plugin")
    addrList = getips.getIPStr()
    LOGGER.info(f"My IPs: {addrList}")
    

@pibooth.hookimpl
def state_wait_enter(cfg, app, win):
    text_color = cfg.gettyped('WINDOW', 'text_color')
    if ((not hasattr(app, "pibooth_myip_shown")) or cfg.getboolean('GENERAL', 'debug')) :
        app.pibooth_myip_data={
            "text_color": text_color,
            "texts": place_text(text_color,win),
            "last_scan": time.time()
        }
        
@pibooth.hookimpl
def state_wait_exit(cfg, app, win):
    if hasattr(app, 'pibooth_myip_data'):
        del(app.pibooth_myip_data)
        app.pibooth_myip_shown=True

def draw_bg(surface,rect):
        color = pygame.Color(0,0,0)
        pygame.draw.rect(surface,color, rect) 

@pibooth.hookimpl
def state_wait_do(app, win):
    if hasattr(app, 'pibooth_myip_data'):
        if hasattr(app,"plugin_gallery"):
            if app.plugin_gallery["active"]:
                return #hide when gallery from gallery plugin is active
        show_texts(app.pibooth_myip_data["texts"],win)
        now = time.time()
        if (app.pibooth_myip_data["last_scan"] + 10 < now):
            for text in app.pibooth_myip_data["texts"]:
                draw_bg(win.surface,text[1])
            app.pibooth_myip_data.update({
            "texts": place_text(app.pibooth_myip_data["text_color"],win),
            "last_scan": time.time()
        })
         
@pibooth.hookimpl
def pibooth_configure(cfg):
    """Actions performed after loading of the configuration file or when the
    plugin is enabled for the first time. The ``cfg`` object is an instance
    of :py:class:`ConfigParser` class.

    :param cfg: application configuration
    """
    """Declare the new configuration options"""
    cfg.add_option(SECTION, "IP" , "" ,
                   "Descr",
                   getips.getIPStr(), "" )
    LOGGER.debug("pibooth_myip - Configure options added" )
