import scipy.io
import numpy as np
import skimage.io
import glob
import os
from lip_visualize import draw_mask
import threading
import cv2
import time
"""
1. Hat                                                                                                                                                                                                 
2. Hair                                                                                                                                                                                                
3. Glove                                                                                                                                                                                               
4. Sunglasses                                                                                                                                                                                          
5. UpperClothes                                                                                                                                                                                        
6. Dress                                                                                                                                                                                               
7. Coat                                                                                                                                                                                                
8. Socks                                                                                                                                                                                               
9. Pants                                                                                                                                                                                               
10.Jumpsuits                                                                                                                                                                                          
11.Scarf                                                                                                                                                                                              
12.Skirt                                                                                                                                                                                              
13.Face                                                                                                                                                                                               
14.Left-arm                                                                                                                                                                                           
15.Right-arm                                                                                                                                                                                          
16.Left-leg                                                                                                                                                                                           
17.Right-leg                                                                                                                                                                                          
18.Left-shoe                                                                                                                                                                                          
19.Right-shoe  
"""
table={
    "Background": 0,
    "Hat" :       1,
    "Hair":       2,
    "Glove":      3,
    "Sunglasses": 4,
    "UpperCloth": 5,
    "Dress":      6,
    "Coat":       7,
    "Socks":      8,
    "Pants":      9,
    "Jumpsuits":  10,
    "Scarf":      11,
    "Skirt":      12,
    "Face":       13,
    "Left-arm  ": 14,
    "Right-arm ": 15,
    "Left-leg  ": 16,
    "Right-leg ": 17,
    "Left-shoe ": 18,
    "Right-shoe": 19,
    "Merged":     3 ## self defined label

}
IMAGE_DIR = "/home/allenchen/temp/tmp_cv_final/test/VITON_small_set/data/segment"
TAR_DIR = "/home/allenchen/temp/tmp_cv_final/test/VITON_small_set/data/merged_label"

if not os.path.exists(TAR_DIR):
    os.makedirs(TAR_DIR)
    

### merge label

def process_image_thread(img_path):
    img = skimage.io.imread(img_path)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            # Hat -> Hair
            if img[i][j]==table["Hat"]:
                img[i][j] = table["Hair"]
            # Sunglass -> Face
            elif img[i][j]==table["Sunglasses"]:
                img[i][j] = table["Face"]
            elif img[i][j]==table["UpperCloth"] or img[i][j]==table["Background"]:
                pass
            else:
                img[i][j] = table["Merged"]
    
    img_draw = draw_mask(img)
    filename = os.path.basename(img_path)
    skimage.io.imsave(os.path.join(TAR_DIR, filename), img_draw)

    mat_filename = filename.replace(".png", ".mat")
    scipy.io.savemat(mat_filename, {"segment":img})
    # print("finished saveing file: {}".format(filename))

# tstart = time.time()
# for img_path in glob.glob(os.path.join(IMAGE_DIR, "*.png")):
#     threading.Thread(target=process_image_thread, args=(img_path,)).start()
# tEnd = time.time()
# print("multithread: ".format(tEnd - tstart))

############

tstart = time.time()
for img_path in glob.glob(os.path.join(IMAGE_DIR, "*.png")):
    # threading.Thread(target=process_image_thread, args=(img_path,)).start()
    process_image_thread(img_path)
tEnd = time.time()
print("single thread:{}".format(tEnd - tstart))


#######################################################################################
# for img_path in glob.glob(os.path.join(IMAGE_DIR, "*.png")):
    
    
#     img = skimage.io.imread(img_path)
#     for i in range(img.shape[0]):
#         for j in range(img.shape[1]):
#             # Hat -> Hair
#             if img[i][j]==table["Hat"]:
#                 img[i][j] = table["Hair"]
#             # Sunglass -> Face
#             elif img[i][j]==table["Sunglasses"]:
#                 img[i][j] = table["Face"]
#             elif img[i][j]==table["UpperCloth"] or img[i][j]==table["Background"]:
#                 pass
#             else:
#                 img[i][j] = table["Merged"]
    
#     # ### resize to 641*641
#     # img = cv2.resize(img, (641,641))
    
#     img = draw_mask(img)
#     filename = os.path.basename(img_path)
#     skimage.io.imsave(os.path.join(TAR_DIR, filename), img)
#     # break



# crop image