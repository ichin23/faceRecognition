import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import numpy as np


class Application():
    """Application interface control"""
    def __init__(self, db, fr, video_capture):
        self.db=db
        self.fr=fr
        self.last_img=None
        self.running=True
        self.full_stop=False
        self.video_capture = video_capture
        self.root = tk.Tk()
        self.root.title("Camera")

        self.user_input = tk.StringVar(self.root)
        self.f1=tk.LabelFrame(self.root)
        self.f1.pack()
        self.l1=tk.Label(self.f1,bg='red')
        self.l1.grid(row=0, column=0, columnspan=5, rowspan=4)
        self.b1=tk.Button(self.f1,bg='green',fg='white',activebackground='white',
                       activeforeground='green',text='Save Unknow',relief=tk.RIDGE,
                       height=5,width=10,command=self.save_unknow)
        self.b1.grid(row=0, column=6)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    def update(self, img):
        """Update the camera image
            :param -img: Image in array format
        """
       
        self.last_img=img
        img1 = np.ascontiguousarray(img[:, :, ::-1])
        img = ImageTk.PhotoImage(Image.fromarray(img1))
        self.l1['image']=img
        self.root.update()

    def save_unknow(self):
        """Create input frame"""
        self.content = tk.LabelFrame(self.f1)

        l1 = tk.Label(self.content, text="Name")
        e1 = tk.Entry(self.content, textvariable=self.user_input)

        btn = tk.Button(self.content, text="Save", command=self.save_person)
        btn2 = tk.Button(self.content, text="Cancel", command=self.cancel_save)
        self.content.grid(row=0, column=0)

        l1.grid(row=0, column=0)
        e1.grid(row=0, column=1)
        btn.grid(column=0, row=1, columnspan=4)
        btn2.grid(column=2, row=1, columnspan=2)
        self.content.grid(column=6, row=1, columnspan=4, rowspan=2)

    def save_person(self):
        """Save the unknow person with the typed name"""
        encoding =self.fr.get_encoding(self.last_img)
        name = self.user_input.get()

        self.db.insert_person(name, encoding)
        self.fr.get_names()
        self.cancel_save()

    def cancel_save(self):
        """Close the input frame"""
        self.content.destroy()

    def on_closing(self):
        """Ask for close application"""
        self.running=False
        self.video_capture.release()
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()
            self.full_stop=True
        else:
            self.running=True
            self.video_capture.open(0)
