"""
Blah.
"""

import tkinter as tk
import tkinter.scrolledtext

MODIFIER_OPTIONS = [
    "Health",
    "Defense",
    "Mobility",
    "Speed",
    "Damage",
    "Accuracy",
    "Fire Rate",
    "Range"
]

class FieldEditor:
    """
    Blah
    """

    root = None

    def __init__(self, node):
        FieldEditor.root = tk.Tk()
        FieldEditor.root.protocol("WM_DELETE_WINDOW", on_quit)
        self.entries = []
        self.modifiers = []
        self.modifier_vals = []
        self.modifier_idx = 0
        self.modules = []
        self.create_fields(FieldEditor.root, node)

    def create_fields(self, root, node):
        """
        TODO
        -------------------------------
        | Name: | ____ | Icon: | ____ |
        |--------------|--------------|
        | Type: | ____ | Modifiers:   |
        |--------------|--------------|
        | Desc: | ____ |  Mdf frame   |
        |--------------|--------------|
        |       | ____ |  Add  | remv |
        |--------------|--------------|
        | Flvr: | ____ | Modules:     |
        |--------------|--------------|
        |       | ____ |  Mdl frame   |
        |--------------|--------------|
        |  save | cncl |  Add  | remv |
        -------------------------------

        TODO: Change frames to canvas and add a scroll bar
        """

        # Name
        tk.Label(root, text="Name:").grid(row=0)
        e1 = tk.Entry(root, width=20)
        #e1.insert(10, node.name)w
        e1.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W + tk.E)
        self.entries.append(e1)

        # Type
        tk.Label(root, text="Type:").grid(row=1)
        e2 = tk.Entry(root, width=20)
        #e1.insert(10, node.name)
        e2.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W + tk.E)
        self.entries.append(e2)

        # Description
        tk.Label(root, text="Description:").grid(row=2, sticky=tk.N)
        e3 = tk.scrolledtext.ScrolledText(root, width=25, height=10)
        e3.grid(row=2, column=1, padx=5, pady=5, rowspan=2)
        self.entries.append(e3)

        # Flavor Text
        tk.Label(root, text="Flavor Text:").grid(row=4, sticky=tk.N)
        e4 = tk.scrolledtext.ScrolledText(root, width=25, height=10)
        e4.grid(row=4, column=1, padx=5, pady=5, rowspan=2)
        self.entries.append(e4)

        # Icon
        tk.Label(root, text="Icon:").grid(row=0, column=2)
        e5 = tk.Entry(root)
        e5.grid(row=0, column=3, padx=5, pady=5, sticky=tk.W)
        self.entries.append(e5)

        # Modifiers
        tk.Label(root, text="Modifiers:").grid(row=1, column=2, columnspan=2)
        modifier_frame = tk.Frame(root)
        modifier_frame.grid(row=2, column=2, columnspan=2, sticky=tk.N)

        def add_modifier(frame):
            mod_string = tk.StringVar(frame)
            mod_string.set(MODIFIER_OPTIONS[0])
            mod_dropdown = tk.OptionMenu(modifier_frame,
                                         mod_string,
                                         *MODIFIER_OPTIONS
                                         )
            mod_dropdown.grid(row=self.modifier_idx, sticky=tk.N + tk.W)
            self.modifiers.append(mod_string)

            e = tk.Entry(frame)
            e.grid(row=self.modifier_idx, column=1)
            self.modifier_vals.append(e)

            self.modifier_idx += 1


        def remove_modifier(frame):
            if self.modifier_idx > 0:
                for widget in frame.grid_slaves()[-2:]:
                    widget.grid_forget()
                del self.modifiers[-1]
                del self.modifier_vals[-1]
                self.modifier_idx -= 1

        b1 = tk.Button(root,
                       text="Add",
                       command=lambda: add_modifier(modifier_frame)
                       )
        b1.grid(row=3, column=2, sticky=tk.N + tk.E)

        b2 = tk.Button(root,
                       text="Remove",
                       command=lambda: remove_modifier(modifier_frame)
                       )
        b2.grid(row=3, column=3, sticky=tk.N + tk.W)

        # Modules
        tk.Label(root, text="Modules:").grid(row=4, column=2, columnspan=2)
        module_frame = tk.Frame(root)
        module_frame.grid(row=5, column=2, columnspan=2, sticky=tk.N)

        def add_module(frame):
            pass

        def remove_module(frame):
            pass

        b3 = tk.Button(root,
                       text="Add",
                       command=lambda: add_module(module_frame)
                       )
        b3.grid(row=6, column=2, sticky=tk.N + tk.E)

        b4 = tk.Button(root,
                       text="Remove",
                       command=lambda: remove_module(module_frame)
                       )
        b4.grid(row=6, column=3, sticky=tk.N + tk.W)

    def store_values(self):
        """
        TODO
        """
        pass

    def update(self):
        """
        TODO
        """
        if FieldEditor.root:
            FieldEditor.root.update_idletasks()
            FieldEditor.root.update()


def on_quit():
    """
    This method is here to intercept the Tk.destroy and set
    root to None
    """
    FieldEditor.root.destroy()
    FieldEditor.root = None
