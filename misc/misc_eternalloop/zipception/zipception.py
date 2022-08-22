from pwn import *
import glob,shutil,os

# zipDirName = "zipception"

fileName = glob.glob(f"*.zip")[0].lstrip(f"./")
io = process('sh')
def listDir(keyword = "",dir = "."):
    arr = []
    for f in glob.glob(f"{dir}/{keyword}"):
        arr.append(f.lstrip(f"{dir}/"))
    return arr

while True:
    io.sendline(f"unzip -Z1 {fileName}")
    fileNamePass = io.recvrepeat(1).decode().strip()
    zipdir = listDir(keyword="*.zip")
    print(zipdir)
    io.sendline(f"unzip -q -P {fileNamePass[:-4]} {fileName}")
    print(io.recvrepeat(1).decode())
    os.remove(fileName)
    print(fileName, fileNamePass)
    fileName = fileNamePass
    if fileName=="6969.zip":
        break