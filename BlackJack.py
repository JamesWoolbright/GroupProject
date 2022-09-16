
from tkinter import *
import random

blackjack = Tk()
blackjack.withdraw()
exitcondition = True

def FORGET():
    playerscoretitle.place_forget()
    dealerscoretitle.place_forget()
    hit.place_forget()
    stand.place_forget()
    again.place(x=780, y=700)
    quit.place(x=845, y=835)

def FIRSTHIT():
    global playerscore
    global dealerscore
    playerscore = playerscore + int(random.choice(playerfirsthit))
    playerscorelabel.config(text=playerscore)
    hit1.place_forget()
    hit.place(x=500, y=800)
    dealerscore = dealerscore +int(random.choice(dealerfirsthit))
    dealerscorelabel.config(text=dealerscore)
    stand.config(state=NORMAL)

def HIT():
    global playerscore
    global dealerscore
    playerscore = playerscore + int(random.choice(playerhit))
    playerscorelabel.config(text=playerscore)
    if dealerscore < 17:
        dealerscore = dealerscore +int(random.choice(dealerfirsthit))
        dealerscorelabel.config(text=dealerscore)
    if playerscore == 21 and dealerscore < 21 or dealerscore == 21 and playerscore < 21:
        BLACKJACK()
    if playerscore > 21 and dealerscore <= 21 or playerscore <= 21 and dealerscore > 21:
        BUST()
    if playerscore == 21 and dealerscore == 21 or playerscore > 21 and dealerscore > 21:
        PUSH()

def BLACKJACK():
    bjtitle.config(text='BLACKJACK', bg='black', fg='white')
    FORGET()
    if playerscore == 21 and dealerscore < 21:
        WIN()
    if dealerscore == 21 and playerscore < 21:
        LOSE()

def BUST():
    bjtitle.config(text='BUST!', bg='black', fg='white')
    if playerscore > 21 and dealerscore <= 21:
        LOSE()
    if playerscore <= 21 and dealerscore > 21:
        WIN()

def PUSH():
    bjtitle.config(text='PUSH!', bg='black', fg='white')
    winloselabel.config(text='ITS A TIE!', bg='blue', fg='white')
    winloselabel.pack()
    FORGET()

def STAND():
    global dealerscore
    global playerscore
    while dealerscore < 17:
        dealerscore = dealerscore +int(random.choice(dealerfirsthit))
        dealerscorelabel.config(text=dealerscore)
    if playerscore == 21 and dealerscore < 21 or dealerscore == 21 and playerscore < 21:
        BLACKJACK()
    if playerscore > 21 and dealerscore <= 21 or playerscore <= 21 and dealerscore > 21:
        BUST()
    if playerscore == 21 and dealerscore == 21 or playerscore > 21 and dealerscore > 21 or playerscore == dealerscore:
        PUSH()
    if playerscore > dealerscore and playerscore < 21:
        WIN()
    if dealerscore > playerscore and dealerscore < 21:
        LOSE()

def WIN():
    global winloselabel
    winloselabel.config(text='YOU WIN!', bg='gold')
    winloselabel.pack()
    FORGET()

def LOSE():
    global winloselabel
    winloselabel.config(text='YOU LOSE!', bg='red')
    winloselabel.pack()
    FORGET()

def AGAIN():
    global playerscore
    global dealerscore
    playerscore = 0
    dealerscore = 0
    playerscorelabel.config(text=dealerscore)
    dealerscorelabel.config(text=dealerscore)
    bjtitle.config(text='Blackjack', bg='green', fg='black')
    winloselabel.pack_forget()
    hit1.place(x=500, y=800)
    stand.place(x=1100, y=800)
    again.place_forget()
    quit.place_forget()
    playerscoretitle.place(x=460, y=220)
    dealerscoretitle.place(x=1000, y=220)
    stand.config(state=DISABLED)

def EXIT():
    blackjack.withdraw()
    global exitcondition
    exitcondition = True

def PLAY():
    blackjack.deiconify()
    global exitcondition
    exitcondition = False

#sets up root window

#Sets up Blackjack window
blackjack.attributes('-fullscreen', True)
blackjack.config(bg='green')
exit = Button(blackjack, text='exit', bg='red', font='Arial, 20', command=EXIT)
exit.place(x=0,y=0)
bjtitle = Label(blackjack, text='Blackjack', font='Arial, 70', bg='green')
bjtitle.pack()
hit1 = Button(blackjack, text='  Hit  ', bg='grey', font='Arial, 50', command=FIRSTHIT)
hit1.place(x=500, y=800)
hit = Button(blackjack, text='  Hit  ', bg='grey', font='Arial, 50', command=HIT)
stand = Button(blackjack, text='Stand', bg='grey', font='Arial, 50', command=STAND)
stand.place(x=1100, y=800)
stand.config(state=DISABLED)
playerscoretitle = Label(blackjack, text='Your Score', font='Arial, 50', bg='green', fg='white')
playerscoretitle.place(x=460, y=220)
dealerscoretitle = Label(blackjack, text='Dealer Score', font='Arial, 50', bg='green', fg='white')
dealerscoretitle.place(x=1000, y=220)
playerscore = 0
dealerscore = 0
playerscorelabel = Label(blackjack, text=playerscore, font='Arial, 150', bg='green')
playerscorelabel.place(x=550, y=450)
dealerscorelabel = Label(blackjack, text= dealerscore, font='Arial, 150', bg='green')
dealerscorelabel.place(x=1150, y=450)
winloselabel = Label(blackjack, font='Arial, 50')
again = Button(blackjack, text='Play Again', bg='lime', font='Arial, 50', command=AGAIN)
quit = Button(blackjack, text='  Quit  ', bg='red', font='Arial, 50', command=EXIT)

#random values
playerfirsthit = ['2','3','4','5','6','7','8','9','10', '10', '10', '10', '11']
dealerfirsthit = ['2','3','4','5','6','7','8','9','10', '10', '10', '10', '11']
playerhit = ['1', '2','3','4','5','6','7','8','9','10', '10', '10', '10']
dealerhit = ['1', '2','3','4','5','6','7','8','9','10', '10', '10', '10']

while exitcondition == False:
    blackjack.update()