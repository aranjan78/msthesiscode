# import the necessary packages
from PIL import Image
import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--first", required=True,
            help="first input image")
ap.add_argument("-s", "--second", required=True,
            help="second")
args = vars(ap.parse_args())

imageA = Image.open(args["first"])
#box = (300, 300, 550, 550)
box = (440, 200, 700, 600)
imageB = imageA.crop(box) 
imageB.save(args["second"])
