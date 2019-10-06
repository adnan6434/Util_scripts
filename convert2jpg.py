import os
import pathlib
from PIL import Image as im
import numpy as np
image_dim=224

path=r"D:\SNS-HDS database\sns images\skin\\"
path=pathlib.Path(path)
for img_file in path.rglob("*.png"):
        img = im.open(img_file)
        img=img.resize((image_dim,image_dim),im.ANTIALIAS)
        img=img.convert("RGB")
        print(img_file)
        #important solution
        img_file2=pathlib.Path(str(img_file).replace(img_file.name,img_file.name[:-3]+"jpg"))
        print(img_file2)
        img.save(img_file2)
        os.unlink(img_file)#deletes the png file
for img_file in path.rglob("*.bmp"):
        img = im.open(img_file)
        img=img.resize((image_dim,image_dim),im.ANTIALIAS)
        img=img.convert("RGB")
        print(img_file)
        #important solution
        img_file2=pathlib.Path(str(img_file).replace(img_file.name,img_file.name[:-3]+"jpg"))
        print(img_file2)
        img.save(img_file2)
        os.unlink(img_file)#deletes the bmp file
        
for img_file in path.rglob("*.jpeg"):
        img = im.open(img_file)
        img=img.resize((image_dim,image_dim),im.ANTIALIAS)
        img=img.convert("RGB")
        print(img_file)
        #important solution
        img_file2=pathlib.Path(str(img_file).replace(img_file.name,img_file.name[:-4]+"jpg"))
        print(img_file2)
        img.save(img_file2)
        os.unlink(img_file)#deletes the jpeg file
for img_file in path.rglob("*.jpg"):
        img = im.open(img_file)
        img=img.resize((image_dim,image_dim),im.ANTIALIAS)
        img=img.convert("RGB")
        print(img_file)
        #important solution
        img_file2=pathlib.Path(str(img_file).replace(img_file.name,img_file.name[:-3]+"jpg"))
        print(img_file2)
        img.save(img_file2)
