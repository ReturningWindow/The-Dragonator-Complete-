import tkinter
from PIL import ImageTk
from PIL import Image
import tkinter.messagebox
import pygame
import random
import data
import Log.metal_logger as log

class Dragonator:

    def __init__(self):
        self.window = self.setup_window()
        self.frames = self.setup_frames(self.window)
        self.images = [ImageTk.PhotoImage(Image.open(i)) for i in data.images]
        self.labels = self.setup_labels(self.frames, self.images)
        self.SONG_LIMIT = 7
        self.setup_home()
        self.setup_fourth_gen()
        self.setup_fifth_gen()
        self.window.mainloop()
    
    def setup_window(self):
        pygame.mixer.init()
        window = tkinter.Tk()
        window.title("The Dragonator v{}".format(data.VERSION))
        image = tkinter.PhotoImage(file=data.ICON)
        window.iconphoto(False, image)
        window.geometry("620x210")
        window.resizable(0, 0)
        return window

    def setup_frames(self, window, bg="gray"):
        frames = [tkinter.Frame(window, bg=bg) for i in range(3)]
        for items in frames:
            items.grid(row=0, column=0, sticky="nsew")
        frames[0].tkraise()
        log.log.debug("Frames Created")
        return frames

    def setup_labels(self, frames, images):
        labels = [
            tkinter.Label(frames[0], text="Welcome!", bg="red"),
            tkinter.Label(frames[1], text="Gen 4"),
            tkinter.Label(frames[2], text="Gen 5"),
            tkinter.Label(frames[0], image=images[0]),
            tkinter.Label(frames[1], image=images[1]), tkinter.Label(frames[1], image=images[2]),
            tkinter.Label(frames[2], image=images[3]), tkinter.Label(frames[2], image=images[4]),
        ]
        labels[0].grid(row=0, column=0)
        labels[0].config(text="Pick a generation")
        log.log.debug("Created Labels")
        return labels

    def setup_home(self):
        self.labels[3].grid(row=0, column=1, padx=3)
        button1 = tkinter.Button(self.frames[0], text="Gen 1", command=lambda:self.play(1))
        button2 = tkinter.Button(self.frames[0], text="Gen 2", command=lambda:self.play(2))
        button3 = tkinter.Button(self.frames[0], text="Gen 3", command=lambda:self.play(3))
        button4 = tkinter.Button(self.frames[0], text="Gen 4", command=lambda:self.frames[1].tkraise())
        button5 = tkinter.Button(self.frames[0], text="Gen 5", command=lambda: self.frames[2].tkraise())
        random_button = tkinter.Button(self.frames[0], text="Wildcard", command=lambda: self.wildcard())
        button1.grid(row=0, column=3, padx=2)
        button2.grid(row=0, column=4, padx=2)
        button3.grid(row=0, column= 6)
        button4.place(x=320, y=120)
        button5.place(x=370, y=120)
        random_button.place(x=420, y=120)

    def setup_fourth_gen(self):
        self.labels[1].pack()
        self.labels[4].pack(side=tkinter.LEFT)
        self.labels[5].pack(side=tkinter.LEFT)
        button1 = tkinter.Button(self.frames[1], text="MH4U", command=lambda:self.play(4))
        button2 = tkinter.Button(self.frames[1], text="MHGU", command=lambda:self.play(5))
        button3 = tkinter.Button(self.frames[1], text="Back", command=lambda:self.frames[0].tkraise())
        button1.pack()
        button2.pack()
        button3.pack(fill=tkinter.BOTH)

    def setup_fifth_gen(self):
        self.labels[2].pack()
        self.labels[6].pack(side=tkinter.LEFT)
        self.labels[7].pack(side=tkinter.LEFT)
        button1 = tkinter.Button(self.frames[2], text="MHW", command=lambda:self.play(6))
        button2 = tkinter.Button(self.frames[2], text="MHR", command=lambda:self.play(7))
        button3 = tkinter.Button(self.frames[2], text="Back", command=lambda:self.frames[0].tkraise())
        button1.pack()
        button2.pack()
        button3.pack(fill=tkinter.BOTH)


    def wildcard(self):
        self.play(random.randint(1, self.SONG_LIMIT))

    def play(self, button):
        pygame.mixer.music.load(data.tracks[button-1])
        pygame.mixer.music.play(-1)
