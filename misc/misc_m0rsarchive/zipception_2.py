from pwn import *
import glob,os
from PIL import Image

# fileName = glob.glob(f"*.zip")[0].lstrip(f"./")
dirTree = "flag/"
fileIt = 651
io = process('sh')
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                        'C':'-.-.', 'D':'-..', 'E':'.',
                        'F':'..-.', 'G':'--.', 'H':'....',
                        'I':'..', 'J':'.---', 'K':'-.-',
                        'L':'.-..', 'M':'--', 'N':'-.',
                        'O':'---', 'P':'.--.', 'Q':'--.-',
                        'R':'.-.', 'S':'...', 'T':'-',
                        'U':'..-', 'V':'...-', 'W':'.--',
                        'X':'-..-', 'Y':'-.--', 'Z':'--..',
                        '1':'.----', '2':'..---', '3':'...--',
                        '4':'....-', '5':'.....', '6':'-....',
                        '7':'--...', '8':'---..', '9':'----.',
                        '0':'-----', ', ':'--..--', '.':'.-.-.-',
                        '?':'..--..', '/':'-..-.', '-':'-....-',
                        '(':'-.--.', ')':'-.--.-'}
def listDir(keyword = "",dir = "."):
    arr = []
    for f in glob.glob(f"{dir}/{keyword}"):
        arr.append(f.lstrip(f"{dir}/"))
    return arr

def get_key(val):
    for key, value in MORSE_CODE_DICT.items():
         if val == value:
             return key

def decodeMorse(morse):
    return([get_key(i) for i in morse])

while True:
    io = process('sh')
    fileName = f"flag_{fileIt}.zip"
    print(f"{dirTree}{fileName}")
    im = Image.open(dirTree+"pwd.png")
    width,height = im.size
    im_rgb = im.convert('RGB')
    pix = im_rgb.load()
    morseFromImg = ""
    morse = ""
    bgColor = pix[0,0]
    count = 0
    for i in range(1,height-1,2):
        for j in range(1,width-1):
            if bgColor!=pix[j,i]:
                count += 1
            else:
                if count==1:
                    morse+="."
                elif count == 3:
                    morse+="-"
                count = 0
        morse+= " "
    morseArr = morse.strip().split(" ")
    print(morseArr, decodeMorse(morseArr))
    password = "".join(decodeMorse(morseArr)).lower()
    print(password, fileName, dirTree)
    if "flag" in dirTree:
        io.sendline(f"unzip -o -qq -P {password} {dirTree}{fileName} -d {dirTree}")
    else:
        io.sendline(f"unzip -o -qq -P {password} {dirTree}{fileName}")
    print(io.recvrepeat(1).decode())
    dirTree+="flag/"
    fileIt-=1

