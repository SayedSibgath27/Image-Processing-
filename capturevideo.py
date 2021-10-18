from tkinter import*
import cv2
from PIL import Image,ImageTk

w=Tk()
w.geometry('1550x1550')

#Step1:- Creat a lable to display video
vlabel=Label(w)
vlabel.place(x=10,y=20)

#Step2:- Creat a camara object
cobj=cv2.VideoCapture(0)

#Define the function to capture video
def showvideo():
    #Step 4:- Capture the image 
    cvimage=cv2.cvtColor(cobj.read()[1],cv2.COLOR_BGR2RGB)
    img=Image.fromarray(cvimage)
    
    #Step 5:- Set the image into the label
    photo=ImageTk.PhotoImage(image=img)
    vlabel.imgtk=photo
    vlabel.configure(image=photo)
    
    #Step 6:- Call the function after every 0.2 sec
    vlabel.after(20,showvideo)
showvideo()


w.mainloop()
