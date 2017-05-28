import tkinter as tk
import tkinter.filedialog as tkf
# def directory(dire):
#     directory = True
directory = False
def Fenster(root):
    tk.Frame(root)
    root.title("Tets")
    tk.Label(root, text="Browse your directory.").pack()
    # tk.Button(root, text="Browse", command=directory()).pack()
    if directory == True:
        tkf.askdirectory()

if __name__ == "__main__":
    root = tk.Tk()
    Fenster(root)
    root.mainloop()