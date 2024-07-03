# create a GUI with a label and a button. 
from tkinter import *


class MyGui:

    def __init__(self, masterframe):
        myframe = Frame(masterframe)  #create Frame Widget
        myframe.pack()
        myframe.master.title("Ninja Turtles")
        frame1 = Frame(masterframe)
        frame1.pack(side=RIGHT, fill=X, expand=YES)

        checkbox1 = Checkbutton(masterframe, text="L Ninja")  #create checkbox.

        checkbox1.pack(side=TOP, padx=4, pady=4)
        checkbox1.config(bg="#00008b")

        checkbox2 = Checkbutton(masterframe, text="D Ninja")  #create checkbox.
        checkbox2.pack(side=TOP, padx=4, pady=4)

        checkbox3 = Checkbutton(masterframe, text="R Ninja")

        checkbox3.pack(side=TOP)

        checkbox4 = Checkbutton(masterframe, text="M Ninja")
        checkbox4.pack(side=TOP, padx=4, pady=4)

        radiobtn1 = Radiobutton(masterframe, text="Grey")
        radiobtn1.pack()

        nin_pic = 'Ninja Turtle R'
        ninja_turtle_frame = LabelFrame(masterframe, bg="red", width="200", height="200")  # New frame

        scrollbar = Scrollbar(frame1)
        scrollbar.pack(side=RIGHT)
        frame2 = Frame(masterframe)
        label5 = Label(frame2, text="Karate")
        label5.grid(row=1, column=6)
        frame2.pack()


def main():
    root = Tk()  # Gui object instantiation
    root.geometry("400x400")
    root.resizable()
    g = MyGui(root)
    root.mainloop()


if __name__ == "__main__":
    main()
