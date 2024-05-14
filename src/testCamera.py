from tkinter import *
from PIL import Image, ImageTk
import cv2
import numpy as np


class Application():
	def __init__(self):
		self.root = Tk()
		self.root.title("Camera")

		self.f1=LabelFrame(self.root,bg='red')
		self.f1.pack()
		
		self.l1=Label(self.root,bg='red')
		self.l1.pack()
		
		self.b1=Button(self.root,
			text='Save Person', height=5, width=20,
			command=self.savePerson)
		self.b1.pack(side=LEFT,padx=60,pady=5)
		
	def savePerson(self):
		self.form = Tk()
		self.form.title("Add person")
		
		content = Frame(self.form)
		
		
		l1 = Label(content, text="Name")
		e1 = Entry(content)
		
		btn = Button(content, text="Save")
		
		content.grid(row=0, column=0)
		
		l1.grid(row=0, column=0)
		e1.grid(row=0, column=1)
		btn.grid(column=0, row=1, columnspan=4)
		
		
	def update(self, img):
		img = cv2.flip(img, 1)
		img1 = np.ascontiguousarray(img[:, :, ::-1])
		img = ImageTk.PhotoImage(Image.fromarray(img1))
		self.l1['image']=img
		self.root.update()
		
video = cv2.VideoCapture(0)	
app = Application()
while True:
	ret, img = video.read()
	app.update(img)
	
video.release()
