import os
import shutil

path = input("Enter the name of your directory")

list_of_files = os.listdir(path)
for x in list_of_files:
    name,ext = os.path.splitext(x)
    ext = ext[1:]

    if ext == '':
        continue

    if os.path.exists(path + '/' + ext):
        shutil.move(path+'/'+x, path+'/'+ext+'/'+x)

    else:
        os.makedirs(path + '/' + ext)
        shutil.move(path+'/'+x, path+'/'+ext+'/'+x)