#!/bin/python
from PIL import Image
import numpy as np
# Choose image to use as carrier
image_name = input("Enter file name of image to use as carrier: ")

# Choose message
message = input("Message to be hidden: ")

# Import image
image = Image.open(image_name)
image.load()
img = np.asarray(image, dtype="int32")
# Hash message character (one character at a time, so that hash doesn't become too large)
message_array = []
message_array.append(len(message))
for character in message:
    message_array.append(ord(character))

message_index = 0
int_count = 0
def next_bit(message_index):
    global int_count
    if message_index==0:
        if int_count>=15:
            int_count = 0
            return next_bit(message_index+1)
    if message_index>=len(message_array):
        return (0, message_index)
    if int_count>=8 and message_index!=0:
        int_count = 0
        return next_bit(message_index+1)
    int_count+=1
    bit = message_array[message_index] % 2
    message_array[message_index] = int(message_array[message_index]/2)
    return (bit, message_index)
    
# Will use the last bit of the RED channel of every pixel to store data
for i in range(len(img)):
    for j in range(len(img[0])):
        # Remove the last bit
        img[i][j][0] = int(img[i][j][0]/2)
        img[i][j][0] *=2
        (bit, message_index) = next_bit(message_index)
        img[i][j][0] += bit
        if message_index>=len(message_array):
            break
    if message_index>=len(message_array):
        break
if message_index<len(message_array):
    print("Warning: Image not large enough to store whole message, only beginning was saved")

print('New image saved! (same file name, overwritten)')
image = Image.fromarray(img.astype(np.uint8)).save(image_name)
