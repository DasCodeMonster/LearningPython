import tkinter as tk
import tkinter.filedialog as tkf

Directory = None
Filename = None

def DeinText():
    print(e.get())

def Browse():
    global Directory
    global Filename
    Directory = tkf.askdirectory()
    # Filename = tkf.asksaveasfilename()
    d.set(Directory)
    print(Directory)

def dynamiclabel(label):
    label.config(text = Directory)

def SaveFile():
    f = open(Directory + "\\Hallo.txt", "w")
    f.write(e.get())

if __name__ == "__main__":
    root = tk.Tk()
    root.title("GUI")
    d = tk.StringVar()
    tk.Label(root, text="Browse your directory.").grid(row=0)
    tk.Button(root, text="Browse", command=Browse).grid(row=0, column=2)
    DynamicLabel = tk.Label(root, textvariable=d).grid(row=0, column=1)
    # dynamiclabel(DynamicLabel)
    tk.Label(root, text="Dein Text: ").grid(row=2, sticky="w")
    tk.Button(root, text="Print", command=DeinText).grid(row=2, column=2)
    tk.Button(root, text="Quit", command=root.quit).grid(row=3)
    tk.Button(root, text="Save File", command=SaveFile).grid(row=3, column=1)
    e = tk.Entry(root)
    e.grid(row=2, column=1)
    root.update_idletasks()
    root.mainloop()