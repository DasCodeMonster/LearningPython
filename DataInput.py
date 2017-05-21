if __name__ == "__main__":
	f=open("Bio","w")
	#print(f.read())
	#print(f.readline())
	a=input("Name: ")
	a="Name: "+a
	f.write(a)
	b=input("Alter: ")
	b="\nAlter: "+b
	f.write(b)
	c=input("Geburtsdatum: ")
	c="\nGeburtsdatum: "+c
	f.write(c)
	f.close
	rf=open("Bio","r")
	print(rf.read())
	rf.close