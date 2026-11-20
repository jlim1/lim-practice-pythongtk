# The middle button is packed into the expanding center area.
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

button = Gtk.Button()


def create_middle(area):
    button.set_label("Middle Area")
    area.pack_start(button, True, True, 0)
