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
    img_file_ = img_file
    out_file_ = out_file
    print(img_file_)
    print(sys.argv)
    if len(sys.argv) > 1:
        img_file_ = sys.argv[1]
        if len(sys.argv) > 2:
            out_file_ = sys.argv[2]
    # print("⠀")
    # print((ord("⠀")+0))
    # print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    # print ("".join([chr(i+10240) for i in range(256)]))

    if not os.path.isdir(in_dir): os.mkdir(in_dir)
    if not os.path.isdir(out_dir): os.mkdir(out_dir)

    bw_im = np.sum(cv2.imread(img_file_),axis=2)>threshold
    # print(bw_im)


    vt_group = np.array([bw_im[i*4:i*4+4] for i in range(math.ceil(len(bw_im)/4))])

    hz_group = np.array([[
    chr(10240+ a[0][b*2+0]*1 + a[1][b*2+0]*2 + a[2][b*2+0]*4 + a[0][b*2+1]*8 + a[1][b*2+1]*16 + a[2][b*2+1]*32 + a[3][b*2+0]*64 + a[3][b*2+1]*128 )
    for b in range(math.ceil(len(a[0])/2))]
    for a in vt_group ])
    # print (hz_group)
    text = "\n".join(["".join(a) for a in hz_group])
    with open(out_file_, "w",encoding="utf-16") as f:
        f.write(text)



























if __name__ == "__main__":
    main()
