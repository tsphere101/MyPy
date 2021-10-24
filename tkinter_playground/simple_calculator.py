from tkinter import *


class Main:
    def __init__(self):
        self.root = Tk()
        self.root.title("Simple Calculator")
        self.root.geometry('400x600')


        # Widgets
        self.entry_value = StringVar()
        self.entry = Entry(self.root,width = 10,textvariable=self.entry_value,state='disable',font=('K2D ExtraLight',40),justify='right',borderwidth=0,bg="#f0f0f0",disabledforeground='#1a1a1a')
        self.entry_value.set("0")

        # Config grid column rows
        for i in range(4):
            Grid.columnconfigure(self.root,i,weight=1)

        for i in range(7):
            Grid.rowconfigure(self.root,i,weight=1)
        # Grid them to the screen
        self.entry.grid(row=0,column=0,columnspan=5,sticky='we',ipady=50,padx=15)
        # self.entry.pack()




        # Buttons
        self.__init_button()

    def __init_button(self):
        self.number_buttons =[]
        NUMBER = '0123456789'
        self.number_buttons.append(Button(text= str(0),font=('K2D ExtraLight',30),borderwidth=1,command = lambda : self.handler_number_button(0)))
        self.number_buttons.append(Button(text= str(1),font=('K2D ExtraLight',30),borderwidth=1,command = lambda : self.handler_number_button(1)))
        self.number_buttons.append(Button(text= str(2),font=('K2D ExtraLight',30),borderwidth=1,command = lambda : self.handler_number_button(2)))
        self.number_buttons.append(Button(text= str(3),font=('K2D ExtraLight',30),borderwidth=1,command = lambda : self.handler_number_button(3)))
        self.number_buttons.append(Button(text= str(4),font=('K2D ExtraLight',30),borderwidth=1,command = lambda : self.handler_number_button(4)))
        self.number_buttons.append(Button(text= str(5),font=('K2D ExtraLight',30),borderwidth=1,command = lambda : self.handler_number_button(5)))
        self.number_buttons.append(Button(text= str(6),font=('K2D ExtraLight',30),borderwidth=1,command = lambda : self.handler_number_button(6)))
        self.number_buttons.append(Button(text= str(7),font=('K2D ExtraLight',30),borderwidth=1,command = lambda : self.handler_number_button(7)))
        self.number_buttons.append(Button(text= str(8),font=('K2D ExtraLight',30),borderwidth=1,command = lambda : self.handler_number_button(8)))
        self.number_buttons.append(Button(text= str(9),font=('K2D ExtraLight',30),borderwidth=1,command = lambda : self.handler_number_button(9)))
        
        self.operators_buttons = []
        self.operators_buttons.append(Button(text = '+',font=('K2D ExtraLight',30),borderwidth=1,command = lambda : self.handler_operator_button('+')))
        self.operators_buttons.append(Button(text = '-',font=('K2D ExtraLight',30),borderwidth=1,command = lambda : self.handler_operator_button('-')))
        self.operators_buttons.append(Button(text = 'x',font=('K2D ExtraLight',30),borderwidth=1,command = lambda : self.handler_operator_button('*')))
        self.operators_buttons.append(Button(text = '/',font=('K2D ExtraLight',30),borderwidth=1,command = lambda : self.handler_operator_button('/')))
        self.operators_buttons.append(Button(text= '=', font=('K2D ExtraLight',30),borderwidth=1,command = lambda : self.handler_operator_button('=')))
        self.operators_buttons.append(Button(text= '<', font=('K2D ExtraLight',30),borderwidth=1,command = lambda : self.handler_operator_button('<')))
        self.operators_buttons.append(Button(text= 'C', font=('K2D ExtraLight',30),borderwidth=1,command = lambda : self.handler_operator_button('C')))

        # Border Color Config
        for button in self.number_buttons:
            button.config(borderwidth=1,relief=RIDGE)

        for button in self.operators_buttons:
            button.config(borderwidth=1,relief=RIDGE)


        # Numbers Button
        padx_val = 0
        self.number_buttons[7].grid(row=3,column=0,sticky='nswe',padx=padx_val)
        self.number_buttons[8].grid(row=3,column=1,sticky='nswe',padx=padx_val)
        self.number_buttons[9].grid(row=3,column=2,sticky='nswe',padx=padx_val)

        self.number_buttons[4].grid(row=4,column=0,sticky='nswe',padx=padx_val)
        self.number_buttons[5].grid(row=4,column=1,sticky='nswe',padx=padx_val)
        self.number_buttons[6].grid(row=4,column=2,sticky='nswe',padx=padx_val)

        self.number_buttons[1].grid(row=5,column=0,sticky='nswe',padx=padx_val)
        self.number_buttons[2].grid(row=5,column=1,sticky='nswe',padx=padx_val)
        self.number_buttons[3].grid(row=5,column=2,sticky='nswe',padx=padx_val)

        self.number_buttons[0].grid(row=6,column=1,sticky='nswe',padx=padx_val)

        # Operators Buttons
        self.operators_buttons[0].grid(row=5,column=3,sticky='nswe',padx=padx_val)
        self.operators_buttons[1].grid(row=4,column=3,sticky='nswe',padx=padx_val)
        self.operators_buttons[2].grid(row=3,column=3,sticky='nswe',padx=padx_val)
        self.operators_buttons[3].grid(row=2,column=3,sticky='nswe',padx=padx_val)
        self.operators_buttons[4].grid(row=6,column=3,sticky='nswe',padx=padx_val)
        self.operators_buttons[5].grid(row=1,column=3,sticky='nswe',padx=padx_val)
        self.operators_buttons[6].grid(row=1,column=2,sticky='nswe',padx=padx_val)


            
    
    def handler_number_button(self,num):
        value = self.entry_value.get()
        if value == '0':
            value = str(num)
        else:
            value+=str(num)
        self.entry_value.set(value)

    def handler_operator_button(self,op):
        if op == 'C':
            self.entry_value.set('0')
        elif op == '<':
            value = self.entry_value.get()
            if value != '0' :
                self.entry_value.set(value[:-1])

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    main = Main()
    main.run()