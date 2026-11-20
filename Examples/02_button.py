# The clicked signal connects the button to a Python method.
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")
        self.button = Gtk.Button(label="Click Here")
        self.button.connect("clicked", self.button_clicked)
        self.add(self.button)

    def button_clicked(self, widget):
        print("Gametime")


window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
