from  tkinter import *  #for gui
import os

def fun1():
    
    os.system("py Motion_Detection3.py")
    
    
def fun2():
    
    os.system("py user_details.py")

screen=Tk() 
screen.title("MOTION DETECTION") 
screen.geometry("1000x750")

#buttons
btn=Button(screen, text='Start Tracking',font='Times 16 bold',width=35,height=4,bg='brown',fg='white',command = fun1)
btn1=Button(screen, text='Target Email',font='Times 16 bold',width=35,height=4,bg='brown',fg='white',command = fun2)
#placing
btn.pack(pady=50)
btn1.pack(pady = 50)
screen.mainloop()
