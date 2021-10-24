from tkinter import *


root = Tk()


number_of_clicks = 0

def my_click():
    global number_of_clicks
    number_of_clicks+=1
    print(number_of_clicks)
    label_number_of_click['text'] = str(number_of_clicks)




label_name = Label(root, text = 'This is the button!')
label_number_of_click = Label(root,text = str(number_of_clicks))
my_button = Button(root,text = "Click me!", padx = 45,command = my_click,bg='#faafac')




label_name.pack()
label_number_of_click.pack()
my_button.pack()

root.mainloop()