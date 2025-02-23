# import the module that allows me to create a python window
import tkinter
import random
# creating the tkinter window
window = tkinter.Tk()
window.geometry("1080x720")
window.resizable(False,False)
window.title("Rock paper scisor")
# usuefull variables
vicotry_count=0
deafeat_count=0
draw_count=0
player_move=""
computer_move=""
historic_of_move=[]
list_of_move= ["paper","rock","scissors"]
# define all the functions that i will need
def computer_move_choice():
    global  computer_move
    what_to_do= random.randint(1,4)
    if what_to_do== 1 or what_to_do== 2 or historic_of_move.__len__()==0:
        computer_move= random.choice(list_of_move)
    else:
        p=0
        s=0
        r=0
        if  historic_of_move.__len__()<10:
            for x in historic_of_move:
                if x== "paper":
                    p+=1
                elif x== "rock":
                    r+=1
                else:
                    s+=1
        else:
            last_nine = historic_of_move[-9:]
            for x in last_nine:
                if x == "paper":
                    p += 1
                elif x == "rock":
                    r += 1
                else:
                    s += 1
        if p >s and p> r:
            computer_move== "scissors"
        elif s >p and s> r:
            computer_move="rock"
        elif r>p and r >s:
            computer_move="paper"
        else:
            computer_move = random.choice(list_of_move)

def rock():
    global historic_of_move
    global player_move
    player_move= "rock"
    historic_of_move.append(player_move)
    computer_move_choice()
    detect_win(player_move, computer_move)

def paper():
    global historic_of_move
    global player_move
    player_move="paper"
    historic_of_move.append(player_move)
    computer_move_choice()
    detect_win(player_move, computer_move)


def scissor():
    global historic_of_move
    global player_move
    player_move="scissors"
    historic_of_move.append(player_move)
    computer_move_choice()
    detect_win(player_move, computer_move)

def Quit():
    window.quit()
def reset():
    vicotry_count=0
    deafeat_count=0
    draw_count=0
    victor_label.config(text=f"Victory: {vicotry_count}")
    defeat_label.config(text=f"Defeat: {deafeat_count}")
    draw_label.config(text=f"Draw: {draw_count}")
    game = tkinter.Label(window, text=f"Game: {vicotry_count + deafeat_count + draw_count}", font=("Helvetica", 12))
    game.place(x=20, y=20)
def do_nothing():
    pass
def create_button(window=window,text="",bg="white",activebackground="white",command=do_nothing,xPos=0,yPos=0):
    button= tkinter.Button(window,text=text,bg=bg,activebackground=activebackground,command=command)
    button.place(x=xPos,y=yPos)
def detect_win(Pmove,Cmove):
    global  deafeat_count
    global vicotry_count
    global  draw_count
    if Cmove== Pmove:
        draw_count+=1

    elif Cmove == "rock" and Pmove == "scissors":
        deafeat_count+=1
    elif  Cmove == "rock" and Pmove == "paper":
        vicotry_count+=1

    elif Cmove == "paper" and Pmove =="rock":
        deafeat_count+=1
    elif Cmove == "paper" and Pmove == "scissors":
        vicotry_count+=1

    elif Cmove == "scissors" and Pmove == "paper":
        deafeat_count+=1
    elif Cmove == "scissors" and Pmove == "rock":
        vicotry_count+=1
    # Update labels
    victor_label.config(text=f"Victory: {vicotry_count}")
    defeat_label.config(text=f"Defeat: {deafeat_count}")
    draw_label.config(text=f"Draw: {draw_count}")
    game = tkinter.Label(window,text= f"Game: {vicotry_count+deafeat_count+draw_count}",font=("Helvetica",12))
    game.place(x=20,y=20)
#create the player's and computer's frame
player_frame= tkinter.Frame(window,bg="blue",width=300,height=450)
player_frame.place(x=80,y=125)
computer_frame = tkinter.Frame(window,bg="blue",width=300,height=450)
computer_frame.place(x=700,y=125)
#creation of the diffrent buttons in the game
create_button(window,"ROCK","blue","red",rock,100,620)
create_button(window,"PAPER","blue",None,paper,200,620)
create_button(window,"SCISSORS","blue",None,scissor,300,620)
create_button(window,"RESET","green","red",reset,800,620)
create_button(window,"QUIT","gray","red",Quit,880,620)

#creation of all my labels

victor_label=tkinter.Label(window,text= f"Victory: {vicotry_count}",font=("Helvetica",12))
defeat_label=tkinter.Label(window,text= f"Defeat: {deafeat_count}",font=("Helvetica",12))
draw_label= tkinter.Label(window,text= f"Draw: {draw_count}",font=("Helvetica",12))
victor_label.place(x=370,y=20)
defeat_label.place(x=630,y=20)
draw_label.place(x=500,y=20)
player_label=tkinter.Label(window,text="Player:" ,font=("Helvetica",15))
player_label.place(x=200,y=80)
Computer_label=tkinter.Label(window,text="Computer:" ,font=("Helvetica",15))
Computer_label.place(x=820,y=80)

window.mainloop()