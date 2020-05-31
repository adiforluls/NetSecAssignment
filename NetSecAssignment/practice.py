import tkinter as tk
from tkinter import *
from tkinter.ttk import *

root = Tk()
style = Style()
var1 = StringVar()
s = StringVar()
sml1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cap1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
sml1.reverse()
cap1.reverse()

def encrypt():
	var1 = ip.get("1.0",'end-1c')       #ip = encryption box and op = decryption box
	op.delete("1.0",'end-1c')                                  
	s=""
	for i in range(len(var1)):
		#can also use modular arithmetic instead of a list
		temp = ord(var1[i])
		if temp>=65 and temp<=90:        #for capital letters
			s+=cap1[temp-65]             #for small letters
		elif temp>=97 and temp<=122:
			s+=sml1[temp-97]
		else: 
			s+=var1[i]                   #any other character or symbol should remain intact
	op.insert("end",s)
	return ''

#same as encryption
def decrypt():
	var1 = op.get("1.0",'end-1c')
	ip.delete("1.0",'end-1c')
	s=""
	for i in range(len(var1)):
		temp = ord(var1[i])
		if temp>=65 and temp<=90:
			s+=cap1[temp-65]
		elif temp>=97 and temp<=122:
			s+=sml1[temp-97]
		else:
			s+=var1[i]
	ip.insert("end",s)
	return ''

def close_window():                                         
	root.destroy()

root.title('HACKERMAN')
root.geometry("500x500")

style.configure('TButton', font = 
               ('calibri', 10, 'bold', 'underline'), 
                foreground = 'red') 

frame1 = Frame(root)
frame1.pack()
ip = Text(frame1, height = 25, width = 200)
scroll = Scrollbar(frame1, orient=VERTICAL, command = ip.yview)
scroll.pack(side=RIGHT, fill=Y)
ip["yscrollcommand"] = scroll.set
ip.pack(side=LEFT, fill=BOTH, expand=YES)

frame2 = Frame(root)
frame2.pack()
enc = Button(frame2, text="Encrypt", command = encrypt)
dec = Button(frame2, text="Decrypt", command = decrypt)
enc.pack(side = LEFT)
dec.pack(side = RIGHT)

frame3 = Frame(root)
frame3.pack()
op = Text(frame3, height = 25, width = 200)
scroll1 = Scrollbar(frame3, orient=VERTICAL, command = op.yview)
scroll1.pack(side=RIGHT, fill=Y)
op["yscrollcommand"] = scroll1.set
op.pack(side=RIGHT, fill=BOTH, expand=YES)
quit = Button(frame2, text="Quit", style='W.TButton', command=close_window)
quit.pack(side = LEFT)

root.mainloop()

