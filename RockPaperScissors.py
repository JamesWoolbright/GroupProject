import random
import tkinter as tk
 
window = tk.Tk()
window.withdraw()
window.attributes("-fullscreen", True)
window.title('Rock Paper Scissors')
window.config(bg='black')
 
message = tk.Label(window,text='Welcome to Rock Paper Scissors. Choose one of the options to start.')
message.place(x=165, y=20)
message.config(bg='pink', font=('Comic Sans Ms', 10, 'bold'))
 
USER_SCORE = 0
COMP_SCORE = 0
USER_CHOICE = ""
COMP_CHOICE = ""
 
 
 
 
def choice_to_number(choice):
    rps = {'rock':0,'paper':1,'scissor':2}
    return rps[choice]
def number_to_choice(number):
    rps={0:'rock',1:'paper',2:'scissor'}
    return rps[number]
 
def random_computer_choice():
    return random.choice(['rock','paper','scissor'])
tielabel = tk.Label(window, text="",bg="black",fg="white")
tielabel.place(x=300, y=150)
def result(human_choice,comp_choice):
    global USER_SCORE
    global COMP_SCORE
    user=choice_to_number(human_choice)
    comp=choice_to_number(comp_choice)
    if(user==comp):
        tielabel.config(text="You have tied")
    elif((user-comp)%3==1):
        tielabel.config(text="")
        USER_SCORE+=1
    else:
        tielabel.config(text="")
        COMP_SCORE+=1
    text_area = tk.Text(window,height=12,width=30,bg="#FFFF99")
    text_area.place(x=300,y=250)
    answer = "Your Choice: {uc} \nComputer's Choice : {cc} \n Your Score : {u} \n Computer Score : {c} ".format(uc=USER_CHOICE,cc=COMP_CHOICE,u=USER_SCORE,c=COMP_SCORE)    
    text_area.insert(tk.END,answer)
 
def rock():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='rock'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)
def paper():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='paper'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)
def scissor():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='scissor'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)
 
button1 = tk.Button(window,text="       Rock       ",bg="skyblue",command=rock)
button1.place(x=100, y=200)
button2 = tk.Button(window,text="       Paper      ",bg="pink",command=paper)
button2.place(x=100, y=300)
button3 = tk.Button(window,text="      Scissor     ",bg="lightgreen",command=scissor)
button3.place(x=100, y=400)

 
t1 = False
def Start():
    global t1
    t1 = True
    window.deiconify()
def Stop():
    global t1
    t1 = False
    window.withdraw()
exitbutton = tk.Button(window,bg="white",text="exit", command=Stop)
exitbutton.place(x=100, y=500)
def main():
    while t1 == True:
        window.update()