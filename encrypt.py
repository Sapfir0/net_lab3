from PIL import Image, ImageDraw 
from random import randint		

secretInfo = "i am sanyassssssssssssssssssssssssssssssЭ"
print(len(secretInfo))
def stega_encrypt():	
	
	keys = [] 					#сюда будут помещены ключи
	import os
	imgPath = os.path.join(os.path.curdir, "image.jpg")
	img = Image.open(imgPath)
	draw = ImageDraw.Draw(img)	   		#объект рисования
	width = img.size[0]  		   		#ширина
	height = img.size[1]		   		#высота	
	pix = img.load()				#все пиксели тут
	f = open('keys.txt','w')			#текстовый файл для ключей

	for elem in ([ord(elem) for elem in secretInfo]):
		points = (randint(1,width-10),randint(1,height-10))		
		g, b = pix[points][1:3]
		draw.point(points, (elem,g , b))														
		f.write(str(points)+'\n')								
	
	print('keys were written to the keys.txt file')
	img.save("newimage.png", "PNG")
	f.close()
												
stega_encrypt()
