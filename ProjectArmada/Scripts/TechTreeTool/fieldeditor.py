"""
Blah.
"""

import tkinter as tk

class FieldEditor:
    """
    Blah
    """

    root = None

    def __init__(self, node):
        FieldEditor.root = tk.Tk()
        FieldEditor.root.protocol("WM_DELETE_WINDOW", on_quit)
        self.create_fields(FieldEditor.root, node)

    def create_fields(self, root, node):
        """
        TODO
        """
        # Name
        tk.Label(root, text="Name:").grid(row=0)
        e1 = tk.Entry(root, width=30)
        #e1.insert(10, node.name)
        e1.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W + tk.E)

        # Type
        tk.Label(root, text="Type:").grid(row=1)
        e2 = tk.Entry(root, width=30)
        #e1.insert(10, node.name)
        e2.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W + tk.E)

        # Description
        tk.Label(root, text="Description:").grid(row=2)
        e3 = tk.Text(root, height=10, width=30)
        e3.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        # Flavor Text
        tk.Label(root, text="Flavor Text:").grid(row=3)
        e3 = tk.Text(root, height=5, width=30)
        e3.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

        # Icon
        tk.Label(root, text="Icon:").grid(row=0, column=2)
        e3 = tk.Entry(root)
        e3.grid(row=0, column=4, padx=5, pady=5, sticky=tk.W)

        # Modifiers

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
