from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import numpy as np


class ImageEditor:

	def show_image(self):
		factor = (259.0 * (self.contrast + 255.0)) / (255.0 * (259.0 - self.contrast))
		tmp = Image.fromarray(np.clip((factor *(self.picturedata-128.0)+128)*self.brightness,0,255).astype(dtype=np.uint8))
		self.img = ImageTk.PhotoImage(tmp)
		self.canvas.create_image(self.width/2,self.height/2, anchor = CENTER, image = self.img)

	def negative (self):
		if self.picturedata.size:
			data = self.picturedata
			negativ = 255 - data
			self.picturedata = negativ 
			self.show_image()
		else:
			self.status['text'] = "No file loaded!"

	def rotateLeft (self):
		if self.picturedata.size:
			data = self.picturedata
			rotLeft = np.rot90(data)
			self.picturedata = rotLeft 
			self.show_image()
		else:
			self.status['text'] = "No file loaded!"

	def rotateRight (self):
		if self.picturedata.size:
			data = self.picturedata
			rotRight = np.rot90(data, axes=(1,0))
			self.picturedata = rotRight 
			self.show_image()
		else:
			self.status['text'] = "No file loaded!"

	def flipX (self):
		if self.picturedata.size:
			data = self.picturedata
			flipx = np.flip(data,0)
			self.picturedata = flipx 
			self.show_image()
		else:
			self.status['text'] = "No file loaded!"

	def flipY (self):
		if self.picturedata.size:
			data = self.picturedata
			flipy = np.flip(data,1)
			self.picturedata = flipy 
			self.show_image()
		else:
			self.status['text'] = "No file loaded!"

	def makeGray (self):
		if self.picturedata.size:
			data = self.picturedata
			if data.ndim==3:
				gray = (data * np.array([[[0.299, 0.587, 0.114]]])).sum(axis=2).astype(dtype=np.uint8)
				self.picturedata = gray 
				self.show_image()
			else:
				self.status['text'] = "Image is already in gray colors!"
		else:
			self.status['text'] = "No file loaded!"

	def brightenUp (self):
		if self.picturedata.size:
			if self.brightness<2.5:
				self.brightness+=0.05
				self.show_image()
			else:
				self.status['text'] = "No more brigthness can be added!"
		else:
			self.status['text'] = "No file loaded!"

	def brightenDown (self):
		if self.picturedata.size:
			if self.brightness>0:
				self.brightness-=0.05
				self.show_image()
			else:
				self.status['text'] = "No more brigthness can be substracted!"
		else:
			self.status['text'] = "No file loaded!"

	def contrastUp (self):
		if self.picturedata.size:
			if self.contrast<255:
				self.contrast+=5
				self.show_image()
			else:
				self.status['text'] = "No more contrast can be added!"
		else:
			self.status['text'] = "No file loaded!"

	def contrastDown (self):
		if self.picturedata.size:
			if self.contrast>-255:
				self.contrast-=5
				self.show_image()
			else:
				self.status['text'] = "No more contrast can be substracted!"
		else:
			self.status['text'] = "No file loaded!"

	def loadImage(self):
		fname = filedialog.askopenfilename()
		if fname:
			try:
				self.picturedata =np.asarray(Image.open(fname))
				self.show_image()
				self.imageLoaded =1
				self.status['text'] = "Image loaded."
			except:
				self.status['text'] = "Unsupported file format"
				self.imageLoaded = 0

	def saveImage(self):
		if self.picturedata.size:
			fname =  filedialog.asksaveasfilename()
			if fname:
				try:
					factor = (259.0 * (self.contrast + 255.0)) / (255.0 * (259.0 - self.contrast))
					tmp = Image.fromarray(np.clip((factor *(self.picturedata-128.0)+128)*self.brightness,0,255).astype(dtype=np.uint8))
					tmp.save(fname)
					self.status['text'] = "Image saved."
				except:
					self.status['text'] = "Oops! Something went wrong when saving the image."
		else:
			self.status['text'] = "No file loaded!"

	def sizeEvent (self, event):
		self.status['text'] = str(event.width) +"x"+str(event.height)

	def canvasEvent(self, event):
		self.width = event.width
		self.height = event.height
		if self.imageLoaded:
			self.canvas.delete("all")
			self.show_image()

	def __init__(self,master):
		self.imageLoaded = 0
		self.width = 408
		self.height = 347
		self.picturedata = np.array([])
		self.brightness = 1
		self.contrast = 0
		master.title("Image Editor")
		rootFrame 	= Frame(master, bg = "#404040")
		imageFrame  = Frame(rootFrame, bg = "#404040")
		buttonFrame = Frame(rootFrame, bg = "#404040")
		statusFrame = Frame(master, bg = "#404040")
		rootFrame.pack(side = TOP,fill = "both", expand = True)
		imageFrame.pack(fill ="both", expand = True, side = LEFT)
		buttonFrame.pack(fill ="y", side = RIGHT, anchor =E)
		statusFrame.pack(fill ="x", side = BOTTOM, anchor =S)
		rootFrame.bind("<Configure>", self.sizeEvent)

		menubar =Menu(root, background = "#bbbbc9", activebackground = "#adadba",relief = FLAT)
		filemenu = Menu(menubar, tearoff=0, background = "#bbbbc9", activebackground = "#adadba",relief = FLAT)
		filemenu.add_command(label="Load image", command=self.loadImage, background = "#bbbbc9", activebackground = "#adadba")
		filemenu.add_command(label="Save image", command=self.saveImage, background = "#bbbbc9", activebackground = "#adadba")
		filemenu.add_separator()
		filemenu.add_command(label="Quit", command=master.quit, background = "#bbbbc9", activebackground = "#adadba")
		menubar.add_cascade(label="File", menu=filemenu, background = "#bbbbc9", activebackground = "#adadba")
		root.config(menu=menubar)

		self.status = Label(statusFrame, text = "Status", bg ="#bbbbc9", anchor = W)
		self.status.pack(side = BOTTOM, fill ="x")

		self.canvas = Canvas(imageFrame, width = 300, height = 300, bg = "#404040", highlightthickness= 0, relief = FLAT)
		self.canvas.pack(fill ="both", expand = True)
		self.canvas.bind("<Configure>", self.canvasEvent)


		#Buttons
		self.rotateL   = Button(buttonFrame, text="Rotate <-", command = self.rotateLeft, bg = "#404040", fg = "#fff3d3", activebackground = "#8fa876", relief = FLAT, highlightthickness = 0, cursor = "hand2").pack(fill = "x")
		self.rotateR   = Button(buttonFrame, text="Rotate ->", command = self.rotateRight, bg = "#404040", fg = "#fff3d3", activebackground = "#8fa876", relief = FLAT, highlightthickness = 0, cursor = "hand2").pack(fill = "x")
		self.mirrorX   = Button(buttonFrame, text="Flip X", command = self.flipX, bg = "#404040", fg = "#fff3d3", activebackground = "#8fa876", relief = FLAT, highlightthickness = 0, cursor = "hand2").pack( fill = "x")
		self.mirrorY   = Button(buttonFrame, text="Flip Y", command = self.flipY, bg = "#404040", fg = "#fff3d3", activebackground = "#8fa876", relief = FLAT, highlightthickness = 0, cursor = "hand2").pack(fill = "x")
		self.inverse   = Button(buttonFrame, text="Inverse colors", command = self.negative, bg = "#404040", fg = "#fff3d3", activebackground = "#8fa876", relief = FLAT, highlightthickness = 0, cursor = "hand2").pack(fill = "x")
		self.gray 	   = Button(buttonFrame, text="Gray colors", command = self.makeGray, bg = "#404040", fg = "#fff3d3", activebackground = "#8fa876", relief = FLAT, highlightthickness = 0, cursor = "hand2").pack(fill = "x")
		self.bright    = Button(buttonFrame, text="Brighten", command = self.brightenUp, bg = "#404040", fg = "#fff3d3", activebackground = "#8fa876", relief = FLAT, highlightthickness = 0, cursor = "hand2").pack(fill = "x")
		self.dark 	   = Button(buttonFrame, text="Darken", command = self.brightenDown, bg = "#404040", fg = "#fff3d3", activebackground = "#8fa876", relief = FLAT, highlightthickness = 0, cursor = "hand2").pack(fill = "x")
		self.contrastM = Button(buttonFrame, text="More contrast", command = self.contrastUp, bg = "#404040", fg = "#fff3d3", activebackground = "#8fa876", relief = FLAT, highlightthickness = 0, cursor = "hand2").pack(fill = "x")
		self.contrastL = Button(buttonFrame, text="Less contrast", command = self.contrastDown, bg = "#404040", fg = "#fff3d3", activebackground = "#8fa876", relief = FLAT, highlightthickness = 0, cursor = "hand2").pack(fill = "x")

	def say_hi(self):
		print("hello")

root = Tk()
root.minsize(408, 347)

app= ImageEditor(root)

root.mainloop()