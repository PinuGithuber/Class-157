from tkinter import *
from PIL import ImageTk, Image
import random
root=Tk()

root.title("Pokemon")
root.geometry("600x400")

root.configure(background="yellow2")

abra=ImageTk.PhotoImage(Image.open("abra.jpg"))
bulb=ImageTk.PhotoImage(Image.open("bulbasour.jpg"))
button=ImageTk.PhotoImage(Image.open("button.jpg"))
char=ImageTk.PhotoImage(Image.open("charmender.jpg"))
iyv=ImageTk.PhotoImage(Image.open("iyvasour.jpg"))
jiggly=ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
kadabra=ImageTk.PhotoImage(Image.open("kadabra.jpg"))
meowth=ImageTk.PhotoImage(Image.open("meowth.jpg"))
nido=ImageTk.PhotoImage(Image.open("nidoking.jpg"))
paras=ImageTk.PhotoImage(Image.open("paras.jpg"))
persion=ImageTk.PhotoImage(Image.open("persion.jpg"))
pikachu=ImageTk.PhotoImage(Image.open("pikachu.jpg"))
ratata=ImageTk.PhotoImage(Image.open("ratata.jpg"))
squirtle=ImageTk.PhotoImage(Image.open("squirtle.jpg"))


player1 = Label(root, text = "Player 1", bg = "royal blue", fg = "white")
player1.place(relx = 0.1, rely= 0.3, anchor = CENTER)

player2 = Label(root, text = "Player 2", bg = "royal blue", fg = "white")
player2.place(relx = 0.9, rely= 0.3, anchor = CENTER)

player1score = Label(root, bg = "royal blue", fg = "white")
player1score.place(relx = 0.1, rely= 0.4, anchor = CENTER)

player2score = Label(root, bg = "royal blue", fg = "white")
player2score.place(relx = 0.9, rely= 0.4, anchor = CENTER)

rndice = Label(root, bg = "yellow", fg = "yellow")
rndice.place(relx = 0.5, rely= 0.5, anchor = CENTER)

pokedex=[abra, bulb, char, iyv, jiggly, kadabra, meowth, nido, paras, persion, pikachu, ratata, squirtle]
power=[30, 60, 50, 100, 70, 70, 60, 90, 40, 70, 200, 40, 50]

player1_score = 0
def player1():
    global player1_score
    random_no = random.randint(0, 12)
    ranpoke=pokedex[random_no]
    rndice["image"] = ranpoke
    rnpower = power[random_no]
    player1_score = player1_score + rnpower
    player1score["text"] = str(player1_score)
    
player_1_btn = Button(root, image = button, command = player1)
player_1_btn.place(relx = 0.1, rely = 0.6 , anchor =  CENTER)
    
player1_score = 0
def player2():
    global player2_score
    random_no = random.randint(0, 12)
    ranpoke=pokedex[random_no]
    rndice["image"] = ranpoke
    rnpower = power[random_no]
    player2_score = player1_score + rnpower
    player2score["text"] = str(player1_score)
    
player_2_btn = Button(root, image = button, command = player2)
player_2_btn.place(relx = 0.9, rely = 0.6 , anchor =  CENTER)
root.mainloop()
