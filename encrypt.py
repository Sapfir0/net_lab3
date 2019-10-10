from PIL import Image, ImageDraw 
from random import randint		
import os

def changeFilename(imgPath, innerString, extension=".png"):
	#imgPath.split(".")[-1]
	return os.path.splitext(imgPath)[0] + innerString + extension


def putPixels(image, elem):
	def setPixel(width, height, pix, draw, elem): # слишком просто
		points = (randint(1,width-10),randint(1,height-10))		
		g, b = pix[points][1:3]
		ascii = ord(elem)
		draw.point(points, (ascii, g, b))	
		return points
	
	draw = ImageDraw.Draw(image)	   		
	pix = image.load()

	width = image.size[0]  		   	
	height = image.size[1]
	points = setPixel(width, height, pix, draw, elem)
	return points



def getPattern(imgPath: str, secretInfo: str, outputPath: str, imageSize):
	img = Image.new("RGB", imageSize, "black")

	for elem in secretInfo:
		putPixels(img, elem)							

	outputPath = changeFilename(outputPath, "Pattern")
	img.save(outputPath)
	img.show()
												

def encrypt(imgPath: str, secretInfo: str, outputPath: str):	
	img = Image.open(imgPath)
	img.show()

	with open('keys.txt','w') as f:
		for elem in secretInfo:
			points = putPixels(img, elem)														
			f.write(str(points)+'\n')			
		f.close()

	if not outputPath:
		outputPath = changeFilename(imgPath, "coded")
	img.save(outputPath, "PNG")
	img.show()
	getPattern(imgPath, secretInfo, outputPath, img.size)


