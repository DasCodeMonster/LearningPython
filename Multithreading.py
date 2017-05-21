import threading
import time

class MyThread(threading.Thread):
	def __init__(self, ID, Name):
		threading.Thread.__init__(self)
		self.ID = ID
		self.Name = Name
		
	def run(self):
		print("Starte ", self.ID)
		time.sleep(10)
		print("Beende", self.ID)
		
Thread1 = MyThread(1, "Thread1")
Thread2 = MyThread(2, "Thread2")

Thread1.start()
Thread2.start()

print("Beende Main Thread")