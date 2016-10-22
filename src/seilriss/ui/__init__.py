# -*- coding: utf-8 -*-
import pygame
import seilriss.pygameui as ui

from . import consts
from .import scenes
from .app import SeilrissApp


def run():
    ui.init('Seilriss', consts.SCREEN_SIZE.size)
    pygame.mouse.set_visible(False)
    ui.scene.push(scenes.Main())
    SeilrissApp().run()
