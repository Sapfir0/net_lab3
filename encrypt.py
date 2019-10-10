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
	
	currentChar = 0
	currentBit = 0
	count = 0
	for x in range(width):
		for y in range(height):
			r,g,b = pix[(x,y)]
			if (currentChar<len(elem)):
				r = r&254
				currentlyCodedElem = elem[currentChar]
				code = ord(currentlyCodedElem)
				bitToCode = code&(1<<currentBit)
				lsb = bitToCode>>currentBit
				r |= lsb
				draw.point((x,y), (r,g,b))
				if (currentBit==7):
					currentBit = 0
					currentChar+=1
				else:
					currentBit+=1

							

def encrypt(imgPath: str, secretInfo: str, outputPath: str):	
	img = Image.open(imgPath)
	img.show()
	putPixels(img, secretInfo)

	if not outputPath:
		outputPath = changeFilename(imgPath, "coded")
	img.save(outputPath, "PNG")
	img.show()


