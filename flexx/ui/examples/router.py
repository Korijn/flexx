# doc-export: Router
"""
An interactive router demo.
"""

from flexx import app, ui


class RedWidget(ui.Widget):
    def init(self):
        self.style = 'background:#f00'
        self.title = 'red'


class GreenWidget(ui.Widget):
    def init(self):
        self.style = 'background:#0f0'
        self.title = 'green'


class Router(ui.Widget):
    def init(self):
        pass


class Main(ui.Widget):
    def init(self):
        with Router() as self.router:
            pass

if __name__ == '__main__':
    m = app.launch(Main, 'xul')
    app.run()
