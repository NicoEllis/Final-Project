import tkinter as tk
from tkinter import colorchooser

class DrawingApp:
    def initial_setup(self, root):
        self.root = root
        self.root.title("Drawing App")

        self.canvas = tk.Canvas(self.root, width = 400, height = 400, bg = "white")

        self.brush_color = "black"
        self.brush_size = 2

        self.setup_ui()

        bind ("", self.paint)

    def choose_color(self):
        self.brush_color = colorchooser.askcolor(title="Choose color")

    def change_brush_size(self, val):

    def paint(self,event):

def main():
    root
    app
    root

    if __name__ == "__main__":
        main()