import tkinter
from PIL import ImageTk, Image
import tkinter.messagebox
import pygame
import time
import random
import data


class Dragonator:

	def __init__(self):
		pygame.mixer.init()
		self.main_window = tkinter.Tk()
		self.main_window.title("The Dragonator v" + data.VERSION)
		self.pimage = tkinter.PhotoImage(file=data.PROGRAM_ICON)
		self.main_window.iconphoto(False, self.pimage)
		self.main_window.geometry("620x210")
		self.main_window.resizable(0, 0)
		self.first_through_third_gen = tkinter.Frame(self.main_window, bg="gray")
		self.fourth_gen = tkinter.Frame(self.main_window, bg="gray")
		self.fifth_gen = tkinter.Frame(self.main_window, bg="gray")


		for frames in (self.first_through_third_gen, self.fourth_gen, self.fifth_gen):
			frames.grid(row=0, column=0, sticky='nsew')


		self.first_through_third_gen.tkraise()
		self.commander_image = ImageTk.PhotoImage(Image.open(data.FRONT_IMAGE))
		self.gore_magala_image = ImageTk.PhotoImage(Image.open(data.FOURTH_GEN_FLAGSHIP2))
		self.valstrax_image = ImageTk.PhotoImage(Image.open(data.GENERATIONS_FLAGSHIP))
		self.nergignate_image = ImageTk.PhotoImage(Image.open(data.WORLD_FLAGSHIP))
		self.magnamalo_image = ImageTk.PhotoImage(Image.open(data.RISE_FLAGSHIP))
		self.front_image = tkinter.Label(self.first_through_third_gen, image= self.commander_image)
		self.gore = tkinter.Label(self.fourth_gen, image=self.gore_magala_image)
		self.val = tkinter.Label(self.fourth_gen, image=self.valstrax_image)
		self.nergignate = tkinter.Label(self.fifth_gen, image=self.nergignate_image)
		self.magna = tkinter.Label(self.fifth_gen, image=self.magnamalo_image)
		self.welcome_label = tkinter.Label(self.first_through_third_gen, text="Welcome Hunter", bg="red")
		self.welcome_label.grid(row=0, column=0)
		self.fourth_label = tkinter.Label(self.fourth_gen, text="Fourth Generation")
		self.fifth_label = tkinter.Label(self.fifth_gen, text="Fifth Generation")

		self.welcome_label.config(text="Pick a generation")
		self.front_image.grid(row=0, column=1, padx=3)
		self.first_generation_button = tkinter.Button(self.first_through_third_gen, text="First Generation", command= lambda: self.play(1))
		self.second_generation_button = tkinter.Button(self.first_through_third_gen, text="Second Generation", command= lambda: self.play(2)) # I think I need to get a new audio file. There are some extra bits that aren't proof of a hero
		self.third_generation_button = tkinter.Button(self.first_through_third_gen, text="Third Generation", command= lambda: self.play(3))
		self.random_pick_button = tkinter.Button(self.first_through_third_gen, text="Wildcard", command= lambda: self.play_random_song())
		self.fourth_generation_button = tkinter.Button(self.first_through_third_gen, text="Fourth Generation", command= lambda: self.fourth_gen.tkraise())
		self.fifth_generation_button = tkinter.Button(self.first_through_third_gen, text="Fifth Generation", command= lambda: self.fifth_gen.tkraise())
		self.first_generation_button.grid(row=0, column=3, padx=2)
		self.second_generation_button.grid(row=0, column=4, padx=2)
		self.third_generation_button.grid(row=0, column= 6)
		self.random_pick_button.place(x=530, y=120)
		self.fourth_generation_button.place(x=320, y=120)
		self.fifth_generation_button.place(x=430, y=120)

			# **** Fourth Generation Frame ****
		self.fourth_label.pack()
		self.gore.pack(side=tkinter.LEFT)
		self.val.pack(side=tkinter.LEFT)
		self.mh4u_button = tkinter.Button(self.fourth_gen, text="MH4U", command=lambda:self.play(4, 1))
		self.mhgu_button = tkinter.Button(self.fourth_gen, text="MHGU", command=lambda:self.play(4, 2))
		self.back_button1 = tkinter.Button(self.fourth_gen, text="Back", command=lambda:self.first_through_third_gen.tkraise())
		self.mh4u_button.pack()
		self.mhgu_button.pack()
		self.back_button1.pack(fill=tkinter.BOTH)

			# **** Fifth Generation Frame ****
		self.fifth_label.pack()
		self.nergignate.pack(side=tkinter.LEFT)
		self.magna.pack(side=tkinter.LEFT)
		self.mh_world_button = tkinter.Button(self.fifth_gen, text="Monster Hunter World", command=lambda:self.play(5, 1))
		self.mh_rise_button = tkinter.Button(self.fifth_gen, text="Monster Hunter Rise", command=lambda:self.play(5, 2))
		self.back_button2 = tkinter.Button(self.fifth_gen, text="Back", command=lambda:self.first_through_third_gen.tkraise())
		self.mh_world_button.pack()
		self.mh_rise_button.pack()
		self.back_button2.pack(fill=tkinter.BOTH)

		self.main_window.mainloop()


	def play_random_song(self):
		a = random.randint(1, 5)
		b = random.randint(1, 2) if a > 3 else 0
		self.play(a, b)


	def play(self, button, extra_game_id=0):
		if(button == 1):
			pygame.mixer.music.load(data.MH_ONE_PROOF_OF_A_HERO)
		elif(button == 2):
			pygame.mixer.music.load(data.MH_DOS_PROOF_OF_A_HERO)
		elif(button == 3):
			pygame.mixer.music.load(data.MH_TRI_PROOF_OF_HERO)
		elif(button == 4 and extra_game_id == 1):
			pygame.mixer.music.load(data.MH_FOUR_PROOF_OF_HERO)
		elif(button == 4 and extra_game_id == 2):
			pygame.mixer.music.load(data.MHGU_PROOF_OF_HERO)
		elif(button == 5 and extra_game_id == 1):
			pygame.mixer.music.load(data.MH_WORLD_PROOF_OF_HERO)
		elif(button == 5 and extra_game_id == 2):
			pygame.mixer.music.load(data.MH_RISE_PROOF_OF_HERO)
		pygame.mixer.music.play(-1)

