from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import numpy as np


class ImageEditor:
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

		menubar =Menu(root, background = "#bbbbc9", activebackground = "#adadba",relief = FLAT)
		filemenu = Menu(menubar, tearoff=0, background = "#bbbbc9", activebackground = "#adadba",relief = FLAT)
		filemenu.add_command(label="Load image", command=self.say_hi, background = "#bbbbc9", activebackground = "#adadba")
		filemenu.add_command(label="Save image", command=self.say_hi, background = "#bbbbc9", activebackground = "#adadba")
		filemenu.add_separator()
		filemenu.add_command(label="Quit", command=master.quit, background = "#bbbbc9", activebackground = "#adadba")
		menubar.add_cascade(label="File", menu=filemenu, background = "#bbbbc9", activebackground = "#adadba")
		root.config(menu=menubar)

		self.status = Label(statusFrame, text = "Status", bg ="#bbbbc9", anchor = W)
		self.status.pack(side = BOTTOM, fill ="x")

		self.canvas = Canvas(imageFrame, width = 300, height = 300, bg = "#404040", highlightthickness= 0, relief = FLAT)
		self.canvas.pack(fill ="both", expand = True)


		#Buttons
		self.rotateL   = Button(buttonFrame, text="rotateL", command = self.say_hi, bg = "#404040", fg = "#fff3d3", activebackground = "#8fa876", relief = FLAT, highlightthickness = 0, cursor = "hand2").pack(fill = "x")
		self.rotateR   = Button(buttonFrame, text="rotateR", command = self.say_hi, bg = "#404040", fg = "#fff3d3", activebackground = "#8fa876", relief = FLAT, highlightthickness = 0, cursor = "hand2").pack(fill = "x")
		self.mirrorX   = Button(buttonFrame, text="mirrorX", command = self.say_hi, bg = "#404040", fg = "#fff3d3", activebackground = "#8fa876", relief = FLAT, highlightthickness = 0, cursor = "hand2").pack(fill = "x")
		self.mirrorY   = Button(buttonFrame, text="mirrorY", command = self.say_hi, bg = "#404040", fg = "#fff3d3", activebackground = "#8fa876", relief = FLAT, highlightthickness = 0, cursor = "hand2").pack(fill = "x")
		self.inverse   = Button(buttonFrame, text="inverse", command = self.say_hi, bg = "#404040", fg = "#fff3d3", activebackground = "#8fa876", relief = FLAT, highlightthickness = 0, cursor = "hand2").pack(fill = "x")
		self.gray 	   = Button(buttonFrame, text="toGray", command = self.say_hi, bg = "#404040", fg = "#fff3d3", activebackground = "#8fa876", relief = FLAT, highlightthickness = 0, cursor = "hand2").pack(fill = "x")
		self.bright    = Button(buttonFrame, text="brigthen", command = self.say_hi, bg = "#404040", fg = "#fff3d3", activebackground = "#8fa876", relief = FLAT, highlightthickness = 0, cursor = "hand2").pack(fill = "x")
		self.dark 	   = Button(buttonFrame, text="darken", command = self.say_hi, bg = "#404040", fg = "#fff3d3", activebackground = "#8fa876", relief = FLAT, highlightthickness = 0, cursor = "hand2").pack(fill = "x")
		self.contrastM = Button(buttonFrame, text="moreContrast", command = self.say_hi, bg = "#404040", fg = "#fff3d3", activebackground = "#8fa876", relief = FLAT, highlightthickness = 0, cursor = "hand2").pack(fill = "x")
		self.contrastL = Button(buttonFrame, text="lessContrast", command = self.say_hi, bg = "#404040", fg = "#fff3d3", activebackground = "#8fa876", relief = FLAT, highlightthickness = 0, cursor = "hand2").pack(fill = "x")

	def say_hi(self):
		print("hello")

root = Tk()
root.minsize(408, 347)

app= ImageEditor(root)

root.mainloop()