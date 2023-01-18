from tkinter import *
win = Tk()

#add widgets
class MyWin:
    def __init__(self,win):
        self.lbl1 = Label(win,text="My First Standard Calculator", fg="Red")
        self.lbl1.place(x=350,y=20)
        self.lbl2 = Label(win,text="Input No.1", fg="red")
        self.lbl2.place(x=85,y=50)
        self.txt1 = Entry(win,bd=4, bg="white")
        self.txt1.place(x=150,y=50)
        self.lbl3 = Label(win,text="Input No.2", fg="red")
        self.lbl3.place(x=85,y=100)
        self.txt2 = Entry(win,bd=4, bg="white")
        self.txt2.place(x=150,y=100)
        self.lbl4= Label(win,text="Result", fg="red")
        self.lbl4.place(x=100,y=150)
        self.txt3 = Entry(win,bd=4, bg="white")
        self.txt3.place(x=150,y=150)
        self.btn1 = Button(win,text="Addition", bg="green", command= self.addition)
        self.btn1.place(x=300,y=50)
        self.btn2 = Button(win, text="Subtraction",bg="green" ,command = self.subtraction)
        self.btn2.place(x=300, y=100)
        self.btn3 = Button(win, text="Multiplication", bg="green" , command = self.multiplication)
        self.btn3.place(x= 370, y = 50)
        self.btn4 = Button(win, text="Division",bg="green", command= self.division)
        self.btn4.place(x=380, y=100)

    def addition(self):
        self.txt3.delete(0,'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1+num2
        self.txt3.insert(END,str(result))

    def subtraction(self):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 - num2
        self.txt3.insert(END, str(result))

    def multiplication(self):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 * num2
        self.txt3.insert(END, str(result))



    def division(self):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 // num2
        self.txt3.insert(END, str(result))

mywin = MyWin(win)


win.geometry("800x500+10+20")
win.title("Standard Calculator")
win.mainloop()