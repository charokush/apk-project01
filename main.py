import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import os
import random
os.environ['XDG_RUNTIME_DIR'] = '/run/user/0'


kivy.require('1.9.0')


class MyRoot(BoxLayout):
	def __init__(self):
		super(MyRoot,self).__init__()

	def generate_number(self):
		self.random_label.text=str(random.randint(0,1000))

class NeuralRandom(App):
	def build(self):
		return MyRoot()

neuralRandom=NeuralRandom()
neuralRandom.run()


"""from tkinter import *
from tkinter import messagebox
import base64
import os

def main_screen():
	screen=Tk()
	screen.geometry("375x398")

	image_icon=PhotoImage(file="hero.png")
	screen.iconphoto(False,image_icon)
	screen.title("PctApp")

	def reset():
		code.set("")
		text1.delete(1.0,END)

	Label(text="Enter text for decryption and encrytion",fg="black", font=("calbri",13)).place(x=10,y=10)
	text1=Text(font="Robote 20",bg = "white",relief=GROOVE,wrap=WORD,bd=0)
	text1.place(x=10,y=50, width=355,height=100)
	Label(text="Enter text for decryption and encrytion",fg="black", font=("calbri",13)).place(x=10,y=170)
	code=StringVar()
	Entry(textvariable=code, width=19,bd=0,font=("arial",25),show="*").place(x=10,y=200)

	Button(text="ENCRYPT",height="2",width=23,bg="#ed3833",fg="white",bd=0).place(x=10,y=250)
	Button(text="ENCRYPT",height="2",width=23,bg="#00bd56",fg="white",bd=0).place(x=200,y=250)
	Button(text="RESET",height="2",width=50,bg="#1089ff",fg="white",bd=0,command=reset).place(x=10,y=300)
	screen.mainloop()






main_screen()"""