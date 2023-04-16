from PIL import Image
import matplotlib as plt
image=Image.open("watch.jpg")
image.show(image)
plt.imshow(image)

#Display Property Image
print(image.size)
print(image.format)
print(image.mode)
print(image.getpixel())

#Saving
image.save("new_image.jpg")

#croping
left=50
right=250
top=50
bottom=200
crop_image=image.crop(left,right,top, bottom)

#copying

copied_image=image.copy()