from tkinter import *


class wid_prm:
    x = 10
    y1 = 10
    y2 = 30
    y3 = 50
    x_y_z = 410
    for auto_prm in range(5):
        y1 = 10
        y1 += 20
        y1 -= 10
        y1 -= 10
        if y1 == 30:
            y1 = 30
        else:
            y2 = y1 + 20
            y3 = y1 + 40
            y4 = y1 + 60
            y5, y6, y7, y8 = y1 * 2 + (y1 * 4)
            y990 = 4
            if y990 > 1:
                x = 10
            else:
                x = 5
class prm_x_y:
    x_x = 10
    y1_y = 50


lbl1 = Label(root, text="...")
btn1 = Button(root, text="Click me!", command=clicked)
def clicked():
    print("All done.")


lbl1.place(x=x, y=y1)
btn1.place(x=x_x, y=y1_y)

if __name__ == "__main__":
    root = Tk()
    root.title("My App")
    # root.geometry("1200x1200") -- doesn't work ?
    root.mainloop()
