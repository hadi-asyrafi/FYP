from Tkinter import *
import ttk

class mainGui:

    def __init__(self, master):
        self.master = master
        master.title("Wikipedia Tools")
	root.resizable(width=False, height=False)
	master.geometry('860x540')

	self.mainframe = ttk.Frame(master, padding="3 3 12 12")
	self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        self.label = ttk.Label(self.mainframe, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = ttk.Button(self.mainframe, text="Greet", command=self.greet)
        self.greet_button.pack(side=LEFT)

        self.close_button = ttk.Button(self.mainframe, text="Close", command=master.quit)
        self.close_button.pack(side=RIGHT)

    def greet(self):
        print("Greetings!")

root = Tk()
my_gui = mainGui(root)
root.mainloop()
