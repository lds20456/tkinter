import tkinter

screen = tkinter.Tk()
screen.title("fifa")
screen.geometry("500x100")

label1=tkinter.Label(screen, text="python")
label1.grid(column=0, row=0)

def click1():
    button1.configure(text="멍청이가 눌림")
    button1.configure(command=click2)
    label1.configure(foreground="red")
    label1.configure(text="멍청이가 날 바꾸다니")
def click2():
    button1.configure(text="python")
    button1.configure(command=click1)
    label1.configure(foreground="black")
    label1.configure(text="멍청이")
        
button1 = tkinter.Button(screen, text="멍청이",  command=click1)
button1.grid(column=0, row=1)

label1.configure(text="python")
label1.grid(column=0, row=0)

screen.mainloop()

