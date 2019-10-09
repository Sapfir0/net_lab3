from PIL import Image 		
from re import findall

def stega_decrypt():
	
	a = []						    
	keys = []
	import os
	imgPath = os.path.join(os.path.curdir, "newimage.png")
	img = Image.open(imgPath)		
	pix = img.load()
	f = open(os.path.join(os.path.curdir, 'keys.txt'),'r')
	y = str([line.strip() for line in f])				
																
	for i in range(len(findall(r'\((\d+)\,',y))):
		points = (int(findall(r'\((\d+)\,',y)[i]),int(findall(r'\,\s(\d+)\)',y)[i])) # x,y
		keys.append(points) 	
	for key in keys:
		a.append(pix[tuple(key)][0])							
	return ''.join([chr(elem) for elem in a])	


print("you message: ",stega_decrypt())



