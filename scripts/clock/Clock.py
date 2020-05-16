import Display


class Clock(object):
    def __init__(self):
        super().__init()

    @property
    def display(self):
        try:
            return self._display
        except AttributeError:
            self._display = Display()
            self._display.start()
            return self._display

    @display.setter
    def display(self, display):
        try:
            self._display.stop()
        except AttributeError:
            pass
        self._display = display
