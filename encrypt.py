from PIL import Image, ImageDraw 
from random import randint		
import os

def changeFilename(imgPath, innerString, extension=".png"):
	#imgPath.split(".")[-1]
	return os.path.splitext(imgPath)[0] + innerString + extension


def putPixels(image, elem):
	draw = ImageDraw.Draw(image)	   		
	pix = image.load()

	width = image.size[0]  		   	
	height = image.size[1]

	points = (randint(1,width-10),randint(1,height-10))		
	g, b = pix[points][1:3]
	ascii = ord(elem)
	draw.point(points, (ascii,g , b))	
	return points


def getPattern(imgPath: str, secretInfo: str, outputPath: str, imageSize):
	img = Image.new("RGB", imageSize, "black")

	for elem in secretInfo:
		putPixels(img, elem)							

	outputPath = changeFilename(outputPath, "Pattern")
	img.save(outputPath)
												

def encrypt(imgPath: str, secretInfo: str, outputPath: str):	
	img = Image.open(imgPath)

	with open('keys.txt','w') as f:
		for elem in secretInfo:
			points = putPixels(img, elem)														
			f.write(str(points)+'\n')			
		f.close()


	if not outputPath:
		outputPath = changeFilename(imgPath, "coded")
	img.save(outputPath, "PNG")
	getPattern(imgPath, secretInfo, outputPath, img.size)


