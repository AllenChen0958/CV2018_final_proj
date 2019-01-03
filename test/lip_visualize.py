import scipy.io
import numpy as np
import skimage.io
import glob
import os
IMAGE_DIR = "/home/allenchen/temp/tmp_cv_final/test/segment"
TAR_DIR = "/home/allenchen/temp/tmp_cv_final/test/segment/visualize"


mat = scipy.io.loadmat('human_colormap.mat')
test_img = scipy.io.loadmat('000001_0.mat')



def draw_mask(image, color_mat=mat["colormap"]):
    image = image.astype(np.int32)
    result = np.zeros([image.shape[0], image.shape[1], 3])
    for i in range(len(color_mat)):
        result[np.where(image==i)] = color_mat[i]
    return result



# mat = scipy.io.loadmat('000001_0.mat')
# ary = mat["segment"]
# ary = ary.astype(np.int32)
# c = []
# for i in range(ary.shape[0]):
#     for j in range(ary.shape[1]):
#         if(ary[i][j])!=0 and ary[i][j] not in c:
#             c.append(ary[i][j])
# print(c)
# ary = ary*255
# ary = ary.astype(np.int32)
# print(ary.shape)
# skimage.io.imsave("seg.png", ary)

def visualize_mat(mat, width=256, each_height=25, filename="mat.png"):
    # print(mat.shape)
    # print(mat)
    # print(np.repeat(mat, width, axis=1))
    # print(np.repeat(mat, height, axis=0))
    result = np.zeros([each_height*mat.shape[0], width, 3])
    # for i in range(mat.shape[0]):
    #     result[:,i*height : (i+1)*height,:]= mat[i]
    # print(result)
    # result = np.repeat(mat, 2, axis=0)
    
    for i in range(mat.shape[0]):
        for j in range(width):
            for k in range(i*each_height,(i+1)*each_height):
                result[k, j,:]=mat[i]
    if(filename is not None):
        skimage.io.imsave(filename, result)
    return result

            

def main():
    
    img = draw_mask(test_img["segment"], mat["colormap"])
    skimage.io.imsave("seg.png", img)
    # visualize_mat(mat["colormap"], filename="mat.png")

    # for img_path in glob.glob(os.path.join(IMAGE_DIR, "*.png")):
    #     img = skimage.io.imread(img_path)
    #     v = draw_mask(img, mat["colormap"])
    #     filename = os.path.basename(img_path)
    #     filename = os.path.join(TAR_DIR, filename)
    #     skimage.io.imsave(filename, v)

if __name__ == "__main__":
    main()