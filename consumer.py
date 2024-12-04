from queue import Queue
import tkinter as tk


def rgb_to_hex(r: int, g: int, b: int):
    return f"#{r:02x}{g:02x}{b:02x}"


def update_overlay(queue: Queue, canvas, root):

    if not queue.empty():

        attack_speed, (r, g, b) = queue.get()
        canvas.configure(bg=rgb_to_hex(r, g, b))
        canvas.delete("attack_speed_text")
        canvas.create_text(100, 50, text=attack_speed, fill="white", font=("Arial", 24), tags="attack_speed_text")
        
    root.after(100, update_overlay, queue, canvas, root)


def consumer(queue: Queue):
    
    root = tk.Tk()
    root.overrideredirect(True)
    root.attributes("-alpha", 0.5)
    root.geometry("200x100+1500+1000")
    root.attributes("-topmost", True)

    canvas = tk.Canvas(root, width=200, height=100, highlightthickness=0)
    canvas.pack()

    update_overlay(queue, canvas, root)
    root.mainloop()