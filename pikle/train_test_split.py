from tqdm import tqdm
import os
PATH = "/home/allenchen/temp/tmp_cv_final/VITON/data"
IMAGE_LIST_NAME = "image.txt"
TRAIN_PAIR_NAME = "viton_train_pairs.txt" 
TEST_PAIR_NAME = "viton_test_pairs.txt"
DUMMY_IMAGE_NAME = "viton_train_images.txt"
TRAIN_TEST_SPLIT= 0.1

ratio = int(1/TRAIN_TEST_SPLIT)
with open(os.path.join(PATH, IMAGE_LIST_NAME), "r") as image_f, open(os.path.join(PATH, TRAIN_PAIR_NAME), "w") as train_pair_f, open(os.path.join(PATH, TEST_PAIR_NAME), "w") as test_pair_f, open(os.path.join(PATH, DUMMY_IMAGE_NAME), "w") as dummy_f:
    lines = image_f.readlines()
    
    for i, img in enumerate(tqdm(lines)):
        if (i+1)%ratio==0:
            print(img, file=test_pair_f, end='')
        else:
            print(img, file=train_pair_f, end='')
        
            # can be replaced with simply copy viton_train_pairs.txt and rename as viton_train_images.txt
            print(img, file=dummy_f, end='')


