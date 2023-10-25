
import pandas
from tkinter import *
import csv
from random import *
import time

BACKGROUND_COLOR = "#B1DDC6"
window=Tk()
window.title("Learn Japenese ")
window.config(pady=50,padx=50,bg=BACKGROUND_COLOR)
canvas=Canvas(width=800,height=526)
cimg=PhotoImage(file="images/card_front.png")
canvas.create_image(400,263,image=cimg)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
count=0
score=Label(text=f"Score : {count}",bg=BACKGROUND_COLOR,font="Times 20 italic bold")
score.place(x=20,y=0)
lifes=["❤️","❤️","❤️","❤️","❤️","❤️","❤️"]
life=Label(text=lifes,bg=BACKGROUND_COLOR,font="Times 20",fg="#D80032")
life.place(x=350,y=0)
correctFlag=True
def restart():
    global lifes
    global count
    global correctFlag
    correctFlag=True
    count=0
    lifes=["❤️","❤️","❤️","❤️","❤️","❤️","❤️"]
    score.config(text=f"Score : {count}",bg=BACKGROUND_COLOR)
    show()
instruction="""

-> Launch the game.

-> You will see a Japanese word presented as a question in the middle of the screen.

-> The word will have three components:

-> The Japanese word (in Kanji or Hiragana) at the top.

-> Its pronunciation in English (Romaji) in the middle.

-> Three possible English meanings at the bottom.

-> Your task is to match the Japanese word with the correct English meaning.

-> Click on the green tick button to reveal the correct answer.

-> If you're correct, a "Correct!" message will appear, and you'll earn points.

-> If you're wrong, a "Wrong!" message will appear, and you can try again.

-> The next Japanese word will appear after you press the green tick button.

-> Keep playing to test and improve your Japanese vocabulary.
"""


def new():
    global look
    global in_english
    global in_japenese
    global canvas
    global cimg
    canvas.delete('all')
    canvas=Canvas(width=800,height=526)
    cimg=PhotoImage(file="images/card_front.png")
    canvas.create_image(400,263,image=cimg)
    canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
    look=canvas.create_text(400,120,fill="green",font="Times 102 italic bold",text="")
    in_japenese=canvas.create_text(400,240,fill="black",font="Times 52 italic bold",text="")
    in_english=canvas.create_text(400,400,fill="blue",font="Times 65 italic bold",text="")
    canvas.grid(row=0,column=1,columnspan=2,pady=50)



#reading and getting data
def instructions():

    global instruction_text
    global look
    global in_english
    global in_japenese
    new()
    instruction_text=canvas.create_text(400, 230, fill="green", font="Times 13 italic bold", text=instruction)
data=pandas.read_csv("data.csv")


