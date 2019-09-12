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
bitmap = face.glyph.bitmap

for num in range(10):
    face.load_char( chr(ord('0')+num) )
    print("process char: %d"%num)
    
    height=bitmap.rows
    width=bitmap.width
    channel=1
    
    imgPath="images\\%d.png"%num
    imgPath=os.path.join(cwd,imgPath)
    img = np.zeros( (height,width,channel), np.uint8 )
    
    for row in range(height):
        for col in range(width):
            img[row][col] = 255 - bitmap.buffer[row*width + col]
    
    cv2.imwrite(imgPath,img)

#os.system("pause")
