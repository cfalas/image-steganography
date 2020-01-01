# image-steganography
Include text inside an image without visibly altering the image

The text is added by altering the least significant bit of the RED channel of each pixel.
The first 15 bits/pixels contain the length of the message, and then each 8 bits contain a number corresponding to an ASCII character
