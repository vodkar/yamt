from prompt_toolkit.application import get_app
from prompt_toolkit.filters import Condition


class HasFocusMixin:
    @property
    def has_focus(self):
        return Condition(lambda: get_app().layout.has_focus(self))

    def focus(self):
        get_app().layout.focus(self)
