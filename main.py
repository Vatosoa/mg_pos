import tkinter as tk
from tkinter import ttk
from gui.app_interface import *

def main():
    root = tk.Tk()
    root.title("Malagasy : POS Tagger")
    create_gui(root)
    root.mainloop()

if __name__ == "__main__":
    main()
