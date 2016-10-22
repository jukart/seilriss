import seilriss.pygameui as ui
from seilriss.ui import consts

from .base import BaseScene
from .countdown import CountDown


class Main(BaseScene):

    def __init__(self):
        super(Main, self).__init__()
        top = 0
        self.back = ui.Label(consts.SCREEN_SIZE, '', halign=ui.CENTER)
        self.add_child(self.back)

        rect = consts.SCREEN_SIZE.copy()
        rect.height = rect.height / 3
        rect.bottom = rect.height
        self.title = ui.Label(rect, '', halign=ui.CENTER)
        self.add_child(self.title)
        top += rect.height

        rect = consts.SCREEN_SIZE.copy()
        rect.height = rect.height / 6
        rect.top = top
        self.info1 = ui.Label(rect, '', halign=ui.CENTER)
        self.add_child(self.info1)
        top += rect.height

        rect = consts.SCREEN_SIZE.copy()
        rect.height = rect.height / 6
        rect.top = top
        self.info2 = ui.Label(rect, '', halign=ui.CENTER)
        self.add_child(self.info2)

    def layout(self):
        super(Main, self).layout()
        self._setLabel(self.back, '')
        self._setLabel(self.title, 'HGSV')
        self._setLabel(self.info1, 'Count Down')
        self._setLabel(self.info2, 'Starten')

    def _setLabel(self, label, text):
        label.text_shadow_offset = None
        label.font = ui.resource.get_font(40)
        label.background_color = (0, 0, 0)
        label.text_color = (255, 255, 255)
        label.text = text

    def mouse_up(self, a, pt):
        ui.scene.push(CountDown())
