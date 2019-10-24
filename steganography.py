from analizing import analize
import argparse
from encrypt import encrypt
from decrypt import decrypt
import os

secretInfo = "Not quick but flexable brown fox jumps over lazy dog. "
secretInfo = """
Etiam a erat at nunc dictum tincidunt tincidunt at nibh. In lacus quam, rutrum mattis leo non, cursus cursus nisi. Cras volutpat blandit lectus, id ultricies erat ornare hendrerit. Morbi eu iaculis magna. Donec dignissim finibus congue. Sed augue est, tempor vel cursus id, molestie elementum ligula. Nulla sodales convallis est, et sollicitudin lectus vulputate vitae. Phasellus porttitor nulla dolor, vel pellentesque nunc gravida at. Fusce elit tellus, auctor sit amet est non, semper ultricies purus. Nulla eu lorem iaculis, aliquam enim non, commodo massa. Maecenas sed tellus consectetur, maximus nisi id, commodo arcu. Sed sapien ex, auctor molestie risus non, consectetur vulputate ipsum.
"""

inputImgPath = os.path.join(os.path.curdir, "image.jpg")
outputImgPath = os.path.join(os.path.curdir, "newimage.png")

parser = argparse.ArgumentParser(description='Hide info in image.')
parser.add_argument('-d', '--decrypt', action="store_true",)
parser.add_argument('-a', '--analize', action="store_true",)
parser.add_argument('-e', '--encrypt', action="store_true",)
parser.add_argument('-i', '--imgPath', default=inputImgPath )
parser.add_argument('-m', '--mode', default="1b", type=str, help="Input 1b or 1bit for coding 1 bit \n 3b or 3bit for coding 3 bit \n 1B or 1Byte for coding full one byte to pixel")
parser.add_argument('-s', '--story', default=secretInfo, type=str, help="Input you story")
parser.add_argument('--length', default=-1, type=int, help="Input decrypt length > 0")


args = parser.parse_args()
algorithm = args.mode 


if args.decrypt:
    length = args.length if args.length > 0 else len(secretInfo)
    res = decrypt(args.imgPath, length, algorithm)
    print(f"Раcшифрована информация с файла {args.imgPath}:\n{res}")
elif args.encrypt:
    encrypt(args.imgPath, args.story, outputImgPath, algorithm)
    print(f"Зашифрована информация \"{args.story}\" в {outputImgPath}")
    if args.analize:
        analize(args.imgPath, outputImgPath)
else:
    print("Пу")

