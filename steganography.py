import argparse
from encrypt import encrypt
from decrypt import decrypt
import os

secretInfo = "Quick brown fox jumps over lazy dog."

inputImgPath = os.path.join(os.path.curdir, "image.jpg")
outputImgPath = os.path.join(os.path.curdir, "newimage.png")

parser = argparse.ArgumentParser(description='Hide info in image.')
parser.add_argument('-d', '--decrypt', action="store_true",)
parser.add_argument('-e', '--encrypt', action="store_true",)
parser.add_argument('-i', '--imgPath', default=inputImgPath )
parser.add_argument('-m', '--mode', default="1b", type=str, help="Input 1b or 1bit for coding 1 bit \n 3b or 3bit for coding 3 bit \n 1B or 1Byte for coding full one byte to pixel")
parser.add_argument('-s', '--story', default=secretInfo, type=str, help="Input you story")
parser.add_argument('--length', default=len(secretInfo), type=int, help="Input decrypt length > 0")


args = parser.parse_args()
algorithm = args.mode 


if args.decrypt:
    length = args.length if args.length > 0 else 10
    res = decrypt(args.imgPath, args.length, algorithm)
    print(f"Раcшифрована информация с файла {args.imgPath}:\n{res}")
elif args.encrypt:
    encrypt(args.imgPath, args.story, outputImgPath, algorithm)
    print(f"Зашифрована информация \"{args.story}\" в {outputImgPath}")
else:
    print("Пу")