def show():
    global lifes
    global in_japenese


    new()
    chos=[40,530,291]
    shuffle(chos)



    english1=data["Translation"][randint(1,95)]
    english2=data["Translation"][randint(1,95)]
    chosen=randint(1,95)
    looks=data["Lemma"][chosen]
    english=data["Translation"][chosen]
    japanese=data["Pronunciation"][chosen]
    canvas.itemconfig(look,text=looks)
    canvas.itemconfig(in_japenese,text=japanese)
    #canvas.itemconfig(in_english,text=english)
    def correct():
        global correctFlag
        if correctFlag:
            window.config(bg="#186F65")
            life.config(text=lifes,bg="#186F65",font="Times 20",fg="#D80032")
            canvas.itemconfig(in_japenese,text="Correct")
            canvas.config(bg="#186F65")
            restart_button.config(bg="#186F65")
            right_button.config(bg="#186F65")
            instruction_button.config(bg="#186F65")
            global count
            count+=1

            score.config(text=f"Score : {count}",bg="#186F65")
            def blink():
                life.config(text=lifes,bg=BACKGROUND_COLOR,font="Times 20",fg="#D80032")
                window.config(bg=BACKGROUND_COLOR)
                canvas.config(bg=BACKGROUND_COLOR)
                score.config(text=f"Score : {count}",bg=BACKGROUND_COLOR)
                restart_button.config(bg=BACKGROUND_COLOR)
                right_button.config(bg=BACKGROUND_COLOR)
                instruction_button.config(bg=BACKGROUND_COLOR)
                show()
            window.after(600,blink)



    def incorrect():
            global count
            global lifes
            global in_japenese
            global correctFlag
            if len(lifes)==0:
                canvas.itemconfig(look,text=f"Final Score :{count}",font="Times 72 bold")
                canvas.itemconfig(in_japenese,text="GameOver!!!",fill="red",font="Times 35 bold")
                print("GameOver")
                correctFlag=False
               # in_japenese=canvas.create_text(400,240,fill="black",font="Times 52 italic bold",text="GAME OVER!!!")
            else:
                window.config(bg="#FF6969")
                canvas.config(bg="#FF6969")
                canvas.itemconfig(in_japenese,text="Incorrect")
                score.config(text=f"Score : {count}",bg="#FF6969")
                lifes.pop(len(lifes)-1)
                life.config(text=lifes,bg="#FF6969",font="Times 20",fg="white")
                restart_button.config(bg="#FF6969")
                right_button.config(bg="#FF6969")
                instruction_button.config(bg="#FF6969")
                def blink():
                    window.config(bg=BACKGROUND_COLOR)
                    canvas.config(bg=BACKGROUND_COLOR)
                    canvas.itemconfig(in_japenese,text=japanese)
                    life.config(text=lifes,bg=BACKGROUND_COLOR,font="Times 20",fg="#D80032")
                    score.config(text=f"Score : {count}",bg=BACKGROUND_COLOR)
                    restart_button.config(bg=BACKGROUND_COLOR)
                    right_button.config(bg=BACKGROUND_COLOR)
                    instruction_button.config(bg=BACKGROUND_COLOR)
                window.after(500,blink)

    opt1=Button(height=5,width=30,text=english2,command=incorrect, bg="#45474B", fg='#ffffff')
    opt1.place(x=chos[0],y=390)
    opt2=Button(height=5,width=30,text=english1,command=incorrect, bg="#45474B", fg='#ffffff')
    opt2.place(x=chos[1],y=390)
    opt3=Button(height=5,width=30,text=english,command=correct, bg="#45474B", fg='#ffffff')
    opt3.place(x=chos[2],y=390)

instruction_text = canvas.create_text(400, 230, fill="green", font="Times 13 italic bold", text=instruction)


#somthing=canvas.create_text(400,263,fill="green",font="Times 10 italic bold",text=instruction)


#canvas.create_text(400,280,fill="darkblue",font="Times 20 italic bold",text="Click the bubbles that are multiples of two.")
look=canvas.create_text(400,120,fill="green",font="Times 102 italic bold",text="")
in_japenese=canvas.create_text(400,240,fill="black",font="Times 52 italic bold",text="")
in_english=canvas.create_text(400,400,fill="blue",font="Times 65 italic bold",text="")
canvas.grid(row=0,column=1,columnspan=2,pady=50)

right_image=PhotoImage(file="images/right.png")
right_button=Button(image=right_image,highlightthickness=0,command=show,bg=BACKGROUND_COLOR)
right_button.grid(row=1,column=1,columnspan=2)


instruction_image=PhotoImage(file="images/instructionbutton.png")
instruction_button=Button( text="",font= ('Helvetica 15 bold'),compound="top", image=instruction_image,highlightthickness=0,bg=BACKGROUND_COLOR,command=instructions)
instruction_button.grid(row=1,column=2)

restart_image=PhotoImage(file="images/restart.png")
restart_button=Button(image=restart_image,highlightthickness=0,command=restart,bg=BACKGROUND_COLOR)
restart_button.grid(row=1,column=1)



window.mainloop()
