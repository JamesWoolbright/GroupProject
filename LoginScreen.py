import multiprocessing
import winsound
from tkinter import *
from PIL import Image,ImageTk
import random
import time
import RockPaperScissors
import BlackJack
import TicTacToe


x1 = 0
y1 = 0
a1 = 0.01
a2 = 0.01
def Exit():
    global t
    t = False
    global GlobalLoop
    GlobalLoop = False
def Odvd():
    global t
    t = False
    global dvdActive
    dvdActive = True
    Top1.deiconify()
    root.withdraw()
def Osoundalbum():
    global soundActive
    soundActive = True
    global t
    t = False
    Top2.deiconify()
    root.withdraw()
def backtologin():
    winsound.PlaySound(None, winsound.SND_PURGE)
    global t
    global y1
    global dvdActive
    global x1
    global soundActive
    soundActive = False
    x1 = 0
    y1 = 0
    t = True
    dvdActive = False
    Top1.withdraw()
    Top2.withdraw()
    root.deiconify()
        
def Oblackjack():
    global t
    t = False
    BlackJack.PLAY()
    t = True
def Otictactoe():
    global t
    t = False
    TicTacToe.main()
    t = True
def Orockpaperscissors():
    global t
    t = False
    RockPaperScissors.Start()
    RockPaperScissors.main()
    t = True 
def Sound1Clicked():
    winsound.PlaySound('Group Project\\Never Gonna Give You Up Original.wav', winsound.SND_ASYNC)
def Sound2Clicked():
    winsound.PlaySound('Group Project\\RainSounds.wav', winsound.SND_ASYNC)
def Sound3Clicked():
    winsound.PlaySound('Group Project\\Wilhelm scream.wav', winsound.SND_ASYNC)
def Sound4Clicked():
    winsound.PlaySound('Group Project\\DopplerEffect.wav', winsound.SND_ASYNC)
def Sound5Clicked():
    winsound.PlaySound('Group Project\\Doh.wav', winsound.SND_ASYNC)

def main():
    while GlobalLoop == True:
        root.update()
        while soundActive == True:
            root.update()
            Top2.focus_force()
        while dvdActive == True:
            global x1
            global y1
            global a1
            global a2
            root.update()
            Top1.focus_force()
            x1 += a1
            y1 += a2
            img.place(x=x1, y=y1)
            if x1 > 1700:
                x1 = 1700
                a1 = -.01

            if x1 < 0:
                x1 = 0
                a1 = .01
                
            if y1 > 900:
                y1 = 900
                a2 = -.01
                
            if y1 < 0:
                y1 = 0
                a2 = .01
        while t == True:
            root.update()
            if colorPalete == 0:
                italycolor = italy[random.randrange(0,5)]
                root.config(bg=italycolor)
                Title.config(bg=italycolor)
                time.sleep(0.6)
            else:
                bluetogreenColor = bluetogreen[random.randrange(0,9)]
                root.config(bg=bluetogreenColor)
                Title.config(bg=bluetogreenColor)
                time.sleep(0.6)

if __name__ == "__main__":


    soundActive = False
    GlobalLoop = True
    dvdActive = False
    t = True

    root = Tk()
    root.attributes('-fullscreen', True)
    italy = ['#008961','#00976B','#00A676','#F7F9F9','#E0D0C1','#A76D60']
    bluetogreen = ['#7400B8','#6930C3','#5E60CE','#5390D9','#4EA8DE','#48BFE3','#56CFE1','#64DFDF','#72EFDD','#80FFDB']
    colorPalete = random.randrange(0,2)

    Title = Label(root, text="CFA", font=("Roboto", 24))
    Title.pack()


    exitbutton = Button(root, text="Exit to Desktop", command=Exit)
    exitbutton.place(x=900, y=800)
    rockpaperscissors = Button(root,text="Open Rock Paper Scissors", command=Orockpaperscissors)
    rockpaperscissors.place(x=900, y=300)
    ticTacToe = Button(root, text="Open TicTacToe", command=Otictactoe)
    ticTacToe.place(x=900, y=700)

    BlackJackbutton = Button(root, text="Open Black Jack", command=Oblackjack)
    BlackJackbutton.place(x=900, y=600)

    Dvd = Button(root, text="Open Dvd", command=Odvd)
    Dvd.place(x=900, y=500)

    SoundAlbum = Button(root, text="Open SoundAlbum", command=Osoundalbum)
    SoundAlbum.place(x=900, y=400)

    Top1 = Toplevel()
    Top1.withdraw()
    Top1.attributes("-fullscreen", True)
    Top1.bind("<space>", lambda e: backtologin())

    load1 = Image.open('C:\\Users\\jrwoolbright\\.vscode\\Projects\\Group Project\\Dvd logo.png')
    render = ImageTk.PhotoImage(load1)
    img = Label(Top1, image=render)
    img.place(x=0, y=0)

    Top2 = Toplevel()
    Top2.withdraw()
    Top2.attributes("-fullscreen", True)
    Top2.bind("<space>", lambda e: backtologin())

    Sound1 = Button(Top2, text='Click me for good music',command=Sound1Clicked)
    Sound2 = Button(Top2, text='Play Rain Sounds', command=Sound2Clicked)
    Sound3 = Button(Top2, text='Play Wilhelm Scream', command=Sound3Clicked)
    Sound4 = Button(Top2, text='Play Car Doppler Effect', command= Sound4Clicked)
    Sound5 = Button(Top2, text='Play Doh', command=Sound5Clicked)

    Sound1.place(x=900, y=350)
    Sound2.place(x=900, y=450)
    Sound3.place(x=900, y=550)
    Sound4.place(x=900, y=650)
    Sound5.place(x=900, y=750)

    main()

