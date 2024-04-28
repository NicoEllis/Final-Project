import tkinter as tk
from tkinter import colorchooser

class DrawingApp:
    def initial_setup(self, root):
        self.root = root
        self.root.title("Drawing App")
        
        self.canvas = tk.Canvas(self.root, width= 400, height= 400, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        self.brush_color = "black"
        self.brush_size = 2
        
        self.setup_ui()
        
        self.canvas.bind("<B1-Motion>", self.paint)
        
    def setup_ui(self):
        color_frame = tk.Frame(self.root)
        color_frame.pack(side=tk.LEFT, padx= 5, pady= 5)
        
        self.color_label = tk.Label(color_frame, text="Color:")
        self.color_label.pack(pady=(0,5))
        
        self.color_btn = tk.Button(color_frame, text="Choose Color", command=self.choose_color)
        self.color_btn.pack()
        
        brush_frame = tk.Frame(self.root)
        brush_frame.pack(side=tk.LEFT, padx= 5, pady= 5)
        
        self.brush_label = tk.Label(brush_frame, text="Brush Size:")
        self.brush_label.pack(pady=(0,5))
        
        self.brush_slider = tk.Scale(brush_frame, from_= 1, to= 10, orient=tk.HORIZONTAL, command=self.change_brush_size)
        self.brush_slider.set(self.brush_size)
        self.brush_slider.pack()
        
    def choose_color(self):
        _, self.brush_color = colorchooser.askcolor(title="Choose color")
        
    def change_brush_size(self, val):
        self.brush_size = int(val)
        
    def paint(self, event):
        x1, y1 = (event.x - self.brush_size), (event.y - self.brush_size)
        x2, y2 = (event.x + self.brush_size), (event.y + self.brush_size)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.brush_color, outline=self.brush_color)

def main():
    root = tk.Tk()
    app = DrawingApp()
    app.initial_setup(root)
    root.mainloop()

if __name__ == "__main__":
    main()