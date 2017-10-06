import cv2
import numpy as np
import glob, os

#filename = "../data/train/masks/2__mask_00014.png" #hero
#filename = "../data/train/masks/1__mask_00101.png" #no hero

img_dir = "../data/data_pack2/masks/"

total_files = 0
total_hero = 0

os.chdir(img_dir)
for file in glob.glob("*.png"):
	total_files +=1

	img = cv2.imread(file)

	#print (img.shape)
	blue = img[:,:,0]
	#print (blue)

	if np.any(blue == 255):
		total_hero += 1



percent_hero = 100. * total_hero / total_files

print (percent_hero, "percent of files contain the hero")