"""

Simple example:

.. UIExample:: 50

    anchor = ui.Anchor(text='Click me', href='https://github.com')

Interactive example:

.. UIExample:: 50
    from flexx import ui

    class Example(ui.Widget):

        def init(self):
            self.anchor = ui.Anchor(flex=1, text='Click here', href='https://github.com')

"""
from ... import event
from . import Widget
from ...pyscript.stubs import window


class Anchor(Widget):
    """ Anchor widget.
    """

    class Both:
        @event.prop
        def text(self, v):
            """ The text in the anchor.
            """
            return str(v)

        @event.prop
        def href(self, v):
            """ The href of the anchor.
            """
            return str(v)

        @event.prop
        def name(self, v):
            """ The href of the anchor.
            """
            return str(v)

    class JS:
        def _init_phosphor_and_node(self):
            self.phosphor = self._create_phosphor_widget('div')
            self.node = window.document.createElement('a')
            self.phosphor.node.appendChild(self.node)

        @event.connect('text')
        def _text_changed(self, *events):
            self.node.innerText = self.text
            self._check_real_size(True)

        @event.connect('href')
        def _href_changed(self, *events):
            self.node.href = self.href

        @event.connect('name')
        def _name_changed(self, *events):
            self.node.name = self.name
