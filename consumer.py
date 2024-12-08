from queue import Queue
import tkinter as tk
import time

from boxshape import BoxShape


def rgb_to_hex(r: int, g: int, b: int):
    return f"#{r:02x}{g:02x}{b:02x}"


def update_overlay(queue: Queue, canvas, root):

    start_time = time.time()

    if not queue.empty():

        # Get the canvas dimensions
        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()

        # Dynamically calculate font size
        font_size = int(canvas_height * 0.85)
        font_size = max(16, font_size) # set minimum fontsize

        attack_speed, (r, g, b) = queue.get()
        canvas.configure(bg=rgb_to_hex(r, g, b))
        canvas.delete("attack_speed_text")
        canvas.create_text(
            canvas_width // 2, 
            canvas_height // 2, 
            text=attack_speed, 
            fill="black", 
            font=("Arial", font_size), 
            tags="attack_speed_text"
        )
    
    else:
        # Probably alt-tabbed. Be nice to the computer
        time.sleep(1)

    elapsed = (time.time() - start_time) * 1000  # ms
    remaining_time = max(0, 16 - elapsed)
        
    # 60 fps
    root.after(int(remaining_time), update_overlay, queue, canvas, root)


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