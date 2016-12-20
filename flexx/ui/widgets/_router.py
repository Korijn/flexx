from ... import app
from . import Widget, Anchor


class Router(app.Model):
    """Does pattern matching on paths to manage a hierarchy of widgets."""

    def init(self):
        self.routes = {}
        self.route_context_stack = [self]

    def register(self, route):
        parent = self.route_context_stack[-1]
        parent.routes[route.path] = route

    def push_route_context(self, route):
        self.route_context_stack.append(route)

    def pop_route_context(self):
        self.route_context_stack.pop()

    def register_placeholder(self, placeholder):
        # stub method
        pass


class Route:
    """
    Links a path pattern to a widget class. Should be used as a context manager for convenient declaration of
    the widget hierarchy.
    """

    def __init__(self, path, widget):
        self.router = app.get_active_model()
        if not isinstance(self.router, Router):
            raise ValueError("All Routes must be instantiated in the context of a Router.")

        self.path = path
        self.widget = widget
        self.routes = {}

        self.router.register(self)

    def __enter__(self):
        self.router.push_route_context(self)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.router.pop_route_context()


class IndexRoute(Route):
    """When a Router has no matching paths in its Routes, an IndexRoute is its fallback; it is the default Route."""

    def __init__(self, widget):
        super().__init__(None, widget)


class Placeholder(Widget):
    """The Placeholder serves as an entry-point for the Router to insert its widgets into the children property."""

    def init(self):
        # this happens at runtime, so the Router will have to put itself on the active model stack when it instantiates
        # the widget holding Placeholder
        self.router_stack = tuple(filter(lambda m: isinstance(m, Router), app.get_active_models()))
        if not self.router_stack:
            raise ValueError("All Placeholders must be instantiated in the context of a Router.")

        self.router = self.router_stack[-1]

        self.router.register_placeholder(self)


class Link(Anchor):
    """A specialized Anchor tag that doesn't interact with the URL/browser directly but rather with the Router."""
    def init(self):
        # this happens at runtime, so the Router will have to put itself on the active model stack when it instantiates
        # the widget holding Link
        self.router_stack = tuple(filter(lambda m: isinstance(m, Router), app.get_active_models()))
        if not self.router_stack:
            raise ValueError("All Links must be instantiated in the context of a Router.")

        self.router = self.router_stack[-1]


