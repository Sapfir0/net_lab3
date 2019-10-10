import argparse
from encrypt import encrypt
from decrypt import decrypt
import os

secretInfo = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus luctus, ipsum et interdum volutpat, diam est fringilla ligula, at euismod arcu elit nec odio. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Mauris convallis id metus non viverra. Quisque quis aliquam sapien. Maecenas molestie semper porta. Nullam pretium libero augue, sed porttitor elit egestas non. Nam eget ipsum eget ligula pulvinar commodo. Mauris pretium gravida fermentum. \
Vivamus vel tristique metus, at dapibus sem. Aenean sollicitudin eu arcu non lacinia. Praesent posuere semper ante, vel convallis felis dignissim ut. In facilisis mi nisl, viverra congue tortor bibendum a. Nulla facilisi. Interdum et malesuada fames ac ante ipsum primis in faucibus. Duis ut tempor massa. \
Cras eu arcu at mi lacinia auctor ut in felis. Donec id aliquam dolor. Ut fermentum elementum purus eu tincidunt. Ut non enim iaculis, consectetur dolor a, vehicula odio. Cras vel sapien a justo eleifend gravida nec non risus. Donec vulputate vel felis a gravida. Duis dapibus ligula sit amet nibh bibendum, sit amet scelerisque quam lacinia. \
Duis non cursus ipsum, et commodo mi. Etiam finibus sagittis sollicitudin. Donec eget blandit diam. Sed finibus, sapien eu egestas viverra, ipsum turpis congue risus, sit amet tempus diam neque at orci. Cras ante urna, efficitur et accumsan id, tincidunt vitae elit. Nam nec aliquet nisi. In non ullamcorper dolor. Aenean a tortor quis nisi viverra eleifend. Aenean nec nisl eu ex scelerisque bibendum. Aliquam sit amet rhoncus eros. Praesent finibus hendrerit dui sit amet dapibus. Donec sagittis elit a consequat iaculis. Morbi eu neque eget quam faucibus euismod ac ac metus. Sed blandit felis tempor porttitor pellentesque. \
Duis a turpis odio. Pellentesque sollicitudin augue purus, ac sodales nunc mattis ut. Etiam consectetur eleifend blandit. Mauris at neque tempus, suscipit nisi at, viverra felis. Nunc at augue ac justo porttitor vestibulum. Sed posuere risus ac neque egestas, et tempor ligula lacinia. Nullam finibus neque sem, et bibendum velit posuere eu. Proin vel eros ornare, condimentum justo ut, imperdiet nulla. Nullam id accumsan sem. Maecenas non enim in metus dictum lacinia id id massa. Suspendisse rutrum, metus aliquet aliquet faucibus, ex sapien bibendum diam, quis tincidunt neque metus ut eros. Nunc non mauris tristique, semper orci nec, suscipit justo. "

inputImgPath = os.path.join(os.path.curdir, "image.jpg")
outputImgPath = os.path.join(os.path.curdir, "newimage.png")

parser = argparse.ArgumentParser(description='Hide info in image.')
parser.add_argument('-d', '--decrypt', action="store_true",)
parser.add_argument('-e', '--encrypt', action="store_true",)
parser.add_argument('-i', '--imgPath', default=inputImgPath )


args = parser.parse_args()
if args.decrypt:
    res = decrypt(args.imgPath)
    print("Раcшифрована информация с файла",  res, "в", args.imgPath)
elif args.encrypt:
    encrypt(args.imgPath, secretInfo, outputImgPath)
    print("Зашифрована информация", secretInfo, "в", outputImgPath)
else:
    print("Пу")

