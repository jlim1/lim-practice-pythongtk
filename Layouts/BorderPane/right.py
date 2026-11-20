# The right area packs a button into the supplied container.
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

button = Gtk.Button()


def create_right(area):
    button.set_label("Right Area")
    area.pack_start(button, True, True, 0)
