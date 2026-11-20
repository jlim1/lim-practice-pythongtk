# The file chooser returns the selected path when its response is accepted.
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class FileChooserWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="")
        self.set_border_width(30)
        layout = Gtk.Box(spacing=6)
        self.add(layout)
        button = Gtk.Button(label="Choose File")
        button.connect("clicked", self.on_file_clicked)
        layout.add(button)

    def on_file_clicked(self, widget):
        dialog = Gtk.FileChooserDialog(
            "Select a file Hoss",
            self,
            Gtk.FileChooserAction.OPEN,
            (
                Gtk.STOCK_CANCEL,
                Gtk.ResponseType.CANCEL,
                Gtk.STOCK_OPEN,
                Gtk.ResponseType.OK,
            ),
        )
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Open button clicked")
            print("File selected: " + dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel button clicked")
        dialog.destroy()


window = FileChooserWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
