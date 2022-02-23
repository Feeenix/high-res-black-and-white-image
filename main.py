from install_package import *
import sys, math
import os
from config import *

def main():
    pass
    install_package("numpy","opencv-python")
    sys.path.append("libraries")
    import cv2
    import numpy as np


    print(sys.argv)
    if len(sys.argv) > 1:
        file = sys.argv[1]
    print("⠀")
    print((ord("⠀")+0))
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print ("".join([chr(i+10240) for i in range(256)]))

    if not os.path.isdir(in_dir): os.mkdir(in_dir)
    if not os.path.isdir(out_dir): os.mkdir(out_dir)

    im = np.sum(cv2.imread(img_file),axis=2)>384
    print(im)


























if __name__ == "__main__":
    main()
