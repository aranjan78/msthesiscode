import argparse
import torch
from PIL import Image
import os

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-p0','--path0', type=str, default='./imgs/ex_ref.png')
parser.add_argument('-p1','--path1', type=str, default='./imgs/ex_p0.png')
parser.add_argument('-p2','--path2', type=str, default='./imgs/ex_p1.png')

opt = parser.parse_args()

image = Image.open(opt.path0)
image1 = Image.open(opt.path1)

image1 = image1.resize(image.size)
image1.save(opt.path2)
print(os.listdir("."))

