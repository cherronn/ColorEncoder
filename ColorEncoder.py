import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class LithophaneConverterGUI:
    def __init__(self, master):
        self.master = master
        master.title("Color Encoder with Histogram")

        self.image_path = None
        self.original_image = None
        self.height_map_image = None
        self.histogram_figure = None  

        self.create_widgets()

    def create_widgets(self):
        self.load_button = tk.Button(self.master, text="Load Image", command=self.load_image)
        self.load_button.pack()

        self.canvas_original = tk.Canvas(self.master, width=400, height=400)
        self.canvas_original.pack(side=tk.LEFT)

        self.canvas_height_map = tk.Canvas(self.master, width=400, height=400)
        self.canvas_height_map.pack(side=tk.RIGHT)

        self.save_button = tk.Button(self.master, text="Save Height Map Image", command=self.save_image)
        self.save_button.pack()

        self.histogram_frame = tk.Frame(self.master)
        self.histogram_frame.pack()

        self.save_histogram_button = tk.Button(self.master, text="Save Histogram", command=self.save_histogram)
        self.save_histogram_button.pack()

    def load_image(self):
        self.image_path = filedialog.askopenfilename()
        if self.image_path:
            self.original_image = Image.open(self.image_path).convert("RGB")
            self.display_image(self.original_image, self.canvas_original)
            self.convert_to_height_map()

    def convert_to_height_map(self):
        if self.original_image:
            rgb_array = np.array(self.original_image)
        
            # Opt tested contibutions
            height_map = (
                0.7 * rgb_array[:, :, 0] +   # Red contribution
                0.2 * rgb_array[:, :, 1] +   # Green contribution
                0.0 * rgb_array[:, :, 2]     # Blue contribution 
            ).astype(np.uint8)

            height_map_normalized = ((height_map - height_map.min()) / (height_map.max() - height_map.min()) * 255).astype(np.uint8)

            self.show_histogram(height_map_normalized)

            self.height_map_image = Image.fromarray(height_map_normalized, mode='L')
            self.display_image(self.height_map_image, self.canvas_height_map)

    def show_histogram(self, data):
        for widget in self.histogram_frame.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots(figsize=(5, 4))
        ax.hist(data.ravel(), bins=256, color='blue', alpha=0.7)
        ax.set_title("Linearized Height Map")
        ax.set_xlabel("Pixel Value")
        ax.set_ylabel("Frequency", fontsize=12) 
        ax.yaxis.set_label_position("left")
        ax.yaxis.tick_left()
        ax.grid(True)

        self.histogram_figure = fig

        canvas = FigureCanvasTkAgg(fig, master=self.histogram_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def save_histogram(self):
        if self.histogram_figure:
            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
            if save_path:
                self.histogram_figure.savefig(save_path)

    def save_image(self):
        if self.height_map_image:
            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
            if save_path:
                self.height_map_image.save(save_path)

    def display_image(self, image, canvas):
        img_width, img_height = image.size
        canvas_width, canvas_height = canvas.winfo_width(), canvas.winfo_height()
        scale = min(canvas_width / img_width, canvas_height / img_height)
        new_width, new_height = int(img_width * scale), int(img_height * scale)
        resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(resized_image)
        canvas.delete("all")
        canvas.create_image(canvas_width // 2, canvas_height // 2, image=photo, anchor=tk.CENTER)
        canvas.image = photo

if __name__ == "__main__":
    root = tk.Tk()
    gui = LithophaneConverterGUI(root)
    root.mainloop()
