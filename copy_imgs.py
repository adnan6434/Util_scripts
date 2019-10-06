from shutil import copytree as copydir
import os

src=r"F:\food all things\dataset256\UECFOOD256\\"
dst=r"F:\food all things\dataset256\Food256\\"


copydir(src,dst,symlinks=True)
if (os.path.isdir(dst)):
    pass
else:
    pass
    os.makedirs(dst, mode=0o777, exist_ok=True)
    copydir(src,dst,symlinks=True)