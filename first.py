# import tkinter
# top = tkinter.Tk()
# # Code to add widgets will go here...
# top.mainloop()


from tkinter import Tk, StringVar, OptionMenu, mainloop

master = Tk()

variable = StringVar(master)
variable.set("one") # default value

w = OptionMenu(master, variable, "one", "two", "three")
w.pack()

mainloop()