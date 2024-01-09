from tkinter import *

class Application:
    def __init__(self):
        self.App = Tk()
        self.main_window()
        self.App.mainloop()

    
    def main_window(self):
        self.App.title("Gfinance")
        self.App.geometry("800x500")
        self.App.maxsize(width=1000, height=600)
        self.App.minsize(width=800, height=500)

        
    

Application()