from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox
import pygame
import time
import data 


class Dragonator:

	def __init__(self):
		pygame.mixer.init()
		self.main_window = Tk()
		self.main_window.title("The Dragonator v" + data.VERSION)
		self.pimage = tkinter.PhotoImage(file=data.PROGRAM_ICON)
		self.main_window.iconphoto(False, self.pimage)
		self.main_window.geometry("620x210")
		self.main_window.resizable(0, 0)
		self.first_through_third_gen = Frame(self.main_window, bg="gray")
		self.fourth_gen = Frame(self.main_window, bg="gray")
		self.fifth_gen = Frame(self.main_window, bg="gray")


		for frames in (self.first_through_third_gen, self.fourth_gen, self.fifth_gen):
			frames.grid(row=0, column=0, sticky='nsew')


		self.first_through_third_gen.tkraise()
		self.meme_image = ImageTk.PhotoImage(Image.open(data.FRONT_IMAGE))
		self.one_fourth_gen_image = ImageTk.PhotoImage(Image.open(data.FOURTH_GEN_FLAGSHIP2))
		self.two_fourth_gen_image = ImageTk.PhotoImage(Image.open(data.GENERATIONS_FLAGSHIP))
		self.one_fifth_gen_image = ImageTk.PhotoImage(Image.open(data.WORLD_FLAGSHIP))
		self.two_fifth_gen_image = ImageTk.PhotoImage(Image.open(data.RISE_FLAGSHIP))
		self.meme_label = Label(self.first_through_third_gen, image= self.meme_image)
		self.insect_glavie_with_gore = Label(self.fourth_gen, image=self.one_fourth_gen_image)
		self.hunters_with_valstrax = Label(self.fourth_gen, image=self.two_fourth_gen_image)
		self.nergignate_with_hunters = Label(self.fifth_gen, image=self.one_fifth_gen_image)
		self.magnamalo_image = Label(self.fifth_gen, image=self.two_fifth_gen_image)
		self.welcome_label = Label(self.first_through_third_gen, text="Welcome Hunter", bg="red")
		self.fourth_gen = Label(self.fourth_gen, text="Fourth Generation")
		self.fifth_gen = Label(self.fifth_gen, text="Fifth Generation")
		self.welcome_label.grid(row=0, column=0)
		self.welcome_question = tkinter.messagebox.askquestion("Question", "Do you know where my dragonator is located?")


		if self.welcome_question == "no":
			tkinter.messagebox.showinfo("Okay", "Oh, well uh... look at the time. I'm heading out. Goodbye!")
			time.sleep(2.5)
			exit()
		else:
			# **** First Generation to Third Geneartion Frame 
			self.welcome_label.config(text="Pick a generation")
			self.meme_label.grid(row=0, column=1, padx=3)
			self.first_generation_button = Button(self.first_through_third_gen, text="First Generation", command=lambda: self.play(1))
			self.second_generation_button = Button(self.first_through_third_gen, text="Second Generation", command=lambda:self.play(2)) # I think I need to get a new audio file. There are some extra bits that aren't proof of a hero
			self.third_generation_button = Button(self.first_through_third_gen, text="Third Generation", command=lambda: self.play(3))
			self.fourth_generation_button = Button(self.first_through_third_gen, text="Fourth Generation", command=lambda: self.fourthGen.tkraise())
			self.fifth_generation_button = Button(self.first_through_third_gen, text="Fifth Generation", command=lambda: self.fifthGen.tkraise())
			self.first_generation_button.grid(row=0, column=3, padx=2)
			self.second_generation_button.grid(row=0, column=4, padx=2)
			self.third_generation_button.grid(row=0, column= 6)
			self.fourth_generation_button.place(x=320, y=120)
			self.fifth_generation_button.place(x=430, y=120)

			# **** Fourth Generation Frame ****
			self.fourth_label.pack()
			self.insect_glavie_with_gore.pack(side=LEFT)
			self.hunters_with_valstrax.pack(side=LEFT)
			self.MH4U_Button = Button(self.fourth_gen, text="MH4U", command=lambda:self.play(4, 1))
			self.MHGU_Button = Button(self.fourth_gen, text="MHGU", command=lambda:self.play(4, 2))
			self.back_button1 = Button(self.fourth_gen, text="Back", command=lambda:self.first_through_third_gen.tkraise())
			self.MH4U_Button.pack()
			self.MHGU_Button.pack()
			self.back_button1.pack(fill=BOTH)

			# **** Fifth Generation Frame ****
			self.fifthLabel.pack()
			self.nergignate_with_hunters.pack(side=LEFT)
			self.magnamalo_image.pack(side=LEFT)
			self.MH_World_Button = Button(self.fifth_gen, text="Monster Hunter World", command=lambda:self.play(5, 1))
			self.MH_Rise_Button = Button(self.fifth_gen, text="Monster Hunter Rise", command=lambda:self.play(5, 2))
			self.back_button2 = Button(self.fifth_gen, text="Back", command=lambda:self.first_through_third_gen.tkraise())
			self.MH_World_Button.pack()
			self.MH_Rise_Button.pack()
			self.back_button2.pack(fill=BOTH)

			self.main_window.mainloop()


	def play(self, button, extra_game_id=0):
		if(button == 1):
			pygame.mixer.music.load(MH_1_Proof_Of_A_Hero)
		elif(button == 2):
			pygame.mixer.music.load(MH_DOS_Proof_Of_A_Hero)
		elif(button == 3):
			pygame.mixer.music.load(MH_TRI_Proof_Of_A_Hero)
		elif(button == 4 and extra_game_id == 1):
			pygame.mixer.music.load(MH_4_Proof_Of_A_Hero)
		elif(button == 4 and extra_game_id == 2):
			pygame.mixer.music.load(MHGU_Proof_Of_A_Hero)
		elif(button == 5 and extra_game_id == 1):
			pygame.mixer.music.load(MH_World_Proof_Of_A_Hero)
		elif(button == 5 and extra_game_id == 2):
			pygame.mixer.music.load(MH_Rise_Proof_Of_A_Hero)
		pygame.mixer.music.play()

