import tkinter as tk
import tkinter.filedialog as tkf
# def FileOpen():
#     f = open(tkf.askdirectory(), "w",)
#
# def Fenster(root):
#     root.title("Browse")
#     tk.Label(root, text="Browse your directory.").pack()
#     tk.Button(root, text="Browse", command=FileOpen()).pack()
def DeinText():
    print(e.get())

def Browse():
    Directory = tkf.askdirectory()
    Directory(Directory)

def Directory(Directory):
    Path = Directory
    return Path

def SaveFile():
    f = open(Directory() + "\\Hallo.txt", "w")
    f.write(e.get())

if __name__ == "__main__":
    root = tk.Tk()
    root.title("GUI")
    tk.Label(root, text="Browse your directory.").grid(row=0)
    tk.Button(root, text="Quit", command=root.quit).grid(row=3)
    tk.Button(root, text="Save File", command=Directory).grid(row=3, column=1)
    e = tk.Entry(root)
    tk.Button(root, text="Browse", command=Browse).grid(row=0, column=2, pady=4, sticky="w")
    tk.Label(root, text="Dein Text: ").grid(row=2)
    e.grid(row=2, column=1)
    tk.Button(root, text="Print", command=DeinText).grid(row=2, column=2)
    root.mainloop()
    # Hallo! Wie geht es Dir?