from PIL import Image, ImageDraw 
from random import randint		
import os

def putPixelsByOneBit(data, elem):
	"""
	в один пиксель один значащий бит
	"""
	pixel_arr = []
	currentChar = 0
	currentBit = 0
	count = 0
	for pix in data:
		if not (currentChar<len(elem)):
			break
		
		r,g,b = pix
		r = r&254
		currentlyCodedElem = elem[currentChar]
		code = ord(currentlyCodedElem)
		bitToCode = code&(1<<currentBit)
		lsb = bitToCode>>currentBit
		r |= lsb
		if (currentBit==7):
			currentBit = 0
			currentChar+=1
		else:
			currentBit+=1
		pixel_arr.append((r,g,b))

	return pixel_arr

def putPixelsByThreeBit(data, elem):
	"""
	в один пиксель три значащих бита
	"""
	pixel_arr = []
	def lsb(currentlyCodedElem, currentBit, to_byte = ord):
		code = to_byte(currentlyCodedElem)
		bitToCode = code&(1<<currentBit)
		return bitToCode>>currentBit
	
	
	currentChar = 0
	currentBit = 0
	count = 0
	
	def nextChar():
		nonlocal currentBit, currentChar, pixel_arr
		if (currentBit==7):
			currentBit = 0
			currentChar+=1
		else:
			currentBit+=1

	for pix in data:
		if (currentChar>=len(elem)):
			break

		r,g,b = pix

		r = r&254
		r |= lsb(elem[currentChar], currentBit)
		nextChar()

		g = g&254
		g |= lsb(elem[currentChar], currentBit)
		nextChar()
		
		b = b&254
		b |= lsb(elem[currentChar], currentBit)
		nextChar()

		pixel_arr.append((r,g,b))
	return pixel_arr


def putPixelsByOneByte(data, elem):
	"""
	в один пиксель один значащий байт
	"""
	currentChar = 0
	count = 0
	pixel_arr = []
	for pix in data:
		if not (currentChar<len(elem)):
			break
		r,g,b = pix
		currentlyCodedElem = elem[currentChar]
		code = ord(currentlyCodedElem)
		threeBits = 0b11111000
		twoBits = 0b11111100
		r = (r & threeBits) | (code & ~threeBits)
		g = (g & threeBits) | (code>>3 & ~threeBits)
		b = (b & twoBits)   | (code>>6 & ~twoBits)
		pixel_arr.append((r,g,b))

	return pixel_arr
		
def changeFilename(imgPath, innerString, extension=".png"):
	#imgPath.split(".")[-1]
	return os.path.splitext(imgPath)[0] + innerString + extension							

def encrypt(imgPath: str, secretInfo: str, outputPath: str):	
	img = Image.open(imgPath)
	img.show()

	draw = ImageDraw.Draw(img)	   		
	pixs = img.load()

	width = img.size[0]  		   	
	height = img.size[1]

	# кидаем данные в одномерный массив
	input_data = [pixs[(x,y)] for x in range(width) for y in range(height)]
	
	output = putPixelsByOneBit(input_data, secretInfo)

	x, y = 0, 0
	for i in range(len(output)):
		draw.point((x,y), output[i]) # магия
		x += 1
		if x >= width:
			x = 0
			y += 1
			# здесь должна быть проверка на выход за границы дозволенного, но мне влом

	if not outputPath:
		outputPath = changeFilename(imgPath, "coded")
	
	img.save(outputPath, "PNG")
	img.show()


