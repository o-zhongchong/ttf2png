#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import freetype
import cv2
import numpy as np

cwd = os.path.abspath( os.path.join( sys.path[0],"..") )
os.chdir(cwd)

ttf_file_path = os.path.join( cwd,"ttf\\OCR-B-10 BT.ttf")
font_size = 48

face = freetype.Face(ttf_file_path)
face.set_char_size(font_size * 64)
slot = face.glyph

text = "0123456789abcdefghijklmnokprstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

width,height,baseline = 0,0,0
# compute bbox
for i,c in enumerate(text):
    face.load_char(c)
    bitmap = slot.bitmap
    baseline = max(baseline, max(0,-(slot.bitmap_top-bitmap.rows)))
    height = max(height, bitmap.rows + baseline)
    width += (slot.advance.x >> 6)

imgPath="images\\_charmaps.png"
imgPath=os.path.join(cwd,imgPath)
img = np.zeros( (height,width,1), np.uint8 )
img.fill(255)

x,y = 0,0
# rendering and save image
for i,c in enumerate(text):
    print("process char: %c"%c)
    face.load_char(c)
    
    bitmap = slot.bitmap
    top = slot.bitmap_top
    left = slot.bitmap_left
    h=bitmap.rows
    w=bitmap.width
    
    y = height-baseline-top
    x += left
    
    for i in range(h):
        for j in range(w):
            img[y+i][x+j] = 255 - bitmap.buffer[i*w + j]
    x = x + (slot.advance.x >> 6) - left

cv2.imwrite(imgPath,img)

#os.system("pause")
