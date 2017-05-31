import threading
import tkinter.filedialog as tkf
import tkinter as tk


class Thread(threading.Thread):
    def __init__(self, Id, Aufgabe, args=()):
        threading.Thread.__init__(self)
        self.Id = Id
        self.Aufgabe = Aufgabe
        self.args=args

    def run(self):
        print("Thread", self.Id, "ist da")
        self.Aufgabe(*self.args)


class Aufgaben():
    def Liste_erzeugen(von, bis, teilen):
        for x in range(von, bis):
            t = threading.Thread(target=Aufgaben.Liste_sortieren, args=(x,teilen,))
            Liste.append(x)
            t.start()
        print(Liste)
        print(NeueListe)

    def Liste_sortieren(x, teilen):
        if x % teilen == 0:
            NeueListe.append(x)

    def Liste_filtern():
        pass

    def fib(fibzahl):
        i = 0
        while i < fibzahl + 1:
            lock.acquire()
            zahl = Fib[len(Fib) - 2] + Fib[len(Fib) - 1]
            Fib.append(zahl)
            lock.release()
            i = i + 1
        print("Thread 3 ist Fertig")


def get_entrys():
    fibzahl = int(e1_fibzahl.get())
    von = int(e2_von.get())
    bis = int(e3_bis.get())
    teilen = int(e4_teilen.get())
    return fibzahl, von, bis, teilen

def Berechnen():
    fibzahl, von, bis, teilen =  get_entrys()
    Thread1 = Thread(1, Aufgaben.Liste_erzeugen, args=(von,bis,teilen,))
#     Thread1 = threading.Thread(target=Aufgaben.Liste_erzeugen, args=(von,bis,teilen,))

#     Thread2 = Thread(2, Aufgaben.Liste_sortieren2)
#     Thread3 = threading.Thread(target=Aufgaben.fib, args=(fibzahl,))
    Thread3 = Thread(3, Aufgaben.fib, args=(fibzahl,))
    Thread3.start()
    # Thread2.start() #Thread1 und Thread2 tauschen!
    Thread1.start()
    Thread1.join()
    # Thread2.join()
    Thread3.join()

    print("Die Fibonaccizahl von " + str(fibzahl) + " ist " + str(Fib[fibzahl]))
    print("\nZahlen, von " + str(von) + " bis " + str(bis - 1) + ", die durch " + str(
        teilen) + " Teilbar sind:\n" + str(NeueListe))


def Speichern(self):
    Data1 = "Die Fibonaccizahl von " + str(fibzahl) + " ist " + str(Fib[fibzahl])
    Data2 = "\nZahlen, von " + str(von) + " bis " + str(bis - 1) + ", die durch " + str(
        teilen) + " Teilbar sind:\n" + str(NeueListe)
    Datainput = Data1 + Data2

    while True:
        Speichern = str(input("Speichern? (Ja/Nein): "))
        if Speichern == "Ja" or Speichern == "ja" or Speichern == "Yes" or Speichern == "yes" or Speichern == "Y" or Speichern == "y" or Speichern == "J" or Speichern == "j":
            fopen = open(str(input("Dateiname: ") + ".txt"), "w")
            fopen.write(Datainput)
            break

        elif Speichern == "Nein" or Speichern == "nein" or Speichern == "No" or Speichern == "no" or Speichern == "Nu" or Speichern == "nu" or Speichern == "N" or Speichern == "n" or Speichern == "Nay" or Speichern == "nay":
            break

        else:
            print("Ungültig\nNochmal...")
            continue

            # nochmal = input("Neue Berechung? (Ja/Nein): ")
            # if nochmal == "Ja" or nochmal == "ja" or nochmal == "J" or nochmal == "j" or nochmal == "Yes" or nochmal == "yes" or nochmal == "Y" or nochmal == "y":
            #     continue
            #
            # if nochmal == "Nein" or nochmal == "nein" or nochmal == "No" or nochmal == "no" or nochmal == "Nu" or nochmal == "nu" or nochmal == "N" or nochmal == "n" or nochmal == "Nay" or nochmal == "nay":
            #     print("Goodbye\nExit...")


if __name__ == "__main__":
    Liste = []
    NeueListe = []
    Fib = [0, 1]
    lock = threading.Lock()
    root = tk.Tk()
    root.title("Multithreading GUI")
    menu = tk.Menu(root)
    root.config(menu=menu)
    Helpmenu = tk.Menu(menu)
    menu.add_cascade(label="Help", menu=Helpmenu)
    tk.Label(root, text="Stelle der Fibonaccizahl:").grid(row=0, column=0, sticky="w", padx=5)
    e1_fibzahl = tk.Entry(root)
    e1_fibzahl.grid(row=0, column=1, sticky="w", padx=5)
    tk.Label(root, text="Fibonaccizahl der Stelle X:").grid(row=1, column=0, sticky="w", padx=5)
    tk.Label(root, text="Hier steht die Fibonaccizahl").grid(row=1, column=1, sticky="w", padx=5)
    tk.Label(root, text="Liste Sortieren:").grid(row=2, column=0, sticky="w", padx=5)
    tk.Label(root, text="Start Liste:").grid(row=3, column=0, sticky="w", padx=5)
    e2_von = tk.Entry(root)
    e2_von.grid(row=3, column=1, sticky="w", padx=5)
    tk.Label(root, text="EndeListe").grid(row=4, column=0, sticky="w", padx=5)
    e3_bis = tk.Entry(root)
    e3_bis.grid(row=4, column=1, sticky="w", padx=5)
    tk.Label(root, text="Zahlen in Liste, die durch n Teilbar sind: n=").grid(row=5, column=0, sticky="w", padx=5)
    e4_teilen = tk.Entry(root)
    e4_teilen.grid(row=5, column=1, sticky="w", padx=5)
    tk.Label(root, text="Ergebnis:").grid(row=6, column=0, sticky="w", padx=5)
    tk.Label(root, text="Hier steht die Liste").grid(row=6, column=1, sticky="w", padx=5)
    tk.Button(root, text="Quit", command=root.quit).grid(row=7, column=0, sticky="w", padx=5)
    tk.Button(root, text="Berechnen", command=Berechnen).grid(row=7, column=0, sticky="ne", padx=5)
    root.mainloop()

    # while True:
    # 	try:
    # 		# fibzahl = int(input("Fibonaccizahl eingeben: "))
    # 		# von = int(input("Erstelle Liste von "))
    # 		# bis = int(input("bis ")) + 1
    # 		# teilen = int(input("Liste teilen durch: "))
    # 		break
    # 	except:
    # 		print("Eingaben dürfen jeweils nur eine Zahl beinhalten!")
