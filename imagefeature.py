from PIL import Image,ImageChops
import cv2
import matplotlib.pyplot as plt



#Read the images 
img1=Image.open('C:\\Users\\HP Elitebook G6\\Desktop\\Python\\Image processing\\img1.jfif')
plt.imshow(img1)

#Preprocessing the image
#Rotate the image
roatetedimages=img1.rotate(180)
plt.imshow(roatetedimages)

#Crop the image
height,width=img1.size
print(height,width)
croparea=(0,0,width/2,height/2)
cropimage=img1.crop(croparea)
plt.imshow(cropimage)

#resize the image 
height,width=img1.size
resizeimage=img1.resize((int(width/2),int(height/2)))
plt.imshow(resizeimage)


#Considing the image
img2=Image.open('C:\\Users\\Sayed Sigbath\\Desktop\\Python\\Image processing\\Captureimage.jpg')
img1.paste(img2,(50,50))
plt.imshow(img1)

#Transpose of an image
transposeimage=img1.transpose(Image.FLIP_LEFT_RIGHT)
plt.imshow(transposeimage)

#Find out the differenec between two images
img2=Image.open('C:\\Users\\Sayed Sigbath\\Desktop\\Python\\Image processing\\img3.jpg')
difference=ImageChops.difference(img1, img2)
difference.show()

