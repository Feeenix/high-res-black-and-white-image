from install_package import *
import sys, math
import os
from config import *

def main():

    install_package("numpy","opencv-python")
    sys.path.append("libraries")
    import cv2
    import numpy as np
    img_file_ = img_file
    out_file_ = out_file
    threshold_= threshold
    print(img_file_)
    print(sys.argv)
    if len(sys.argv) > 1:
        img_file_ = sys.argv[1]
        if len(sys.argv) > 2:
            out_file_ = sys.argv[2]
            if len(sys.argv) > 3:
                threshold_ = int(sys.argv[3])

    if threshold_>=256*3:
        raise ValueError("threshold must be less than "+str(256*3)+", value given: "+str(threshold_))

    if not os.path.isdir(in_dir): os.mkdir(in_dir)
    if not os.path.isdir(out_dir): os.mkdir(out_dir)

    # Load the image into a 3d array
    bw_im = np.sum(cv2.imread(img_file_),axis=2)>threshold_

    # make the height and width a multiple of 4 and 2
    while len(bw_im)%4:
        bw_im = np.vstack((bw_im, np.array([False for i in range(len(bw_im[0]))])) )
    while len(bw_im[0])%2:
        bw_im = np.hstack((bw_im, np.array([[False,] for i in range(len(bw_im))])) )


    # turn the image data into braille
    vt_group = np.array([bw_im[i*4:i*4+4] for i in range(math.ceil(len(bw_im)/4))])
    hz_group = np.array([[
    chr(10240+ a[0][b*2+0]*1 + a[1][b*2+0]*2 + a[2][b*2+0]*4 + a[0][b*2+1]*8 + a[1][b*2+1]*16 + a[2][b*2+1]*32 + a[3][b*2+0]*64 + a[3][b*2+1]*128 )
    for b in range(math.ceil(len(a[0])/2))]
    for a in vt_group ])

    text = "\n".join(["".join(a) for a in hz_group])

    # output the braille
    print(text)
    with open(out_file_, "w",encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
