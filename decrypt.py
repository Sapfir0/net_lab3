from PIL import Image 		
from re import findall
import os

def takeFromPixelByOneBit(pixs: Image, width, height, length: int):
	byte_arr = []
	curChar = 0
	curBit = 0
	count = 0
	for x in range(width):
		for y in range(height):
			count +=1
			if count >= length*8:
				break	
			r,g,b = pixs[(x,y)]
			curChar |= (r&1)<<curBit
			if (curBit==7):
				curBit = 0
				byte_arr.append(curChar)
				curChar = 0
			else:
				curBit+=1	

	return byte_arr

def decrypt(imgPath, length):
	a = []						    
	image = Image.open(imgPath)		
	pix = image.load()
	width = image.size[0]  		   	
	height = image.size[1]
	a = takeFromPixelByOneBit(pix, width, height, length)			
		
	return ''.join([chr(elem) for elem in a])	



