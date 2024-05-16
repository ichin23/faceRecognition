import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import numpy as np


class Application():
    """Application interface control"""
    def __init__(self):
        self.last_img=None
        self.root = tk.Tk()
        self.root.geometry("500x450")
        self.root.title("Camera")

        self.menu = tk.Menu(self.root)

        self.actions_menu = tk.Menu(self.menu, tearoff=0)
        self.actions_menu.add_command(label="Manage Database", command= lambda: manageScreen())

        self.menu.add_cascade(menu=self.actions_menu, label="Actions")

        self.root.config(menu=self.menu)

        frame = tk.Frame(self.root)

        self.user_input = tk.StringVar(frame)

        self.video_frame=tk.Label(frame)
        self.video_frame.pack()

        self.b1=tk.Button(frame,text='Save Unknow',
                       height=2,width=10,command=self.save_unknow)
        self.b1.pack()
        frame.pack()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)


    def resize(self, img):
        width =  self.root.winfo_width()
        height =  self.root.winfo_height()
        img_x_size, img_y_size = img.size
        original_ratio = img_x_size / img_y_size

        if width/height > original_ratio:
            return img.resize((int(original_ratio*height), height))
        else:
            return img.resize((width, int(width/original_ratio)))

    def update(self, img):
        """Update the camera image
            :param -img: Image in array format
        """

        img1 = np.ascontiguousarray(img[:, :, ::-1])
        image = Image.fromarray(img1)
        image = self.resize(image)

        img = ImageTk.PhotoImage(image)
        self.video_frame.configure(image=img)
        self.video_frame.photo=img

    def save_unknow(self):
        """Create input frame"""
        f1 = tk.Tk()
        content = tk.LabelFrame(f1)

        l1 = tk.Label(content, text="Name")
        e1 = tk.Entry(content, textvariable=self.user_input)

        btn = tk.Button(content, text="Save", command=self.save_person)
        btn2 = tk.Button(content, text="Cancel", command=self.cancel_save)
        content.grid(row=0, column=0)

        l1.grid(row=0, column=0)
        e1.grid(row=0, column=1)
        btn.grid(column=0, row=1, columnspan=4)
        btn2.grid(column=2, row=1, columnspan=2)
        content.pack()
        f1.mainloop()

    def save_person(self):
        """Save the unknow person with the typed name"""
        #encoding =self.fr.get_encoding(self.last_img)
        name = self.user_input.get()

        #self.db.insert_person(name, encoding)
        #self.fr.get_names()
        self.user_input.set("")
        self.cancel_save()

    def cancel_save(self):
        """Close the input frame"""
        self.content.destroy()

    def on_closing(self):
        """Ask for close application"""
        self.running=False
        #self.video_capture.release()
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.quit()
            self.full_stop=True
        else:
            self.running=True
            self.video_capture.open(0)

def manage_screen():
	pass
