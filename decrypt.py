from PIL import Image 		
from re import findall
import os

def takeFromPixelByOneBit(pixels, length: int):
	byte_arr = []
	curChar = 0
	curBit = 0
	count = 0
	for pixel in pixels:
		count +=1
		if count >= length*8:
			break	
		r,g,b = pixel
		curChar |= (r&1)<<curBit
		if (curBit==7):
			curBit = 0
			byte_arr.append(curChar)
			curChar = 0
		else:
			curBit+=1	

	return byte_arr

def takeFromPixelByThreeBit(pixels, length:int):
	byte_arr = []
	curChar = 0
	curBit = 0
	count = 0

	# это не лучший вариант, но одноообразного кода становится меньше
	def writeBit():
		nonlocal curBit, curChar, byte_arr
		if (curBit==7):
			curBit = 0
			byte_arr.append(curChar)
			curChar = 0
		else:
			curBit+=1

	for pixel in pixels:
		count +=1
		if count > length*8:
			break	
		r,g,b = pixel
		curChar |= (r&1)<<curBit
		writeBit()
		count +=1
		if count > length*8:
			break	
		curChar |= (g&1)<<curBit
		writeBit()
		count +=1
		if count > length*8:
			break	
		curChar |= (b&1)<<curBit
		writeBit()
		

	return byte_arr

def takeFromPixelByOneByte(pixels, length:int):
	byte_arr = []
	count = 0
	for pixel in pixels:
		count +=1
		if count >= length:
			break	
		r,g,b = pixel
		cur_byte = 0
		cur_byte |= r & 0x03
		cur_byte |= (g & 0x03) << 3
		cur_byte |= (b & 0x02) << 6
		byte_arr.append(cur_byte) 	

	return byte_arr

def decrypt(imgPath, length, mode=0):
	a = []						    
	image = Image.open(imgPath)		
	pixs = image.load()
	width = image.size[0]  		   	
	height = image.size[1]

	# кидаем данные в одномерный массив
	input_data = [pixs[(x,y)] for x in range(width) for y in range(height)]

	if mode == "1b":
		a = takeFromPixelByOneBit(input_data, length)			
	elif mode == "1B":
		a = takeFromPixelByOneByte(input_data, length)	
	else:
		a = takeFromPixelByThreeBit(input_data, length)	
		
	return ''.join([chr(elem) for elem in a])	



