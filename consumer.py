import tkinter as tk

from queue import Queue
from boxshape import BoxShape


def rgb_to_hex(r: int, g: int, b: int):
    return f"#{r:02x}{g:02x}{b:02x}"


def update_overlay(queue: Queue, canvas, root):

    if not queue.empty():

        attack_speed, (r, g, b) = queue.get()
        canvas.configure(bg=rgb_to_hex(r, g, b))
        canvas.delete("attack_speed_text")
        canvas.create_text(100, 36, text=attack_speed, fill="black", font=("Arial", 36), tags="attack_speed_text")
        
    root.after(100, update_overlay, queue, canvas, root)


def consumer(queue: Queue, boxshape: BoxShape):
    color_box_width = 200
    color_box_height = 100
    
    root = tk.Tk()
    root.overrideredirect(True)
    root.attributes("-alpha", 0.5)
    root.geometry(f"{boxshape.width}x{boxshape.height}+{boxshape.x}+{boxshape.y}")
    root.attributes("-topmost", True)
    root.attributes("-transparentcolor", "white")

    canvas = tk.Canvas(root, width=color_box_width, height=color_box_height, highlightthickness=0)
    canvas.pack()

    update_overlay(queue, canvas, root)
    root.mainloop()