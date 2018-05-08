from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import numpy as np


class ImageEditor:
	imageLoaded = 0
	width = 408
	height = 347
	picture = ""

	def show_image(self):
		self.img = ImageTk.PhotoImage(self.picture)
		self.canvas.create_image(self.width/2,self.height/2, anchor = CENTER, image = self.img)

	def negative (self):
		if self.picture:
			data = np.asarray(self.picture,dtype=np.uint8)
			negativ = 255 - data
			self.picture = Image.fromarray(negativ) 
			self.show_image()
		else:
			self.status['text'] = "No file loaded!"

	def rotateLeft (self):
		if self.picture:
			data = np.asarray(self.picture,dtype=np.uint8)
			rotLeft = np.rot90(data)
			self.picture = Image.fromarray(rotLeft) 
			self.show_image()
		else:
			self.status['text'] = "No file loaded!"

	def rotateRight (self):
		if self.picture:
			data = np.asarray(self.picture,dtype=np.uint8)
			rotRight = np.rot90(data, axes=(1,0))
			self.picture = Image.fromarray(rotRight) 
			self.show_image()
		else:
			self.status['text'] = "No file loaded!"

	def flipX (self):
		if self.picture:
			data = np.asarray(self.picture,dtype=np.uint8)
			flipx = np.flip(data,0)
			self.picture = Image.fromarray(flipx) 
			self.show_image()
		else:
			self.status['text'] = "No file loaded!"

	def flipY (self):
		if self.picture:
			data = np.asarray(self.picture,dtype=np.uint8)
			flipy = np.flip(data,1)
			self.picture = Image.fromarray(flipy) 
			self.show_image()
		else:
			self.status['text'] = "No file loaded!"

	def makeGray (self):
		return

	def brightenUp (self):
		return

	def brightenDown (self):
		return

	def contrastUp (self):
		return

	def contrastDown (self):
		return

	def loadImage(self):
		fname = filedialog.askopenfilename()
		if fname:
			try:
				self.picture = Image.open(fname)
				self.show_image()
				self.imageLoaded =1
			except:
				self.status['text'] = "Unsupported file format"
				self.imageLoaded = 0

	def sizeEvent (self, event):
		self.status['text'] = str(event.width) +"x"+str(event.height)

	def canvasEvent(self, event):
		self.width = event.width
		self.height = event.height
		if self.imageLoaded:
			self.canvas.delete("all")
			self.show_image()

	def __init__(self,master):
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
		filemenu.add_command(label="Save image", command=self.say_hi, background = "#bbbbc9", activebackground = "#adadba")
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
		self.rotateL   = Button(buttonFrame, text="rotateL", command = self.rotateLeft, bg = "#404040", fg = "#fff3d3", activebackground = "#8fa876", relief = FLAT, highlightthickness = 0, cursor = "hand2").pack(fill = "x")
		self.rotateR   = Button(buttonFrame, text="rotateR", command = self.rotateRight, bg = "#404040", fg = "#fff3d3", activebackground = "#8fa876", relief = FLAT, highlightthickness = 0, cursor = "hand2").pack(fill = "x")
		self.mirrorX   = Button(buttonFrame, text="mirrorX", command = self.flipX, bg = "#404040", fg = "#fff3d3", activebackground = "#8fa876", relief = FLAT, highlightthickness = 0, cursor = "hand2").pack(fill = "x")
		self.mirrorY   = Button(buttonFrame, text="mirrorY", command = self.flipY, bg = "#404040", fg = "#fff3d3", activebackground = "#8fa876", relief = FLAT, highlightthickness = 0, cursor = "hand2").pack(fill = "x")
		self.inverse   = Button(buttonFrame, text="inverse", command = self.negative, bg = "#404040", fg = "#fff3d3", activebackground = "#8fa876", relief = FLAT, highlightthickness = 0, cursor = "hand2").pack(fill = "x")
		self.gray 	   = Button(buttonFrame, text="toGray", command = self.makeGray, bg = "#404040", fg = "#fff3d3", activebackground = "#8fa876", relief = FLAT, highlightthickness = 0, cursor = "hand2").pack(fill = "x")
		self.bright    = Button(buttonFrame, text="brigthen", command = self.brightenUp, bg = "#404040", fg = "#fff3d3", activebackground = "#8fa876", relief = FLAT, highlightthickness = 0, cursor = "hand2").pack(fill = "x")
		self.dark 	   = Button(buttonFrame, text="darken", command = self.brightenDown, bg = "#404040", fg = "#fff3d3", activebackground = "#8fa876", relief = FLAT, highlightthickness = 0, cursor = "hand2").pack(fill = "x")
		self.contrastM = Button(buttonFrame, text="moreContrast", command = self.contrastUp, bg = "#404040", fg = "#fff3d3", activebackground = "#8fa876", relief = FLAT, highlightthickness = 0, cursor = "hand2").pack(fill = "x")
		self.contrastL = Button(buttonFrame, text="lessContrast", command = self.contrastDown, bg = "#404040", fg = "#fff3d3", activebackground = "#8fa876", relief = FLAT, highlightthickness = 0, cursor = "hand2").pack(fill = "x")

	def say_hi(self):
		print("hello")

root = Tk()
root.minsize(408, 347)

app= ImageEditor(root)

root.mainloop()