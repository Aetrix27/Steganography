"""
[Day 7] Assignment: Steganography
    - Turn in on Gradescope (https://make.sc/bew2.3-gradescope)
    - Lesson Plan: https://tech-at-du.github.io/ACS-3230-Web-Security/#/Lessons/Steganography

Deliverables:
    1. All TODOs in this file.
    2. Decoded sample image with secret text revealed
    3. Your own image encoded with hidden secret text!
"""
# TODO: Run `pip3 install Pillow` before running the code.
from PIL import Image


def decode_image(path_to_png):
    """
    TODO: Add docstring and complete implementation.
    """
    # Open the image using PIL:
    encoded_image = Image.open(path_to_png)

    # Separate the red channel from the rest of the image:
    red_channel = encoded_image.split()[0]

    # Create a new PIL image with the same size as the encoded image:
    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()
    x_size, y_size = encoded_image.size

    # TODO: Using the variables declared above, replace `print(red_channel)` with a complete implementation:
    print(red_channel)  # Start coding here!
    pixels2 = red_channel.load()
    x_red, y_red = red_channel.size
    
    for x in range(x_red-1):
        for y in range(y_red-1):
            redVal = pixels2[x,y]
            binaryNum = format(redVal, 'b')
            if binaryNum[-1] == '0':
                pixels[x,y] = (0,0,0)
            if binaryNum[-1] == '1':
                pixels[x,y] = (255, 255, 255)
    #numList.append(rem)
    #print(pixels.__getitem__((x,y)))
    #if red_channel[0
    #pow*=2

    # DO NOT MODIFY. Save the decoded image to disk:
    decoded_image.save("decoded_image.png")


def encode_image(path_to_png):
    """
    TODO: Add docstring and complete implementation.
    """
    #loop through values, if <128 or >128
    pass


def write_text(text_to_write):
    """
    TODO: Add docstring and complete implementation.
    """
    pass

decode_image("encoded_sample.png")