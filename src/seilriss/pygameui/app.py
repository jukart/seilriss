import pygame


class App(object):

    def __init__(self):
        self.clock = pygame.time.Clock()

    def run(self):
        from seilriss import pygameui as ui
        down_in_view = None
        while True:
            dt = self.clock.tick(10)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.onQuit()
                    pygame.quit()
                    import sys
                    sys.exit()
                mousepoint = pygame.mouse.get_pos()
                if e.type == pygame.MOUSEBUTTONDOWN:
                    hit_view = ui.scene.current.hit(mousepoint)
                    if (hit_view is not None and
                        not isinstance(hit_view, ui.scene.Scene)
                       ):
                        ui.focus.set(hit_view)
                        down_in_view = hit_view
                    else:
                        ui.focus.set(None)
                    pt = hit_view.from_window(mousepoint)
                    hit_view.mouse_down(e.button, pt)
                elif e.type == pygame.MOUSEBUTTONUP:
                    hit_view = ui.scene.current.hit(mousepoint)
                    if hit_view is not None:
                        if down_in_view and hit_view != down_in_view:
                            down_in_view.blurred()
                            ui.focus.set(None)
                        pt = hit_view.from_window(mousepoint)
                        hit_view.mouse_up(e.button, pt)
                    down_in_view = None
                elif e.type == pygame.MOUSEMOTION:
                    if down_in_view and down_in_view.draggable:
                        pt = down_in_view.from_window(mousepoint)
                        down_in_view.mouse_drag(pt, e.rel)
                    else:
                        ui.scene.current.mouse_motion(mousepoint)
                elif e.type == pygame.KEYDOWN:
                    if ui.focus.view:
                        ui.focus.view.key_down(e.key, e.unicode)
                    else:
                        ui.scene.current.key_down(e.key, e.unicode)
                elif e.type == pygame.KEYUP:
                    if ui.focus.view:
                        ui.focus.view.key_up(e.key)
                    else:
                        ui.scene.current.key_up(e.key)
                else:
                    self.event(e)
            ui.scene.current.update(dt / 1000.0)
            ui.scene.current.draw()
            ui.window_surface.blit(ui.scene.current.surface, (0, 0))
            pygame.display.flip()

        def event(self, ev):
            pass

        def onQuit(self):
            pass
