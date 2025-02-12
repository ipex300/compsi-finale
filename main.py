import tkinter
window = tkinter.Tk()
window.geometry("1080x720")
window.resizable(False,False)

def do_nothing():
    pass
def create_button(window=window,text="",bg="white",activebackground="white",command=do_nothing,xPos=0,yPos=0):
    button= tkinter.Button(window,text=text,bg=bg,activebackground=activebackground,command=command)
    button.place(x=xPos,y=yPos)

player_frame= tkinter.Frame(window,bg="blue",width=300,height=450)
player_frame.place(x=80,y=105)
computer_frame = tkinter.Frame(window,bg="blue",width=300,height=450)
computer_frame.place(x=700,y=105)

create_button(window,"ROCK","blue")
create_button(window,"PAPER","blue")
create_button(window,"SCISSORS","blue")

quit = tkinter.Button(window)
reset = tkinter.Button(window   )


window.mainloop()
