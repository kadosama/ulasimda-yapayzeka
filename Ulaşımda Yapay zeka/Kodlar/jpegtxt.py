# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 22:12:26 2021

@author: Ezgi
"""

import glob

imglist = glob.glob("volov4/darknet/cov_data/cov_images/*.jpg", recursive=False)

with open("volov4/darknet/cov_data/train.txt", 'w', encoding = 'utf-8') as f:
	for img in imglist:
		img = img.replace("\\", "/")

		f.write(img + '\n')