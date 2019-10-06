import os,cv2,pathlib,shutil
from PIL import Image as im
import numpy as np
from PIL import ImageFile
import concurrent.futures
ImageFile.LOAD_TRUNCATED_IMAGES = True


dir=r"D:\Food_imgs_download_30_9_3\\"
path=pathlib.Path(dir)
img_files=list(str(i) for i in path.rglob("*.jpg"))
#img_files.reverse()
image_dim=300
print(len(img_files))
def image_resizer(img_file):
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
                       img=img.convert("RGB")
                       img.save(img_file)
               else:
                    print("Odd shape"+str(np.shape(img)))
                    os.unlink(img_file)
           else:
               print("grayscale:"+str(np.shape(img)))
               os.unlink(img_file)    
   except (PermissionError,FileNotFoundError):
       pass
   except OSError:
        os.unlink(img_file)
   finally:
       pass
def parallel_resizer(func,list): 
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for list_obj in zip(list, executor.map(func, list)):
            pass
parallel_resizer(image_resizer, img_files)