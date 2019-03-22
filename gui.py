from tkinter import *
stocklist=['sun','moon','earth']
master=Tk()
variable1=StringVar(master)
variable1.set(stocklist[0])
w=OptionMenu(master,variable1,*stocklist)
w.pack()
variable2=StringVar(master)
variable2.set(stocklist[0])
w=OptionMenu(master,variable2,*stocklist)
w.pack()
def compare():
    cmd=0
    print(cmd)
button=Button(master,text='similarities',command=compare)
button.pack()
mainloop()
