# The header bar holds the window title and action buttons.
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio


class HeaderBarWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="")
        self.set_border_width(10)
        self.set_default_size(500, 400)
        header_bar = Gtk.HeaderBar()
        header_bar.set_show_close_button(True)
        header_bar.props.title = "Rippin Music Player"
        self.set_titlebar(header_bar)
        audio_button = Gtk.Button()
        cd_icon = Gio.ThemedIcon(name="gnome-dev-cdrom-audio")
        image = Gtk.Image.new_from_gicon(cd_icon, Gtk.IconSize.BUTTON)
        audio_button.add(image)
        header_bar.pack_end(audio_button)
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class(box.get_style_context(), "linked")
        left_arrow = Gtk.Button()
        left_arrow.add(Gtk.Arrow(Gtk.ArrowType.LEFT, Gtk.ShadowType.NONE))
        box.add(left_arrow)
        right_arrow = Gtk.Button()
        right_arrow.add(Gtk.Arrow(Gtk.ArrowType.RIGHT, Gtk.ShadowType.NONE))
        box.add(right_arrow)
        header_bar.pack_start(box)
        self.add(Gtk.TextView())


window = HeaderBarWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
