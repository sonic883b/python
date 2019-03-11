import Tkinter


counter = 0
font = ('Helvetica',32,"bold")
button = Tkinter.Button(font=font,text=str(counter))


def clicked():
  global counter,button
  counter = counter + 1
  button.config(text=str(counter))

button.config(command=clicked)
button.pack()
button.mainloop()
