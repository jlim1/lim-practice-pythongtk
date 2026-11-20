# The tree view maps model fields onto individual display columns.
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

people = [
    ("Demo A", 31, "Designer"),
    ("Demo B", 45, "Teacher"),
    ("Demo C", 26, "Baker"),
]


class TreeViewFilterWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="People Finder")
        layout = Gtk.Box()
        self.add(layout)
        people_list_store = Gtk.ListStore(str, int, str)
        for item in people:
            people_list_store.append(list(item))
        for row in people_list_store:
            print(row[:])
            print(row[2])
        people_tree_view = Gtk.TreeView(people_list_store)
        for i, col_title in enumerate(["Name", "Age", "Profession"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(col_title, renderer, text=i)
            people_tree_view.append_column(column)
        layout.pack_start(people_tree_view, True, True, 0)


window = TreeViewFilterWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
