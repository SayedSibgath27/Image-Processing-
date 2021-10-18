from tkinter import *
from PIL import Image,ImageTk
from tkinter import*
import cv2
from PIL import Image,ImageTk
import matplotlib.pyplot as plt
import matplotlib.image as img
from tkinter.filedialog import askopenfilename
from tkinter import PhotoImage
from PIL import Image,ImageChops
import cv2
import matplotlib.pyplot as plt


def rotate():
      
    angle=int(a.get())
        
    #Read the images 
    img1=Image.open('uploadedimage.jpg')
    plt.imshow(img1)
    
    #Preprocessing the image
    #Rotate the image
    roatetedimages=img1.rotate(angle)
    plt.imshow(roatetedimages)
    roatetedimages.save('modefiedimage.jpg')
    print("done")
    roatetedimages.show()
    
    

       

def upload():
   
    def confirmm():
        w.destroy()
        import Camaraapplication            
    path=askopenfilename(initialdir="",
                     filetype=(('imagefile','*jpg'),('allfile','*.*')),
                     title="Choose ypur file"
                     
        ) 
    
    print(path)
    #Display the image on the console
    #image1=img.imread(path)
    #plt.imshow(image1)
    
    #Save the images into oocal directory
    img=Image.open(path)
    img.save('uploadedimage.jpg')
    #print("imageuploaded")    
    confirm_btn=Button(input_frame,text="confirm",font=300,fg='Green',command=confirmm)
    confirm_btn.place(x=80,y=600)
   
   
    
    
w=Tk()
w.geometry('1550x1550')


input_frame=Frame(w,bd=5,bg='blue')
input_frame.place(x=10,y=20,height=1000,width=500)

input_label=Label(input_frame,text="Input",font=('areal',20))
input_label.place(x=10,y=20)


upload=Button(input_frame,text="Upload",font=300,fg='Green',command=upload)
upload.place(x=10,y=600)

capture=Button(w,text="Capture",font=300,fg='Green')
capture.place(x=100,y=600)

image=Image.open("uploadedimage.jpg")
image.thumbnail((1550,1550),Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image)

input_label1=Label(input_frame)
input_label1.configure(image=photo)
input_label1.place(x=10,y=200,height=300,width=300)


a=Spinbox(w)
a.place(x=700,y=200)
r_btn=Button(w, command=rotate, text="rotate")
r_btn.place(x=700,y=240)

output_frame=Frame(w,bd=5,bg='blue')
output_frame.place(x=950,y=20,height=1000,width=500)


oimage=Image.open("modefiedimage.jpg")
oimage.thumbnail((1550,1550),Image.ANTIALIAS)
ophoto=ImageTk.PhotoImage(oimage)

output_label=Label(output_frame)
output_label.configure(image=ophoto)
output_label.place(x=10,y=200,height=300,width=300)


save=Button(output_frame,text="Save",font=300,fg='Green')
save.place(x=10,y=600)





w.mainloop()
