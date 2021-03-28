from tkinter import *
import time
root = Tk()

root.geometry("250x200")




def quit():
    root.quit()
    

    
def clock():
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    seconds = time.strftime("%S")   
    my_clock.config(text=hour + ":" + minute + ":" + seconds)
    
def ticking():
    my_clock.after(1000,clock)
    start.after(1000, ticking)


    
    
    
explaination = Label(root, text='Alarm Clock', fg="grey")
explaination.grid(row=2,column=15,columnspan=1)

start = Button(text='START', width=5,height=3, command=ticking)
start.grid(row=4, column=17,columnspan=2)

stop = Button(text='STOP',width=5, height=3,command=quit)
stop.grid(row=4,column=2)

my_clock = Label(root, text="")
my_clock.grid(row=4, column=14, columnspan=3) 

# ticking()











root.title('Alarm Clock')

root.mainloop()