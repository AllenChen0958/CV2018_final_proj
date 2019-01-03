import scipy.io
import numpy as np

# mat1 = scipy.io.loadmat('human_colormap.mat')
# mat2 = scipy.io.loadmat('000001_0.mat')
mat3 = scipy.io.loadmat('pose.mat')

# print(mat1)
# print("\n\n")
# print(mat2)

# ary = np.array(mat["colormap"])
# print(ary.shape)


print(mat3.keys())
print(mat3["candidate"].shape)
print(mat3["subset"].shape)
# print(mat3)

## save mat
# EX: scipy.io.savemat(mat_filename, {"segment":img})
