from tkinter import *
import webbrowser


class Main:
    def __init__(self):
        self.root = Tk()
        self.label_welcome = Label(self.root, text="Welcome")
        self.button_search_google = Button(
            self.root, command=self.button_handler_url_browser,text = "Search")
        self.label_google_search = Label(self.root,text = "Google Search ")
        self.entry_url_search = Entry(self.root, width=50)
        self.entry_google_search = Entry(self.root,width = 50)

        self.label_welcome.pack()
        self.button_search_google.pack()
        self.entry_url_search.pack()
        self.label_google_search.pack()
        self.entry_google_search.pack()

        self.entry_url_search.bind("<Return>",self.handleReturn_entry_url_search)
        self.entry_url_search.bind("<Control-BackSpace>",self.entry_ctrl_bs)
        self.entry_google_search.bind("<Return>",self.handleReturn_entry_google_search)
        self.entry_google_search.bind("<Control-BackSpace>",self.entry_ctrl_bs)

        

    def button_handler_url_browser(self,url):
        if '.' not in url:
            url += '.com'
        url_search = 'https://'+url
        webbrowser.open(url_search)

    def handleReturn_entry_url_search(self,event):
        ent = event.widget
        self.button_handler_url_browser(ent.get())

    def handleReturn_entry_google_search(self,event):
        ent = event.widget
        search_kw = ent.get()
        url_search = 'https://www.google.co.th/search?q=' + search_kw
        webbrowser.open(url_search)

    def entry_ctrl_bs(self,event):
        ent = event.widget
        end_idx = ent.index(INSERT)
        start_idx = ent.get().rfind(" ",None,end_idx)
        ent.selection_range(start_idx,end_idx)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    main = Main()
    main.run()
