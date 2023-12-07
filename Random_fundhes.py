from tkinter import Tk, Button, StringVar, Label
from random import randint

def number_generating():
    number = randint(0,99999)
    var.set("Result : "+ str(number))

main = Tk()
main.geometry('500x250')
main.resizable(height = 0, width = 0)

button_generate = Button(main , text = "Generate", pady = 20, padx = 30, command= number_generating)
button_generate.place(x= 200,y=150)

var = StringVar()
var.set("Result : ")
result = Label(main, textvariable=var)

result.place(x= 225,y = 50)

main.mainloop()

