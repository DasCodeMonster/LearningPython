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
	def Liste_erzeugen():
		x=0
		while True:
			x = x+1
			lock.acquire()
			Var.Liste.append(x-1)
			lock.release()
			if len(Var.Liste) == 50:
				print("Thread 1 ist fertig", Var.Liste)
				break
				
	def Liste_sortieren():
		while len(Var.Liste)<50:	
			for i in Var.Liste:
				if i%2==0:
					lock.acquire()
					Var.NeueListe.append(i)
					lock.release()
		print("Thread 2 ist fertig", Var.NeueListe)
			
	# def fib():
		# lock.acquire()
		# zahl = Var.Fib[len(Var.Fib)-2] + Var.Fib[len(Var.Fib)-1]
		# self.Ergebnis.append(zahl)
		# lock.release()
		
class Var():
	Liste = []
	NeueListe = []
	Fib = [0,1]

lock = threading.Lock()
Thread1 = Thread(1, Aufgaben.Liste_erzeugen)
Thread2 = Thread(2, Aufgaben.Liste_sortieren)
# Thread3 = Thread(3, Aufgaben.fib)
# Thread3.start()
Thread2.start() #Thread1 und Thread2 tauschen!
Thread1.start()
Thread1.join()
Thread2.join()
# Thread3.join()
# print(Var.Fib[5])
# print(Var.Liste)
# print(Var.NeueListe)