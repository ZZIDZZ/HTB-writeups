from pwn import *
import glob
from PIL import Image

fileName = "flag/pwd.png"
im = Image.open(fileName)
width,height = im.size
im_rgb = im.convert('RGB')
pix = im_rgb.load()
morseFromImg = ""
morse = ""
bgColor = pix[0,0]
count = 0
for i in range(1,height-1,2):
    for j in range(1,width-1):
        print(pix[j,i])
        if bgColor!=pix[j,i]:
            count += 1
        else:
            if count==1:
                morse+="."
            elif count == 3:
                morse+="-"
            count = 0
morseArr = morse.split(" ")
print(morseArr)