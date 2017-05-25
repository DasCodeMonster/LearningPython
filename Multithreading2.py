import threading
import time

class Thread(threading.Thread):
	def __init__(self, Id, Aufgabe):
		threading.Thread.__init__(self)
		self.Id = Id
		self.Aufgabe = Aufgabe

	def run(self):
		print("Thread",self.Id, "ist da")
		self.Aufgabe()

class Aufgaben():
	fibzahl = int(input("Fibonaccizahl eingeben: "))
	von = int(input("Erstelle Liste von "))
	bis = int(input("bis "))+1

	def Liste_erzeugen():
		for x in range(Aufgaben.von, Aufgaben.bis):
			t = threading.Thread(target=Aufgaben.Liste_sortieren, args=(x,))
			Var.Liste.append(x)
			t.start()
		print(Var.Liste)
		print(Var.NeueListe)

	def Liste_sortieren(x):
		if x%2==0:
			Var.NeueListe.append(x)
	
	def Liste_filtern():
		pass

	def fib():
		i = 0
		while i < Aufgaben.fibzahl + 1:
			Var.lock.acquire()
			zahl = Var.Fib[len(Var.Fib)-2] + Var.Fib[len(Var.Fib)-1]
			Var.Fib.append(zahl)
			Var.lock.release()
			i = i+1
		print("Thread 3 ist Fertig")

class Var():
	Liste = []
	NeueListe = []
	Fib = [0,1]
	lock = threading.Lock()
	thread1finish = False
	thread2finish = False
	thread3finish = False
	
Thread1 = Thread(1, Aufgaben.Liste_erzeugen)
# Thread2 = Thread(2, Aufgaben.Liste_sortieren2)
Thread3 = Thread(3, Aufgaben.fib)
Thread3.start()
# Thread2.start() #Thread1 und Thread2 tauschen!
Thread1.start()
Thread1.join()
# Thread2.join()
Thread3.join()
# print("Die Fibonaccizahl von", Aufgaben.fibzahl, "ist ", Var.Fib[Aufgaben.fibzahl])
print("Die Fibonaccizahl von " + str(Aufgaben.fibzahl) + " ist " + str(Var.Fib[Aufgaben.fibzahl]))
# print("Zahlen, von", Aufgaben.von, "bis", Aufgaben.bis, ",die durch 2 Teilbar sind: ", Var.NeueListe)
print("\nZahlen, von " + str(Aufgaben.von) + " bis " + str(Aufgaben.bis) + ", die durch 2 Teilbar sind:\n " + str(Var.NeueListe))
Data1 = "Die Fibonaccizahl von " + str(Aufgaben.fibzahl) + " ist " + str(Var.Fib[Aufgaben.fibzahl])
Data2 = "\nZahlen, von " + str(Aufgaben.von) + " bis " + str(Aufgaben.bis) + ", die durch 2 Teilbar sind:\n " + str(Var.NeueListe)
Datainput = Data1 + Data2
while True:
	Speichern = str(input("Speichern? (Ja/Nein): "))
	if Speichern == "Ja":
		fopen = open(str(input("Dateiname: ")+ ".txt"), "w")
		fopen.write(Datainput)
		print("Goodbye\nExit...")
		break
	elif Speichern == "Nein":
		print("Goodbye\nExit...")
		break
	else:
		print("Ungültig\nNochmal...")
		continue
	
# print(Var.Liste)
# print(Var.NeueListe)
