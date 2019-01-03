import pickle
import numpy as np

with open("data.p", 'rb') as f:
    data=pickle.load(f)
    print(data[0:9])
    print(len(data))