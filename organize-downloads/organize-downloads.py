import os
import shutil
import filecmp
from tqdm import tqdm

# Default Variables
downloadPath = "E:\\Downloads\\"
fileTypes = {
    "Documents": ["doc", "docx", "xls", "xlxs", "ppt", "pptx", "pps", "ppsx", "pdf", "txt"],
    "Images": ["jpg", "jpeg", "png",  "gif", "bmp", "ico"],
    "Audio": ["mp3"],
    "Video": ["mp4", "mkv", "mpg","mpeg", "fla"],
    "Programs": ["exe", "msi"],
    "Compressed": ["zip", "rar", "7z"]
}

def createFolders():
    for fileType in fileTypes.keys():
        path = downloadPath + fileType
        if not os.path.exists(path):
            os.mkdir(path)
    path = downloadPath + "General"
    if not os.path.exists(path):
        os.mkdir(path)

def organize(file):
    # file may also be a directory
    # if directory then it moves to General
    if not (os.path.isdir(file) or file in fileTypes.keys() or file == "General"):
        fileExtension = file.split('.')[-1]
    else:
        return

    src = downloadPath + file
    for fileType in fileTypes:
        if fileExtension in fileTypes[fileType]:
            dest = downloadPath + fileType + "\\" + file
            if not os.path.isfile(dest):
                shutil.move(src, dest)
            elif os.path.isfile(dest) and filecmp.cmp(src, dest):
                # if the same file already exists
                os.remove(src)
            return

    dest = downloadPath + "General\\" + file
    if not os.path.isfile(dest):
        shutil.move(src, dest)
    elif os.path.isfile(dest) and filecmp.cmp(src, dest):
        os.remove(src)

if __name__ == "__main__":
    files = os.listdir(downloadPath)

    if len(files) > len(fileTypes) + 1:
        createFolders()
        for file in tqdm(files):
            organize(file)
        print("Organized !!!")
    else:
        print("Already Organized !!!")