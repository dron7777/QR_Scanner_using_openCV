import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


def choose_picture():
    root = tk.Tk()
    root.withdraw()

    # Open file dialog to select a picture
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
    print(file_path)
    if file_path:
        # Open the selected image using PIL
        image = Image.open(file_path)

        # Display the image using Tkinter
        window = tk.Toplevel()
        window.title("Selected Picture")
        window.geometry("500x500")

        # Resize the image to fit within the window
        image.thumbnail((400, 400))

        # Convert the image to Tkinter-compatible format
        tk_image = ImageTk.PhotoImage(image)

        # Create a label and display the image
        label = tk.Label(window, image=tk_image)
        label.pack()

        window.mainloop()
    else:
        print("No picture selected.")

choose_picture()
