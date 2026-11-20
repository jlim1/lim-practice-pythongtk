# The window embeds the custom input area.
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from top import TopArea


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Boxes are Awesome")
        self.add(TopArea())


window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
