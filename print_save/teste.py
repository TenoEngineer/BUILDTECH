import sys
from os import path, mkdir, listdir
import shutil

user_path = path.expanduser('~')
new_folder = path.join(user_path, 'CALCULOS')
print(listdir(user_path))
if 'CALCULOS' not in listdir(user_path):
    mkdir(new_folder)
else:
    shutil.rmtree(new_folder)