# A submenu groups commands beneath the menu bar item.
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

menu_bar = Gtk.MenuBar()


def create_main_menu(area):
    file_menu = Gtk.Menu()
    menu_item_file = Gtk.MenuItem("File")
    menu_item_file.set_submenu(file_menu)
    menu_item_exit = Gtk.MenuItem("Quit Now!")
    menu_item_exit.connect("activate", Gtk.main_quit)
    file_menu.append(menu_item_exit)
    menu_bar.append(menu_item_file)
    area.pack_start(menu_bar, False, False, 0)
