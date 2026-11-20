# The toolbar packs its buttons horizontally and connects their click handlers.
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

top_button = Gtk.Button()
button_1 = Gtk.Button(label="One")
button_2 = Gtk.Button(label="Two")
button_3 = Gtk.Button(label="Three")


def create_top(area):
    global top_button
    top_button = Gtk.Button(label="This is from toolbar")
    top_button.connect("clicked", button_clicked)
    toolbar = Gtk.Box()
    toolbar.pack_start(top_button, False, False, 0)
    toolbar.pack_start(button_1, False, False, 0)
    toolbar.pack_start(button_2, False, False, 0)
    toolbar.pack_start(button_3, False, False, 0)
    area.pack_start(toolbar, True, True, 0)


def button_clicked(self):
    print("Gametime")


def change_button_text(text):
    top_button.set_label(text)
