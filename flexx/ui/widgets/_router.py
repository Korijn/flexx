from flexx import ui, app


class Router(app.Model):
    def init(self):
        self.routes = {}
        self._route_context_stack = [self]

    def register(self, route):
        parent = self._route_context_stack[-1]
        parent.routes[route.path] = route

    def push_route_context(self, route):
        self._route_context_stack.append(route)

    def pop_route_context(self):
        self._route_context_stack.pop()


class Route:
    def __init__(self, path, widget):
        self.router = app.get_active_model()
        if not isinstance(self.router, Router):
            raise ValueError("All Route objects must be instantiated in the context of a Router.")

        self.path = path
        self.widget = widget
        self.routes = {}

        self.router.register(self)

    def __enter__(self):
        self.router.push_route_context(self)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.router.pop_route_context()


class IndexRoute(Route):
    def __init__(self, widget):
        super().__init__(None, widget)


class Placeholder(ui.Widget):
    pass


class Link(ui.Widget):
    pass


class Foo(ui.Widget):
    pass


if __name__ == '__main__':
    from flexx import app

    class MyApp(ui.Widget):
        def init(self):
            with Router():
                with Route(path="/", widget=Foo):
                    IndexRoute(widget=Foo)
                    Route(path="about", widget=Foo)
                    with Route(path="tasks", widget=Foo):
                        Route(path="/:task-id", widget=Foo)
                    Route(path="contact", widget=Foo)


    m = app.App(MyApp)
    m.launch('xul')
    app.run()
