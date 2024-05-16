from tkinter import *
from PIL import Image, ImageTk
import cv2
import numpy as np
import threading
import time

class Application():
	def __init__(self):
		self.root = Tk()
		self.root.title("Camera")
		self.root.geometry("500x450")
	
		self.l1=Label(self.root)
		self.l1.pack()
		
		self.b1=Button(self.root,
			text='Save Person', height=5, width=20,
			command=self.savePerson)
		self.b1.pack(side=LEFT,fill=BOTH, padx=60,pady=5)
		
		
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
		img = cv2.flip(img, 1)
		img1 = np.ascontiguousarray(img[:, :, ::-1])
		image = Image.fromarray(img1)
		image = self.resize(image)
	
		img = ImageTk.PhotoImage(image)
		self.l1.configure(image=img)
		self.l1.photo=img

app = Application()

def update(app):
	video = cv2.VideoCapture(0)	
	while True:
		
		ret, img = video.read()
		if ret:
			app.update(img)
		time.sleep(0.001)
			
thread = threading.Thread(target=update, args=[app])
thread.daemon=True
thread.start()

app.root.mainloop()





