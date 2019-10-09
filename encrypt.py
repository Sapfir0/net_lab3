from PIL import Image, ImageDraw 
from random import randint		


def encrypt(imgPath, secretInfo):	
	img = Image.open(imgPath)
	draw = ImageDraw.Draw(img)	   		
	width = img.size[0]  		   	
	height = img.size[1]
	pix = img.load()
	f = open('keys.txt','w')

	for elem in secretInfo:
		points = (randint(1,width-10),randint(1,height-10))		
		g, b = pix[points][1:3]
		ascii = ord(elem)
		draw.point(points, (ascii,g , b))														
		f.write(str(points)+'\n')			
	
	print('keys were written to the keys.txt file')
	img.save("newimage.png", "PNG")
	f.close()
												
