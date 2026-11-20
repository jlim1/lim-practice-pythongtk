# Python GTK 3 practice

Standalone desktop examples cover windows, buttons, layouts, tabs and progress indicators. Use Python 3 with PyGObject, GTK **3**, its introspection data, and a working graphical display. On Debian/Ubuntu these bindings are available as `python3-gi` and `gir1.2-gtk-3.0`; use the system Python that can import `gi`.

From this directory:

```text
python3 Examples/02_button.py
```

Click **Click Here**: the terminal should print `Gametime`. Close the window to exit. For a timed progress indicator, run `python3 Examples/15_progressBar.py`. Examples 08 and 09 request icons from the installed desktop theme; an icon may be blank on some systems. No icon files are distributed here.

All 28 numbered examples, both starter scripts, `Project`, and `Layouts/BorderPane` are included. Run `python3 Layouts/BorderPane/main.py` to try the multi-file layout; leave its sibling modules together. The project buttons are UI demonstrations, not a working scanner. The people tables use synthetic rows; the entry demo does not print credentials. Lesson 26 prints a selected path locally; use a sample file. Some examples rely on installed icon themes or link to an external site. All modules passed syntax checks, but windows were not run: GTK 3 introspection data was unavailable.
