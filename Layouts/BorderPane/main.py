# Horizontal and vertical boxes divide the window into the toolbar, content, and status areas.
from main_menu import *
from toolbar import *
from left import *
from middle import *
from right import *
from bottom import *

window = Gtk.Window(title="Title")
window.connect("delete-event", Gtk.main_quit)
layout = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
window.add(layout)
main_menu_area = Gtk.Box()
toolbar_area = Gtk.Box()
main_area = Gtk.Box()
bottom_area = Gtk.Box()
left_main = Gtk.Box()
middle_main = Gtk.Box()
right_main = Gtk.Box()
main_area.pack_start(left_main, False, False, 0)
main_area.pack_start(middle_main, True, True, 0)
main_area.pack_start(right_main, True, True, 0)
layout.pack_start(main_menu_area, False, False, 0)
layout.pack_start(toolbar_area, False, False, 0)
layout.pack_start(main_area, True, True, 0)
layout.pack_start(bottom_area, False, False, 0)
create_main_menu(main_menu_area)
create_top(toolbar_area)
create_left(left_main)
create_middle(middle_main)
create_right(right_main)
create_bottom(bottom_area)
window.show_all()
Gtk.main()
