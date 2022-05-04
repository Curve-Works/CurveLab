import os
import config
import shutil

def mkdir(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)

if __name__ == '__main__':
