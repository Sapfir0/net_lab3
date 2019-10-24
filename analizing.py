from PIL import Image, ImageDraw

def analize(firstImg, secondImg):
    img1 = Image.open(firstImg)
    img2 = Image.open(secondImg)
    #img.show()

    pixs1 = img1.load()
    pixs2 = img2.load()

    width = img1.size[0]
    height = img1.size[1]

    imgOutput = Image.new("RGB", (width, height), "white")	
    drawOut = ImageDraw.Draw(imgOutput)
    for x in range(width):
        for y in range(height):
            if pixs1[(x,y)] != pixs2[(x,y)]:
                drawOut.point((x,y), (0,0,0))

    imgOutput.show()