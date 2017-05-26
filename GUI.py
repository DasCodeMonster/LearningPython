from tkinter import *
class App:
    def __init__(self, master):
        Label(root, text="Hier steht Text!", fg="light green", font="Times", width=100, ).pack()
        self.button = Button(master, text="Quit", fg="red", bg = "light blue",command = master.quit)
        self.button.pack(side=LEFT)
        self.button.place
        self.hi_there = Button(master, text="Hello", command = self.say_hi)
        self.hi_there.pack(side=LEFT)
        self.hi_there.place(x=80, y=180)

    def say_hi(self):
        print("Hallo!")

root = Tk()
root.title("First GUI")
root.geometry("170x200+30+30")
app = App(root)
root.mainloop()
# root.destroy()