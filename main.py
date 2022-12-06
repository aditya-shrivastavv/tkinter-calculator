from tkinter import *

root = Tk()

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        pass
    elif text == " C ":
        display_output.set("")
        screen.update()
    else:
        display_output.set(display_output.get() + text)
        screen.update()

root.geometry("520x650+20+20")
root.minsize(520,650)
root.title("Calculator - tkinter")

#screen display config
display_output = StringVar()
display_output.set("")      # initially blank
screen = Entry(root, textvariable=display_output, font="jetbrains 50 bold")
screen.pack(padx=15, pady=15, fill="both")

fr = Frame(root)

b = Button(fr, padx=10, pady=10, text="9", font="lucida 30 bold", bg="#AFA9A7")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)

b = Button(fr, padx=10, pady=10, text="8", font="lucida 30 bold", bg="#AFA9A7")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)

b = Button(fr, padx=10, pady=10, text="7", font="lucida 30 bold", bg="#AFA9A7")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)

b = Button(fr, padx=10, pady=10, text="/", font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)

b = Button(fr, padx=10, pady=10, text=" C ", font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)

fr.pack(fill="both")

fr = Frame(root)

b = Button(fr, padx=10, pady=10, text="6", font="lucida 30 bold", bg="#AFA9A7")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)

b = Button(fr, padx=10, pady=10, text="5", font="lucida 30 bold", bg="#AFA9A7")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)

b = Button(fr, padx=10, pady=10, text="4", font="lucida 30 bold", bg="#AFA9A7")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)

b = Button(fr, padx=10, pady=10, text="*", font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)

b = Button(fr, padx=10, pady=10, text="%", font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)

fr.pack(fill="both")

fr = Frame(root)

b = Button(fr, padx=10, pady=10, text="3", font="lucida 30 bold", bg="#AFA9A7")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)

b = Button(fr, padx=10, pady=10, text="2", font="lucida 30 bold", bg="#AFA9A7")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)

b = Button(fr, padx=10, pady=10, text="1", font="lucida 30 bold", bg="#AFA9A7")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)

b = Button(fr, padx=10, pady=10, text="+", font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)

b = Button(fr, padx=10, pady=10, text="-", font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)

fr.pack(fill="both")

fr = Frame(root)

b = Button(fr, padx=10, pady=10, text="  ", font="lucida 30 bold", bg="#AFA9A7")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)

b = Button(fr, padx=10, pady=10, text="0", font="lucida 30 bold", bg="#AFA9A7")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)

b = Button(fr, padx=10, pady=10, text="  ", font="lucida 30 bold", bg="#AFA9A7")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)

b = Button(fr, padx=10, pady=10, text="  ", font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)

b = Button(fr, padx=10, pady=10, text="  ", font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)

fr.pack(fill="both")

root.mainloop()