import threading
import time

class MyThread(threading.Thread):
	Ergebnis = [0,1]
	def __init__(self, ID, Name):
		threading.Thread.__init__(self)
		self.ID = ID
		self.Name = Name
		
	def run(self):
		i=0
		while i<20:
			lockMe.acquire()
			zahl = self.Ergebnis[len(self.Ergebnis)-2] + self.Ergebnis[len(self.Ergebnis)-1]
			self.Ergebnis.append(zahl)
			lockMe.release()
			i = i+1
lockMe = threading.Lock()
Thread1 = MyThread(1, "Thread1")
Thread2 = MyThread(2, "Thread2")

Thread1.start()
Thread2.start()
Thread1.join()
Thread2.join()
print(MyThread.Ergebnis[42])
print("Beende Main Thread")