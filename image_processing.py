import os,cv2,pathlib,glob,random,shutil
from PIL import Image as im
import numpy as np
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True


image_dim=300
global dir
dir=r"E:\tibot-ml-experiments\NDS_classifier\Google -1\\"
dir2=dir+"renamed\\"
def encodetoutf(dir):
    str(dir).encode("utf-8")
    return dir
def rename_files():
    print("File renaming started")
    files=list(glob.iglob(os.path.join(dir,"*.jpg")))
    if(os.path.isdir(dir2)):
       pass
    else: 
        os.makedirs(dir2,mode=0o777, exist_ok=False)
    for i,img_file in enumerate(files):
        dst = dir2+str(i+1)+ ".jpg"
        os.rename(img_file, dst)
    files=list(glob.iglob(os.path.join(dir2,"*.jpg")))
    for i,img_file in enumerate(files):
        shutil.move(img_file, dir, shutil.copy2)
    os.rmdir(dir2)
def convert2jpg():
    print("file conversion started")
    path=pathlib.Path(dir)
    for img_file in path.rglob("*.png"):
        try:
            img = im.open(img_file)
            img=img.resize((image_dim,image_dim),im.ANTIALIAS)
            img=img.convert("RGB")
            print(img_file)
            #important solution
            img_file2=pathlib.Path(str(img_file).replace(img_file.name,img_file.name[:-3]+"jpg"))
            print(img_file2)
            img.save(img_file2)
            os.unlink(img_file)#deletes the png file
        except OSError:
            os.unlink(img_file)
    for img_file in path.rglob("*.bmp"):
        try:
            img = im.open(img_file)
            img=img.resize((image_dim,image_dim),im.ANTIALIAS)
            img=img.convert("RGB")
            print(img_file)
            #important solution
            img_file2=pathlib.Path(str(img_file).replace(img_file.name,img_file.name[:-3]+"jpg"))
            print(img_file2)
            img.save(img_file2)
            os.unlink(img_file)#deletes the bmp file
        except OSError:
            os.unlink(img_file)
    for img_file in path.rglob("*.jpeg"):
        try:
            img = im.open(img_file)
            img=img.resize((image_dim,image_dim),im.ANTIALIAS)
            img=img.convert("RGB")
            print(img_file)
            #important solution
            img_file2=pathlib.Path(str(img_file).replace(img_file.name,img_file.name[:-4]+"jpg"))
            print(img_file2)
            img.save(img_file2)
            os.unlink(img_file)#deletes the jpeg file
        except OSError:
            os.unlink(img_file)
    for img_file in path.rglob("*.jpg"):
        try:
            img = im.open(img_file)
            img=img.resize((image_dim,image_dim),im.ANTIALIAS)
            img=img.convert("RGB")
            
        except OSError:
            os.unlink(img_file)
    for img_file in path.rglob("*.gif"):
            os.unlink(img_file)

def clean_grayscale():
    print("cleaning grayscale started")
    files=list(glob.iglob(os.path.join(dir,"*.jpg")))
    count=0
    for i,image in enumerate(files):
        im_path=image
        image=im.open(image)
        img=np.array(image)
        if(len(img.shape)!=3):
         print(img.shape)
         count+=1
         print(im_path)
         os.remove(im_path)
    print(count)
def image_resizer():
    print("image resize started")
    path=pathlib.Path(dir)
    count=0
    for img_file in path.rglob("*.jpg"):
       img = im.open(img_file)
       if(np.shape(img)==(image_dim,image_dim,3)):
           #print(np.shape(img))
           count=count+1
           pass
       else:
           #print(np.shape(img))
           img=img.resize((image_dim,image_dim),im.ANTIALIAS)
           img=img.convert("RGB")
           img.save(img_file)
           
    print(count)
 
#rename_files() 
convert2jpg()
clean_grayscale()
image_resizer()
