from tkinter import*
import cv2
from PIL import Image,ImageTk
import matplotlib.pyplot as plt
import matplotlib.image as img
from tkinter.filedialog import askopenfilename

def captureimage():
    #Step 1:- Creat a camara object
    camaraobj=cv2.VideoCapture(0)
    
    #Step2:- Read the iamge 
    a,frame=camaraobj.read()
    
    #Step 3:- enable the frame
    cv2.imshow('image', frame)
    
    #Step 4:- Destroy the image after 5 sec
    def kill():
        #destroy
        cv2.destroyAllWindows()
    w.after(5000,kill)
    
    #Step5:- save the image 
    path="Captureimage.jpg"
    cv2.imwrite(path, frame)
    
    '''#Read the input
    img=Image.open(path)
    img.show()'''

    image1=img.imread('Captureimage.jpg')
    plt.imshow(image1)

def uploadimage():
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
    img.save('C:\\Users\\HP Elitebook G6\\Desktop\\Python\\Image processing\\uploadedimage.jpg')
    print("imageuploaded")    
    
w=Tk()
w.geometry('1550x1550')

upload=Button(w,text="Upload",command=uploadimage)
upload.place(x=20,y=40)

capture=Button(w,text="Capture",command=captureimage)
capture.place(x=100,y=40)




w.mainloop()