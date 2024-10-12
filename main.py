import tkinter as tk
from PIL import Image, ImageTk
from screeninfo import get_monitors
import random

class DVDPlayer:
    def __init__(self, root, image_path, width, height):
        self.root = root
        self.root.title("DVD Idle Player")
        self.root.geometry(f"{width}x{height}")
        self.root.state('zoomed')
        self.root.configure(bg='white')
        self.root.overrideredirect(True)  # Remove the title bar
        self.root.wm_attributes('-transparentcolor', 'white')  # Set transparent color
        self.root.wm_attributes('-topmost', True)  # Keep the window on top

        self.canvas = tk.Canvas(root, width=width, height=height, bg='white', highlightthickness=0)
        self.canvas.pack()

        self.image = Image.open(image_path)
        self.photo = ImageTk.PhotoImage(master=self.canvas, image=self.image)

        # Generate random starting coordinates
        start_x = random.randint(0, width - self.image.width)
        start_y = random.randint(0, height - self.image.height)

        self.image_id = self.canvas.create_image(start_x, start_y, anchor='nw', image=self.photo)

        self.dx = 2
        self.dy = 2

        self.move_image()

    def move_image(self):
        coords = self.canvas.coords(self.image_id)
        # Adjust the boundary conditions based on image size
        if coords[0] < 0 or coords[0] + self.image.width >= self.root.winfo_width():
            self.dx = -self.dx
        if coords[1] < 0 or coords[1] + self.image.height >= self.root.winfo_height():
            self.dy = -self.dy

        # Move the image
        self.canvas.move(self.image_id, self.dx, self.dy)
        self.root.after(10, self.move_image)

def main():
    for m in get_monitors():
        print(str(m))
        if m.is_primary:
            width = m.width
            height = m.height
    
    root = tk.Tk()
    app = DVDPlayer(root, "image.png", width, height)
    root.mainloop()


if __name__ == "__main__":
    main()