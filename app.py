"""
[Day 7] Assignment: Steganography
    - Turn in on Gradescope (https://make.sc/bew2.3-gradescope)
    - Lesson Plan: https://tech-at-du.github.io/ACS-3230-Web-Security/#/Lessons/Steganography

Deliverables:
    1. All TODOs in this file.
    2. Decoded sample image with secret text revealed
    3. Your own image encoded with hidden secret text!
"""
from PIL import Image


def decode_image(path_to_png):
    """This functions decodes an image if it has encrypted text"""
    # Open the image using PIL:
    encoded_image = Image.open(path_to_png)

    # Separate the red channel from the rest of the image:
    red_channel = encoded_image.split()[0]

    # Create a new PIL image with the same size as the encoded image:
    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()

    pixels2 = red_channel.load()
    x_red, y_red = red_channel.size
    
    """Iterates through each red channel pixel, converting it to binary"""
    for x in range(x_red-1):
        for y in range(y_red-1):
            redVal = pixels2[x,y]
            binaryNum = format(redVal, 'b')

            """Gets LSB of binary Number, and checks if it is 0 or 1 to decode the message"""

            if binaryNum[-1] == '0':
                pixels[x,y] = (0,0,0)
            if binaryNum[-1] == '1':
                pixels[x,y] = (255, 255, 255)

    # DO NOT MODIFY. Save the decoded image to disk:
    decoded_image.save("decoded_image.png")

def write_text(text_to_write, image, encoded_image, pixel, new_pixels):
    """
    This function writes hidden text inside of the photo
    """

    x_size, y_size = image.size
    secret_data = text_to_write
    data_index = 0
    '''Converts the data to binary'''
    binary_secret_data = ' '.join(format(ord(x), 'b') for x in secret_data)
    
    data_len = len(binary_secret_data)
    for x in range(x_size-1):
        for y in range(y_size-1):
            new_pixels[x,y] = pixel[x,y]

    for x in range(x_size-1):
        for y in range(y_size-1):
            new_tuple = [pixel[x,y][0],pixel[x,y][1],pixel[x,y][2]]
            '''Converts binary to RGB form'''
            red = [ format(i, "08b") for i in pixel[x,y] ]
            '''The least significant bit changes for each color channel if there is still data to store'''
            if data_index < data_len:
                new_tuple[0] = int(red[:-1] + binary_secret_data[data_index], 2)
                data_index += 1
                new_pixels[x,y] = (new_tuple[0], new_tuple[1], new_tuple[2])
      
            if data_index >= data_len:
                break
    encoded_image.save("encoded_image.png")

def encode_image(path_to_png, text_to_write):
    """
    This function encodes an image with encrypted text
    """

     # read the image
    image = Image.open(path_to_png)
    encoded_image = Image.new("RGB", image.size)
    pixel = image.load()
    new_pixels = encoded_image.load()
    write_text(text_to_write, image, encoded_image, pixel, new_pixels)


encode_image("ladybug.jpg", "test")
decode_image("encoded_sample.png")


#decode_image("encoded_sample.png")