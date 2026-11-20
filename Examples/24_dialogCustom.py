# The custom dialog returns the response associated with its selected button.
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Dialog Example")
        self.set_default_size(200, 100)
        self.set_border_width(30)
        button = Gtk.Button(label="Open a PopUp")
        button.connect("clicked", self.button_clicked)
        self.add(button)

    def button_clicked(self, widget):
        dialog = PopUp(self)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("You clicked the OK button")
        elif response == Gtk.ResponseType.CANCEL:
            print("You clicked the CANCEL button")
        dialog.destroy()


class PopUp(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(
            self,
            "PopUp Title",
            parent,
            Gtk.DialogFlags.MODAL,
            (
                "Custom cancel text",
                Gtk.ResponseType.CANCEL,
                Gtk.STOCK_OK,
                Gtk.ResponseType.OK,
            ),
        )
        self.set_default_size(200, 100)
        self.set_border_width(10)
        area = self.get_content_area()
        area.add(Gtk.Label("Wow that's so amazing, you can open a pop up."))
        self.show_all()


win = MainWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
