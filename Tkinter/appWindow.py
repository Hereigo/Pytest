from tkinter import *
from tkinter import messagebox


class MyApp:
    def __init__(self, master):
        self.master = master
        self.master.after(  # run func after X.000 seconds
            3000, self.master.focus_force()
        )
        self.master.attributes()
        self.master.bind()
        self.master.config()
        # self.master.destroy()
        # self.master.focus_force()
        self.master.geometry("600x400+600+300")  # <== H х W + L + R
        self.master.grab_set()
        self.master.iconbitmap(
            # ===> _tkinter.TclError: format error in bitmap data
            # os.path.dirname(os.path.abspath(__file__)) + "/tkinter.ico"
        )
        self.master.lift()
        # self.master.lower() # Open behind of all windows
        self.master.maxsize()
        self.master.minsize()
        self.master.protocol()
        self.master.resizable(False, False)
        self.master.state()  # Maximized, Minimized, ...
        self.master.title("My App")

        self.lbl1 = Label(
            self.master,
            text="Bla-bla-bla very-very-very-very important text bla-bla-bla ...",
        )
        self.lbl1.pack()
        self.btn1 = Button(self.master, text="Show MessageBox", command=self.show_msg)
        self.btn1.pack()
        self.btn2 = Button(self.master, text="Exit App", command=self.exit_app)
        self.btn2.pack()

        # selt.xxx = Entry() # Single line text widget.
        # selt.xxx = Frame() # Multiple line text widget.
        # selt.xxx = Text()  # Rectangular group of widget with paddings.

        self.lbl1.place(x=10, y=10)
        self.btn1.place(x=175, y=350)
        self.btn2.place(x=325, y=350)

    def show_msg(self):
        messagebox.showinfo("Messagebox", "Hello, I'm MessageBox!")

    def exit_app(self):
        self.master.destroy()
