from tkinter import *
import hashlib
import tkinter.messagebox
import res.Ency as Ency


class Main:
    def __init__(self):
        self.ency = None
        self.key_used = False
        self.root = Tk()
        self.root.title("Encrypted Vault")
        self.root.geometry('300x450')
        self.root.iconbitmap("res/icon.ico")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.font_style = 'K2D ExtraLight'

        # Widgets
        self.entry_value = StringVar()
        self.entry_data_value = ''
        self.entry = Entry(self.root, width=10, textvariable=self.entry_value, state='disable', font=(
            'K2D ExtraLight', 40), justify='center', borderwidth=0, bg="#f0f0f0", disabledforeground='#1a1a1a')
        self.entry_value.set('')

        # Config grid column rows
        for i in range(3):
            Grid.columnconfigure(self.root, i, weight=1)

        for i in range(7):
            Grid.rowconfigure(self.root, i, weight=1)
        # Grid them to the screen
        self.entry.grid(row=0, column=0, columnspan=5,
                        sticky='we', ipady=50, padx=15)
        # self.entry.pack()

        # Buttons
        self.__init_button()

    def __init_button(self):
        self.number_buttons = []
        NUMBER = '0123456789'
        self.number_buttons.append(Button(text=str(0), font=(
            self.font_style, 30), borderwidth=1, command=lambda: self.handler_button('0')))
        self.number_buttons.append(Button(text=str(1), font=(
            self.font_style, 30), borderwidth=1, command=lambda: self.handler_button('1')))
        self.number_buttons.append(Button(text=str(2), font=(
            self.font_style, 30), borderwidth=1, command=lambda: self.handler_button('2')))
        self.number_buttons.append(Button(text=str(3), font=(
            self.font_style, 30), borderwidth=1, command=lambda: self.handler_button('3')))
        self.number_buttons.append(Button(text=str(4), font=(
            self.font_style, 30), borderwidth=1, command=lambda: self.handler_button('4')))
        self.number_buttons.append(Button(text=str(5), font=(
            self.font_style, 30), borderwidth=1, command=lambda: self.handler_button('5')))
        self.number_buttons.append(Button(text=str(6), font=(
            self.font_style, 30), borderwidth=1, command=lambda: self.handler_button('6')))
        self.number_buttons.append(Button(text=str(7), font=(
            self.font_style, 30), borderwidth=1, command=lambda: self.handler_button('7')))
        self.number_buttons.append(Button(text=str(8), font=(
            self.font_style, 30), borderwidth=1, command=lambda: self.handler_button('8')))
        self.number_buttons.append(Button(text=str(9), font=(
            self.font_style, 30), borderwidth=1, command=lambda: self.handler_button('9')))

        self.operator_buttons = []
        self.operator_buttons.append(Button(text='X', font=(
            self.font_style, 20), borderwidth=1, command=lambda: self.handler_button('X')))
        self.operator_buttons.append(Button(text='Enter', font=(
            self.font_style, 15), borderwidth=1, command=lambda: self.handler_button('E')))

        # Border Color Config
        for button in self.number_buttons:
            button.config(borderwidth=1, relief=RIDGE)

        # Numbers Button
        padx_val = 0
        self.number_buttons[7].grid(
            row=3, column=0, sticky='nswe', padx=padx_val)
        self.number_buttons[8].grid(
            row=3, column=1, sticky='nswe', padx=padx_val)
        self.number_buttons[9].grid(
            row=3, column=2, sticky='nswe', padx=padx_val)

        self.number_buttons[4].grid(
            row=4, column=0, sticky='nswe', padx=padx_val)
        self.number_buttons[5].grid(
            row=4, column=1, sticky='nswe', padx=padx_val)
        self.number_buttons[6].grid(
            row=4, column=2, sticky='nswe', padx=padx_val)

        self.number_buttons[1].grid(
            row=5, column=0, sticky='nswe', padx=padx_val)
        self.number_buttons[2].grid(
            row=5, column=1, sticky='nswe', padx=padx_val)
        self.number_buttons[3].grid(
            row=5, column=2, sticky='nswe', padx=padx_val)

        self.number_buttons[0].grid(
            row=6, column=1, sticky='nswe', padx=padx_val)

        self.operator_buttons[0].grid(
            row=6, column=0, sticky='nswe', padx=padx_val)
        self.operator_buttons[1].grid(
            row=6, column=2, sticky='nswe', padx=padx_val)

    def handler_button(self, operator):
        if operator == 'X':
            self.clear_entry()
        elif operator == 'E':
            # Call authorize fuction
            if self.key_used is False:
                if self.ency:
                    self.ency.key = self.entry_data_value
                    self.ency.toggle(self.ency.key)
                    self.key_used = True

                else:
                    self.check_password(self.entry_data_value)

        else:
            self.entry_data_value += operator
            value = self.entry_value.get()
            self.entry_value.set(value + '*')

    def clear_entry(self):
        self.entry_data_value = ''
        self.entry_value.set('')

    def run(self):
        self.root.mainloop()

    def check_password(self, password):
        if hashlib.sha512(password.encode()).hexdigest() == "24f13d46fbe642304dd6ec6e464125d27adf96d8d7f23996f6e17d1a5c50456eb82b2bd30e83ce85b6c15dc34674a12ab7e75af3040264d004a81e908a532636":
            self.ency = Ency.Ency("res/ency_data.json",
                                  "res/encryption_log.txt", "text.txt")
            self.clear_entry()

        else:
            self.clear_entry()
            tkinter.messagebox.showinfo("Error", "Try again.")

    def on_closing(self):
        if self.key_used:
            try :
                self.ency.toggle(self.ency.key)
                ans = tkinter.messagebox.askyesnocancel(title="Ency",message="Do you want to quit?")
                if ans:
                    self.root.destroy()
                else:
                    self.ency.toggle(self.ency.key)
            except :
                ans = tkinter.messagebox.askokcancel(title="Error",message="Back encryption error occur. Do you want to quit?")
                if ans :
                    self.root.destroy()
        else :
            self.root.destroy()


if __name__ == "__main__":
    main = Main()
    main.run()
