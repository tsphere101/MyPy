from tkinter import *


root = Tk()

accum = 0

def button_handler_sum(entry:Entry,label:Label):
    global accum
    try:
        val = int(entry.get())
    except :
        val = 0
    print(val)
    accum+= val
    label['text'] = "sum is " + str(accum)

label_welcome = Label(root,text = "Hello!")
label_descrb = Label(root,text = "Please enter your name")
entry = Entry(root,width= 50,bg = '#f9edee',borderwidth=2)
button_summit = Button(root,text="submit",command = lambda : button_handler_sum(entry,label_result))
label_result = Label(root,text = "")




label_welcome.grid(row = 0,column = 0)
label_descrb.grid(row = 1,column = 0)
entry.grid(row=1,column = 1)
button_summit.grid(row = 1,column = 2)
label_result.grid(row = 2,column=0)



root.mainloop()