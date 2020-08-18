import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
import matplotlib.pyplot as plt
import tensorflow as tf
import glob
import random
import math
from PIL import Image
import tflearn
from tflearn.data_utils import image_preloader
#%matplotlib inline

# data processing

IMAGE_FOLDER = 'C:/temp/DogsandCats/train'
VALIDATION_FOLDER = 'C:/temp/DogsandCats/test1'
TRAIN_DATA = 'C:/temp/DogsandCats/train/training_data.txt'
TEST_DATA = 'C:/temp/DogsandCats/train/test_data.txt'
VALIDATION_DATA = 'C:/temp/DogsandCats/test1/validation_data.txt'
train_porportion = 0.9
test_porportion = 0.1
#validation_proportion = 0.1

filenames_image = os.listdir(IMAGE_FOLDER)
random.shuffle(filenames_image)

total = len(filenames_image)
fr = open(TRAIN_DATA, 'w')
train_files = filenames_image[0: int(train_porportion*total)]
for filename in train_files:
    if filenames[0:3] == 'cat':
        fr.write()
