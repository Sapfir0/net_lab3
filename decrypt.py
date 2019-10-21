from PIL import Image 		
from re import findall
import os

def takeFromPixelByOneBit(pixs, width, height, length: int):
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

def takeFromPixelByThreeBit(pixs, width, height, length:int):
	pass

def takeFromPixelByOneByte(pixs, width, height, length:int):
	byte_arr = []
	count = 0
	for x in range(width):
		for y in range(height):
			count +=1
			if count >= length:
				break	
			r,g,b = pixs[(x,y)]
			cur_byte = 0
			cur_byte |= r & 0x03
			cur_byte |= (g & 0x03) << 3
			cur_byte |= (b & 0x02) << 6
			byte_arr.append(cur_byte) 	

	return byte_arr

def decrypt(imgPath, length):
	a = []						    
	image = Image.open(imgPath)		
	pix = image.load()
	width = image.size[0]  		   	
	height = image.size[1]

	a = takeFromPixelByOneBit(pix, width, height, length)			
		
	return ''.join([chr(elem) for elem in a])	



