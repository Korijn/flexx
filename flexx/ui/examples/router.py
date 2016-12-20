# doc-export: Router
"""
An interactive router demo.
"""

from flexx import app, ui


class Foo(ui.Widget):
    pass


class MyApp(ui.Widget):
    def init(self):
        with ui.Router():
            with ui.Route(path="/", widget=Foo):
                ui.IndexRoute(widget=Foo)
                ui.Route(path="about", widget=Foo)
                with ui.Route(path="tasks", widget=Foo):
                    ui.Route(path="/:task-id", widget=Foo)
                    ui.Route(path="contact", widget=Foo)


if __name__ == '__main__':
    m = app.App(MyApp)
    m.launch('chrome')
    app.run()
