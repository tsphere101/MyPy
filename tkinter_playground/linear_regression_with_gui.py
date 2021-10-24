from LinearRegression import Regression
from tkinter import *
from tkinter import filedialog


class Main:

    def __init__(self):

        self.root = Tk()
        self.root.title("Linear Regression")
        self.root.geometry('600x400')

        menuitem_file = Menu()
        menuitem_file.add_command(label="New", command=self.handler_new_file)
        menuitem_file.add_command(label="Open")
        menuitem_file.add_command(label="Exit")

        self.menu = Menu()
        self.menu.add_cascade(label="File", menu=menuitem_file)

        self.root.config(menu=self.menu)

    def handler_new_file(self):
        with filedialog.askopenfile(defaultextension='csv') as file:
            self.regression_model = Regression()
            self.regression_model.read_csv(file)
            self.regression_model.plot_linear_regression()

    def run(self):
        self.root.mainloop()

    def open_file():
        file = filedialog.askopenfile()
        return file


if __name__ == "__main__":

    main = Main()
    main.run()
