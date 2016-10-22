import seilriss.pygameui as ui

from .base import BaseScene
from seilriss.ui import consts


class CountDown(BaseScene):

    COLOR_START = (255, 0, 0)
    COLOR_END = (0, 102, 0)
    STEPS = 3 * 60

    def __init__(self):
        super(CountDown, self).__init__()
        self.countDown = self.STEPS
        self.time = ui.Label(consts.SCREEN_SIZE, '', halign=ui.CENTER)
        self.add_child(self.time)
        self.currentColor = self.COLOR_START

    def layout(self):
        super(CountDown, self).layout()
        self.time.text_shadow_offset = None
        self.time.font = ui.resource.get_font(100)
        self.time.background_color = self.currentColor
        self.time.text_color = (0, 0, 0)
        self._setTimer()

    def mouse_up(self, a, pt):
        ui.scene.pop()

    def timer(self, ev):
        if self.countDown <= 0:
            return
        self.countDown -= 1
        if self.countDown <= 0:
            self.currentColor = self.COLOR_END
            self.time.text_color = (255, 255, 255)
            self.time.text = 'Fertig'
        else:
            self._setTimer()
        self.time.background_color = self.currentColor

    def _setTimer(self):
        text = '%02i:%02i' % (self.countDown // 60, self.countDown % 60)
        self.time.text = text
