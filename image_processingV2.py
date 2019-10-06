import os,cv2,pathlib,glob,random,shutil
from PIL import Image as im
import numpy as np
from PIL import ImageFile
from builtins import FileNotFoundError
ImageFile.LOAD_TRUNCATED_IMAGES = True
import concurrent.futures
import time
import itertools
image_dim=300

dir=r"C:\Users\tibot\Downloads\Aiwowo___Google_Search\\"
dir2=dir+"renamed\\"
formats=['png','bmp','jpeg','gif','jpg']
f_format='jpg'
global fmt_len
fmt_len=0
def encodetoutf(dir):
    str(dir).encode("utf-8")
    return dir
def processImage(img_file):
    try:  
       with im.open(img_file) as img:
           if(len(np.shape(img))==3):
               if(np.shape(img)[2]==3):
                    if(np.shape(img)==(image_dim,image_dim,3)):
                       #print("not re"+str(np.shape(img)))
                       pass
                    else:
                       #print("re"+str(np.shape(img)))
                       img=img.resize((image_dim,image_dim),im.ANTIALIAS)
                       img.save(img_file)
               else:
                    print("Odd shape"+str(np.shape(img)))
                    os.unlink(img_file)
           else:
               print("grayscale:"+str(np.shape(img)))
               img.close()
               os.unlink(img_file)    
    except FileNotFoundError:
        pass
    except OSError:
        os.unlink(img_file)
    
def processAndConvert(img_file,fmt_len):
    try:  
       with im.open(img_file) as img:
           if(len(np.shape(img))==3):
               if(np.shape(img)[2]==3):
                    if(np.shape(img)==(image_dim,image_dim,3)):
                       #print("not re"+str(np.shape(img)))
                       pass
                    else:
                       #print("re"+str(np.shape(img)))
                       img=img.resize((image_dim,image_dim),im.ANTIALIAS)
                    img_file2=img_file[:-fmt_len]+f_format
                    if(os.path.isfile(img_file2)):
                        img_file2=img_file[:-fmt_len-1]+'c.'+f_format
                    img.save(img_file2)
                    os.unlink(img_file)#deletes the file
               else:
                    print("Odd shape"+str(np.shape(img)))
                    os.unlink(img_file)
           else:
               print("grayscale:"+str(np.shape(img)))
               os.unlink(img_file)    
    except FileNotFoundError:
        pass
    except OSError:
        os.unlink(img_file)
    
    
def parallel_processing(func,list,fmt_len=None):
    if(fmt_len==None):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            for list_obj in zip(list, executor.map(func, list)):
                pass
    else:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            for list_obj in zip(list, executor.map(func, list,itertools.repeat(fmt_len))):
                pass
        
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
def convertImage():
    print("file conversion started")
    path=pathlib.Path(dir)
    for format in formats:
        img_files=list(str(i) for i in path.rglob("*."+format))
        print(img_files)
        fmt_len=len(format)
        if(format=='gif'):
            parallel_processing(os.unlink,img_files)
            print("done")
        elif(format==f_format):
            parallel_processing(processImage,img_files)   
        else:
            parallel_processing(processAndConvert,img_files,fmt_len)
    

 
#rename_files() 
convertImage()

