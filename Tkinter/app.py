import os
from tkinter import *
from tkinter import messagebox


def clicked1():
    messagebox.showinfo("Messagebox", "Hello, I'm MessageBox!")


def clicked2():
    root.destroy()


if __name__ == "__main__":
    root = Tk()

    lbl1 = Label(root, text="Bla-bla-bla very important text ...")
    btn1 = Button(root, text="Show MessageBox", command=clicked1)
    btn2 = Button(root, text="Exit App", command=clicked2)

    lbl1.place(x=10, y=10)
    btn1.place(x=175, y=350)
    btn2.place(x=325, y=350)

    root.title("My App")
    root.geometry("600x400")
    # icon = BitmapImage(file=os.path.dirname(os.path.abspath(__file__)) + "/tkinter.ico")
    # root.iconbitmap(icon)

    root.mainloop()
