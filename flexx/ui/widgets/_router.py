from flexx import ui, app


class Router(app.Model):
    pass

class Route:
    pass

class IndexRoute(Route):
    pass

class Placeholder(ui.Widget):
    pass

class Link(ui.Widget):
    pass


if __name__ == '__main__':
    from flexx import app

    class MyApp(ui.Widget):
        def init(self):
            with ui.Router():
                pass

    m = app.App(MyApp)
    m.launch('xul')
    app.run()
