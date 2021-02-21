from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox
import pygame
import time

MH_1_Proof_Of_A_Hero = "Music\Monster hunter PROOF OF A HERO (original full ost) HQ.mp3"
MH_DOS_Proof_Of_A_Hero = "Music\Monster Hunter Freedom 2 - Proof of a Hero (Credits).mp3"
MH_TRI_Proof_Of_A_Hero = "Music\Monster Hunter 3 (tri-) OST - Proof of a Hero Monster Hunter main theme.mp3"
MH_4_Proof_Of_A_Hero = "Music\Monster Hunter 4 - Proof of a Hero.mp3"
MHGU_Proof_Of_A_Hero = "Music\Monster Hunter Hunting Music Collection XX - 15 - Proof of a Hero MHXXver"
MH_World_Proof_Of_A_Hero = "Music\Monster Hunter World OST Proof of a Hero (Extended)"
IMAGE = "commander4.jpg"

# TODO Finish the UI for the Fourth Generation and previous Generations
# TODO Get the image to show up on the grid
# TODO Merge branches when complete to get rid of the Fourth Generation on.
# TODO Complete the Fifth Generation Branch


class Dragonator:
	def __init__(self):
		pygame.mixer.init()
		self.main_window = Tk()
		self.main_window.title("The Dragonator v1.1")
		self.main_window.geometry("510x400")
		self.main_window.resizable(0, 0)
		self.firstThroughThirdGen = Frame(self.main_window, bg="gray")
		self.fourthGen = Frame(self.main_window)

		for frames in (self.firstThroughThirdGen, self.fourthGen):
			frames.grid(row=0, column=0, sticky='nsew')

		self.firstThroughThirdGen.tkraise()
		self.meme_image = ImageTk.PhotoImage(Image.open(IMAGE))
		self.meme_label = Label(self.firstThroughThirdGen, image= self.meme_image)
		self.welcomeLabel = Label(self.firstThroughThirdGen, text="Welcome Hunter", bg="red")
		self.welcomeLabel.grid(row=0, column=0)
		self.welcomeQuestion = tkinter.messagebox.askquestion("Question", "Do you know where my dragonator is located?")
		if self.welcomeQuestion == "no":
			tkinter.messagebox.showinfo("Okay", "Oh, well uh... look at the time. I'm heading out. Goodbye!")
			time.sleep(2.5)
			exit()
		else:
			self.welcomeLabel.config(text="Pick a generation")
			self.meme_label.grid(row=4)

			self.first_generation_button = Button(self.firstThroughThirdGen, text="First Generation", command=lambda: self.play(1))
			self.second_generation_button = Button(self.firstThroughThirdGen, text="Second Generation", command=lambda:self.play(2)) # I think I need to get a new audio file. There are some extra bits that aren't proof of a hero
			self.third_generation_button = Button(self.firstThroughThirdGen, text="Third Generation", command=lambda: self.play(3))
			self.first_generation_button.grid(row=3, column=5, rowspan=2)
			self.second_generation_button.grid(row=3, column=6, rowspan=2)
			self.third_generation_button.grid(row=3, column=7, rowspan=2)
			

			self.main_window.mainloop()

	def play(self, button, extraGameId=0):
		if(button == 1):
			pygame.mixer.music.load(MH_1_Proof_Of_A_Hero)
		elif(button == 2):
			pygame.mixer.music.load(MH_DOS_Proof_Of_A_Hero)
		elif(button == 3):
			pygame.mixer.music.load(MH_TRI_Proof_Of_A_Hero)
		elif(button == 4 and extraGameId == 1):
			pygame.mixer.music.load(MH_4_Proof_Of_A_Hero)
		elif(button == 4 and extraGameId == 2):
			pygame.mixer.music.load(MHGU_Proof_Of_A_Hero)
		pygame.mixer.music.play()

The_CommandersDragonator = Dragonator()