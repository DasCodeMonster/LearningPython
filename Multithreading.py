import threading
import time

class MyThread(threading.Thread):
	def __init__(self, ID, Name):
		threading.Thread.__init__(self)
		self.ID = ID
		self.Name = Name
		
	def run(self):
		lockMe.acquire()
		print("Starte", self.ID)
		time.sleep(self.ID*3)
		lockMe.release()
		print("Beende", self.ID)
		
lockMe = threading.Lock()
Thread1 = MyThread(1, "Thread1")
Thread2 = MyThread(2, "Thread2")

Thread1.start()
Thread2.start()
Thread1.join()
Thread2.join()
print("Beende Main Thread")