from tkinter import *

window = Tk()
window.geometry("600x200+10+20")
window.title("How to Use Widgets")


btn = Button(window,text = "Accept", bg="gray")
btn.place(x=270, y=80)

lbl = Label(window, text="Click Accept, if you want to accept me",fg= "red", font= "Times, 10")
lbl.place(x=190, y=60)

txtfld = Entry(window, bd=5)
txtfld.place(x=230, y=10)


window.mainloop()
