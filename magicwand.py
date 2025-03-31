from tkinter import *
from PIL import ImageTk,Image
ds=Tk()
ds.title("MAGIC WAND")
ds.config(bg='sky blue')
l1=Label(ds,text='choose an option',font=('calisto MT',25,'bold'))
l1.pack()
l3=Label(ds,text='',bg='sky blue')
l3.pack()
def csd():
    import pen
def csv():
    import image 
f=Frame(ds,width=5,height=5)
f.pack()
img=ImageTk.PhotoImage(Image.open('Pic1.jpg'))
""""img=ImageTk.PhotoImage(Image.open('movie.jpg'))"""
l=Label(f,image=img)
l.pack()
l4=Label(ds,text='',bg='sky blue')
l4.pack()
b1=Button(ds,text='virtual pen',bg='gold',fg='blue',font=('Arial bold',20),command=csd,bd=10,width=10,height=1)
b1.pack()
l5=Label(ds,text='',bg='sky blue')
l5.pack()
img1=ImageTk.PhotoImage(Image.open('fpic2.jpg'))
l2=Label(f,image=img1)
l2.pack()
l6=Label(ds,text='',bg='sky blue')
l6.pack()
b2=Button(ds,text='invisible cloak',bg='gold',fg='blue',font=('Arial bold',20),command=csv,bd=10,width=15,height=1)
b2.pack()
ds.mainloop()

