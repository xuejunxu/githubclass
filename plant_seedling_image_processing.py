#This script processes with images. It reads jpeg files and 
#convert all the images files into csv format

import os

import pandas as pd

import numpy as np

import cv2

import matplotlib.pyplot as plt

train_path = 'C:/jiaocai/Other/Plant Seedling Classification/train/'
#storing the training path of plant seedling files

#image_per_class is a dictionary storing data of images
image_per_class = {}
for class_name in os.listdir(train_path):
    class_path = train_path+str(class_name)
    class_tag = class_name
    image_per_class[class_tag] = []
    for image in os.listdir(class_path):
        image_path=class_path+'/'+str(image)
        #print(image_path)
        image_col = cv2.imread(image_path, cv2.IMREAD_COLOR)
        image_per_class[class_tag].append(image_col)

#print the number of images in each class in the train set
for key,value in image_per_class.items():
    print("{0} -> {1}".format(key, len(value)))

#get to know the properties of images
print(image_per_class['Maize'][0])
print(len(image_per_class['Maize'][0]))

print('---------------------------------------')

#print out certain image to check manually
cv2.imshow('image',image_per_class['Maize'][0])
cv2.waitKey(0)

#change the image files in image_per_class into a numpy.array format
#for keys in image_per_class[keys]:
    
