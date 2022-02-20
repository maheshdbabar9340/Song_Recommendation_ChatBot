#! /usr/bin/env python3

import sys
import os
import PIL
from PIL import Image

def get_images():
    extentions = ["png", "jpg", "jpeg", "gif", "bmp"]
    final_list = []
    k = os.listdir()
    for i in k:
        if os.path.isfile(i):
            fext = i.split(".")[-1]
            if fext in extentions:
                final_list.append(i)
    return final_list

def convert(img_name, width, height, idx):
    img = Image.open(img_name)
    img = img.resize((width, height))
    img.save("resized_images/" + str(idx) + ".jpg")
    print("resized file " + img_name)

if __name__ == "__main__":
    k = get_images()
    print("the files availabe to resize are ", end = "")
    print(k)
    width, height = map(int, input("enter the width and height of your choice : ").split())
    os.mkdir("resized_images")
    num = 1
    for i in k:
        convert(i, width, height, num)
        num += 1
    print("conversion complete");
    print("all resizable images are stored in resized_images folder")
