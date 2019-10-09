from PIL import Image, ImageDraw 
from random import randint		
import os


def getPattern(imgPath: str, secretInfo: str, outputPath: str, imageSize):
	import numpy as np
	img = Image.new("RGB", imageSize, "black")

	draw = ImageDraw.Draw(img)	   		
	width = imageSize[0]  		   	
	height = imageSize[1]
	pix = img.load()
	with open('keys.txt','w') as f:
		for elem in secretInfo:
			points = (randint(1,width-10),randint(1,height-10))		
			g, b = pix[points][1:3]
			ascii = ord(elem)
			draw.point(points, (ascii,g , b))														
			f.write(str(points)+'\n')			
		f.close()

	img.save(outputPath)
												

def encrypt(imgPath: str, secretInfo: str, outputPath: str):	
	img = Image.open(imgPath)
	draw = ImageDraw.Draw(img)	   		
	width = img.size[0]  		   	
	height = img.size[1]
	pix = img.load()
	with open('keys.txt','w') as f:
		for elem in secretInfo:
			points = (randint(1,width-10),randint(1,height-10))		
			g, b = pix[points][1:3]
			ascii = ord(elem)
			draw.point(points, (ascii,g , b))														
			f.write(str(points)+'\n')			
		f.close()


	if not outputPath:
		outputPath = os.path.splitext(imgPath)[0] + "coded" + ".png" #imgPath.split(".")[-1]
	img.save(outputPath, "PNG")
	getPattern(imgPath, secretInfo, outputPath, (width, height))


