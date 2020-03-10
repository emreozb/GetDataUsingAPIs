from tkinter import *


class player(object):
    def __init__(self, fullname):
        self.fullname = fullname

    def __str__(self):
        return "FullName: {}".format(str(self.fullname))

    def create_window(self):
        root = Tk()
        root.title('Players')
        root.geometry('{}x{}'.format(300, 400))
        
        playerLabel = Label(root, text=self.fullname, fg="blue")
        playerLabel.pack()

        root.mainloop()
