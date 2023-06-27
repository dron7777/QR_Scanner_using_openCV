import cv2
import webbrowser
import numpy as np
from pyzbar.pyzbar import decode
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import re

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

        img = cv2.imread(file_path)
        img = cv2.resize(img, (512, 512))

        for qrcode in decode(img):
            codedata = qrcode.data.decode("UTF-8")
            url_pattern = r'(https?://\S+)'
            match = re.search(url_pattern, codedata)
            if match:
                n = True
            else:
                n = False
            if n:
                webbrowser.open(codedata)
            else:
                print(codedata)

            points = np.array([qrcode.polygon], np.int32)
            points = points.reshape((-1, 1, 2))
            points2 = qrcode.rect

            cv2.polylines(img, [points], True, (0, 255, 0), 5)
            cv2.putText(img, codedata, (points2[0], points2[1] - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 255, 0), 2)

        cv2.imshow("QR Code", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        window.mainloop()
    else:
        print("No picture selected.")


choose_picture()
