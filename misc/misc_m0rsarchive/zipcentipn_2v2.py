from pwn import *
import glob,os

# fileName = glob.glob(f"*.zip")[0].lstrip(f"./")
dirTree = ""
fileIt = 999
io = process('sh')
def listDir(keyword = "",dir = "."):
    arr = []
    for f in glob.glob(f"{dir}/{keyword}"):
        arr.append(f.lstrip(f"{dir}/"))
    return arr

while True:
    io = process('sh')
    fileName = f"flag_{fileIt}.zip"
    print(f"{dirTree}{fileName}.zip")
    io.sendline(f"fcrackzip -b -c '1' -l 1-10 {dirTree}{fileName} -u")
    password = io.recvrepeat(timeout=15).decode().strip()[26:]
    print(password, fileName, dirTree)
    if "flag" in dirTree:
        io.sendline(f"unzip -o -qq -P {password} {dirTree}{fileName} -d {dirTree}")
    else:
        io.sendline(f"unzip -o -qq -P {password} {dirTree}{fileName}")
    print(io.recvrepeat(1).decode())
    dirTree+="flag/"
    fileIt-=1