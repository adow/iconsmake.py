#!/usr/bin/python
#coding=utf-8
# Make icons with different size for iOS
#
# ln -s /PATH_OF_ICONSMAKE/iconsmake.py  /usr/bin/iconsmake
# Put an original icon named Icon-1024.png(size 1024*1024) into folder, and run $ iconsmake

import os
import sys
import re
import random
import getopt
from PIL import Image

def resizer_icon_to_small(image_input,output_filename,output_size):
    input_width=image_input.size[0]
    input_height=image_input.size[1]
    if input_width!=1024 or input_height!=1024:
        print "Input image should be 1024*1024"
        exit(1)
    image_output=image_input.resize((output_size,output_size),Image.ANTIALIAS)
    output_file=open(output_filename,'wb+')
    image_output.save(output_file,image_input.format,quality=95)
    output_file.close()

def resizer_folder():
    icon_1024="Icon-1024.png"
    if not os.path.exists(icon_1024):
        print 'Icon-1024.png not exist'
        exit(1)
    file_1024=open(icon_1024)
    image_1024=Image.open(file_1024)
    resizer_icon_to_small(image_1024,'Icon.png',57)
    resizer_icon_to_small(image_1024,'Icon@2x.png',114)
    resizer_icon_to_small(image_1024,'Icon-72.png',72)
    resizer_icon_to_small(image_1024,'Icon-114.png',114)
    resizer_icon_to_small(image_1024,'Icon-500.png',500)
    resizer_icon_to_small(image_1024,'Icon-512.png',512)
    resizer_icon_to_small(image_1024,'Icon-Small-50.png',50)
    resizer_icon_to_small(image_1024,'Icon-Small.png',29)
    resizer_icon_to_small(image_1024,'Icon-Small@2x.png',58)
    file_1024.close()
    print 'done!'

if __name__=='__main__':
    resizer_folder()
