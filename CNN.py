import numpy as np
import pandas as pd 
from keras.preprocessing.image import ImageDataGenerator, load_img
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import random
import os
#print(os.listdir("C:/temp/DogsandCats/train"))

# define image related constants
FAST_RUN = False
IMAGE_WIDTH=128
IMAGE_HEIGHT=128
IMAGE_SIZE=(IMAGE_WIDTH, IMAGE_HEIGHT)
IMAGE_CHANNELS=3

# prepare training data

filenames = os.listdir("C:/temp/DogsandCats/train")
categories = []
for filename in filenames:
    category = filename.split('.')[0]
    if category == 'dog':
        categories.append(1)
    else:
        categories.append(0)

df = pd.DataFrame({
    'filename': filenames,
    'category': categories
})
# print(df.head())
#        filename  category
# 0     cat.0.jpg         0
# 1     cat.1.jpg         0
# 2    cat.10.jpg         0
# 3   cat.100.jpg         0
# 4  cat.1000.jpg         0
# block comment: Ctrl+K+C & Ctrl+K+U
