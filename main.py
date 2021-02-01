from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox
import pygame
import time

def raise_frame(frame):
	frame.tkraise()


class Dragonator(object):	

	MH_1_Proof_Of_A_Hero = "Music\Monster hunter PROOF OF A HERO (original full ost) HQ.mp3"
	MH_DOS_Proof_Of_A_Hero = "Music\Monster Hunter Freedom 2 - Proof of a Hero (Credits).mp3"
	MH_TRI_Proof_Of_A_Hero = "Music\Monster Hunter 3 (tri-) OST - Proof of a Hero Monster Hunter main theme.mp3"
	MH_4_Proof_Of_A_Hero = "Music\Monster Hunter 4 - Proof of a Hero.mp3"
	MHGU_Proof_Of_A_Hero = "Music\Monster Hunter Hunting Music Collection XX - 15 - Proof of a Hero MHXXver"
	MH_World_Proof_Of_A_Hero = "Music\Monster Hunter World OST Proof of a Hero (Extended)"
	
	def __init__(self):
		pygame.mixer.init()
		self.window = Tk()
		
		# **** Settings and Details ****
		self.window.title("The Dragonator")
		self.window_background = ImageTk.PhotoImage(Image.open("commander4.jpg"))
		self.window_label = Label(self.window, image=self.window_background)
		self.window.geometry("500x400")
		self.window.resizable(0, 0)

		# **** Frames ****
		self.basicTextFrame = Frame(self.window)
		self.welcomeLabel = Label(self.basicTextFrame, text="Welcome Hunter", bg="red")
		self.generationFrame = Frame(self.window)
		self.controlWindowFrame = Frame(self.window)
		self.fourthFrame = Frame(self.window)


		# **** Buttons ****
		self.first_generation_button = Button(self.generationFrame, text="First Generation", command=lambda: self.play(1))
		self.second_generation_button = Button(self.generationFrame, text="Second Generation", command=lambda: self.play(2))
		self.third_generation_button = Button(self.generationFrame, text="Third Generation", command=lambda: self.play(3))

		# **** Packing Frames ****
		self.basicTextFrame.grid(column=0, row=0)
		self.welcomeLabel.pack()


		self.welcomeQuestion = tkinter.messagebox.askquestion("Question", "Do you know where my dragonator is located?")
		if self.welcomeQuestion != "yes":
			tkinter.messagebox.showinfo("Okay", "Oh, well uh... look at the time. I'm heading out. Goodbye!")
			time.sleep(2.5)
			exit()
		else:
			self.welcomeLabel.config(text="Pick a generation")
			self.generationFrame.grid(column=1, row=0)

			# **** Packing Buttons ****
			self.first_generation_button.pack(pady=5)
			self.second_generation_button.pack(pady=5)
			self.third_generation_button.pack(pady=5)

			self.window_label.grid()
			self.window.mainloop()

	def play(self, button):
		if(button == 1):
			pygame.mixer.music.load(self.MH_1_Proof_Of_A_Hero)
		elif(button == 2):
			pygame.mixer.music.load(self.MH_DOS_Proof_Of_A_Hero)
		elif(button == 3):
			pygame.mixer.music.load(self.MH_TRI_Proof_Of_A_Hero)
		elif(button == 4):
			pass

		pygame.mixer.music.play()

The_CommandersDragonator = Dragonator()
'''
	def __init__(self):
		pygame.mixer.init()
		self.window = Tk()
		
		# **** Settings and Details ****
		self.window.title("The Dragonator")
		self.window_background = ImageTk.PhotoImage(Image.open("commander4.jpg"))
		self.window_label = Label(self.window, image=self.window_background)
		self.window.geometry("500x400")
		self.window.resizable(0, 0)

		# **** Frames ****
		self.basicTextFrame = Frame(self.window)
		self.welcomeLabel = Label(self.basicTextFrame, text="Welcome Hunter", bg="red")
		self.generationFrame = Frame(self.window)
		self.controlWindowFrame = Frame(self.window)
		self.fourthFrame = Frame(self.window)


		# **** Buttons ****
		self.first_generation_button = Button(self.generationFrame, text="First Generation", command=lambda: self.play(1))
		self.second_generation_button = Button(self.generationFrame, text="Second Generation", command=lambda: self.play(2))
		self.third_generation_button = Button(self.generationFrame, text="Third Generation", command=lambda: self.play(3))
		self.fourth_generation_button = Button(self.generationFrame, text="Fourth Generation", command=lambda:self.play(4))
		self.fifith_generation_button = Button(self.generationFrame, text="Fifth Generation")

		# **** Packing Frames ****
		self.basicTextFrame.pack()
		self.welcomeLabel.pack()


		self.welcomeQuestion = tkinter.messagebox.askquestion("Question", "Do you know where my dragonator is located?")
		if self.welcomeQuestion != "yes":
			tkinter.messagebox.showinfo("Okay", "Oh, well uh... look at the time. I'm heading out. Goodbye!")
			time.sleep(2.5)
			exit()
		else:
			self.welcomeLabel.config(text="Pick a generation")
			self.generationFrame.pack(side=BOTTOM)

			# **** Packing Buttons ****
			self.first_generation_button.pack(pady=5)
			self.second_generation_button.pack(pady=5)
			self.third_generation_button.pack(pady=5)
			self.fourth_generation_button.pack(pady=5)
			self.fifith_generation_button.pack(pady=5)



			self.window_label.pack()
			self.window.mainloop()

	def play(self, button):
		if(button == 1):
			pygame.mixer.music.load(self.MH_1_Proof_Of_A_Hero)
		elif(button == 2):
			pygame.mixer.music.load(self.MH_DOS_Proof_Of_A_Hero)
		elif(button == 3):
			pygame.mixer.music.load(self.MH_TRI_Proof_Of_A_Hero)
		elif(button == 4):
			
		#pygame.mixer.music.play()
	'''