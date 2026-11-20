# The stack switcher selects which named child the stack displays.
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class StackWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Switcher")
        self.set_border_width(10)
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(box)
        main_area = Gtk.Stack()
        main_area.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        main_area.set_transition_duration(2000)
        check_button = Gtk.CheckButton("Do not fn check me")
        main_area.add_titled(check_button, "checkbox_name", "Check Box")
        label = Gtk.Label()
        label.set_markup("<big>OMG this text is huge!</big>")
        main_area.add_titled(label, "label_name", "Big Label")
        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(main_area)
        box.pack_start(stack_switcher, True, True, 0)
        box.pack_start(main_area, True, True, 0)


win = StackWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
