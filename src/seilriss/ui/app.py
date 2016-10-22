import pygame
import seilriss.pygameui as ui


class SeilrissApp(ui.App):

    def run(self):
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        super(SeilrissApp, self).run()

    def event(self, ev):
        if ev.type == pygame.USEREVENT:
            ui.scene.current.timer(ev)

    def onQuit(self):
        pass
