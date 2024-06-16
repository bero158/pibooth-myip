# -*- coding: utf-8 -*-

"""Pibooth plugin to display IP addresses at first run"""

import pygame
import pibooth
import getips
from pibooth.view.background import multiline_text_to_surfaces
from pibooth.utils import LOGGER

__version__ = "1.0.0"


def place_text(cfg, win):
    win_rect = win.get_rect()
    text = "IP Addresses:\n" + getips.getIPStr(sep = "\n")
    if text:
        text_rect = pygame.Rect(win_rect.width*2 // 3,win_rect.width // 10,win_rect.width // 4, win_rect.height // 2)
        texts = multiline_text_to_surfaces(text,
                                           cfg.gettyped('WINDOW', 'text_color'),
                                           text_rect, 'bottom-left'
                                           )
        for text, rect in texts:
            win.surface.blit(text, rect)
        return texts

@pibooth.hookimpl
def pibooth_startup(cfg):
    
    LOGGER.info("pibooth-myip - Hello from pibooth-myip plugin")
    addrList = getips.getIPStr()
    LOGGER.info(f"My IPs: {addrList}")
    

@pibooth.hookimpl
def state_wait_enter(cfg, app, win):
    if ((not hasattr(app, "pibooth_myip_shown")) or cfg.getboolean('GENERAL', 'debug')) :
        app.pibooth_myip_shown = True
        place_text(cfg,win)
    