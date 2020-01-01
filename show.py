#!/bin/python
from PIL import Image
import numpy as np
# Choose image to use as carrier
image_name = input("Enter file name of image to read contents: ")

# Import image
image = Image.open(image_name)
image.load()
img = np.asarray(image, dtype="int32")

# First 15 bits contains the number of characters
# Every 8 bits is a single character
bit_counter = 0

# Will use the last bit of the RED channel of every pixel to read data
number = 0
num_count = 0
message = ""
size_read = False
for i in range(len(img)):
    for j in range(len(img[0])):
        # Remove the last bit
        number+= pow(2, bit_counter)*(img[i][j][0]%2)
        bit_counter+=1
        if size_read==False and bit_counter==15:
            num_count = number
            number = 0
            size_read = True
            bit_counter = 0
        elif bit_counter==8 and size_read==True:
            message+= chr(number)
            number = 0
            bit_counter=0
        if size_read==True and num_count==len(message):
            break
    if size_read==True and num_count==len(message):
        break

print(message)