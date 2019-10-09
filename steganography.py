import argparse
from encrypt import encrypt
from decrypt import decrypt
import os

secretInfo = "i am sanya"
imgPath = os.path.join(os.path.curdir, "newimage.png")

print("Length of your secret message: ", len(secretInfo))


parser = argparse.ArgumentParser(description='Hide info in image.')
parser.add_argument('-d', '--decrypt', action="store_true",)
parser.add_argument('-e', '--encrypt', action="store_true",)
parser.add_argument('-i', '--image', )


args = parser.parse_args()

if args.decrypt:
    res = decrypt(imgPath)
    print(res)
elif args.encrypt:
    encrypt(imgPath, secretInfo)
else:
    print("Пу")

