from shutil import copyfile
import sys, os
import glob
from tqdm import tqdm


SOURCE_PATH = "/home/allenchen/dataset/lookbook/data"
DESTINATION_PATH = "/home/allenchen/temp/tmp_cv_final/VITON/data/women_top"
ORI_IMG_QUERY = "*CLEAN0*.jpg"
LIST_NAME = "/home/allenchen/temp/tmp_cv_final/VITON/data/image.txt"

# remove the image in the destination dir
print("Remove img in destination directory")
if os.path.isdir(DESTINATION_PATH):
    for img in glob.glob(os.path.join(DESTINATION_PATH, "*.jpg")):
        os.remove(img)

print("Copying and renaming file to destination")


try:
    label_set = dict()
    with open(LIST_NAME, "w") as f:
        for idx, ori_img in enumerate(tqdm(glob.glob(os.path.join(SOURCE_PATH, ORI_IMG_QUERY)))):
            # copy original image to desination directory
            ori_tar_name = "{:0>6d}_0.jpg".format(idx+1)
            # print("tarname:{}".format(ori_tar_name))
            copyfile(ori_img, os.path.join(DESTINATION_PATH,ori_tar_name))

            # query label image 
            pid = ori_img.split("_")[0]
            label_img_query= pid + "_" + "CLEAN1*.jpg"
            for i, img in enumerate(glob.iglob(os.path.join(SOURCE_PATH, label_img_query))):
                label_img = img
                if i >= 1:
                    raise LookupError('more than one label image')         
            # copy label image to desination directory or reuse old copied image
            lab_tar_name = None
            if not label_img in label_set:
                lab_tar_name = "{:0>6d}_1.jpg".format(idx+1)
                copyfile(label_img, os.path.join(DESTINATION_PATH,lab_tar_name))
                label_set.update({label_img:lab_tar_name})
                print("{} {}".format(ori_tar_name, lab_tar_name) ,file=f)
            else:
                lab_tar_name = label_set[label_img]
                print("{} {}".format(ori_tar_name, lab_tar_name) ,file=f)
                
        
except LookupError as error:
    print('Caught this error: ' + repr(error))