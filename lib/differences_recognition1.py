# -*- coding: utf-8 -*-

from PIL import Image
from PIL import ImageChops

def modifyImage(img):

    # get height and width
    width, height = img.size
    
    # get left and right part
    left = img.crop((0, 0, int(width/2), height))
    right = img.crop((int(width/2), 0, width, height))
    
    # get difference
    diff = ImageChops.difference(left, right)
    
    # create double mask
    mask = diff.convert("L").point(lambda i: 0 if  i < 40 else 255)
    double_mask = Image.new('L', img.size)
    double_mask.paste(mask, (0, 0))
    double_mask.paste(mask, (int(width / 2), 0))
    
    # create dark
    dark = img.point(lambda i: (i - 127) / 5 + 27)

    # create composite 
    composite = Image.composite(img, dark, double_mask)
    
    # create new image double size
    newImage = Image.new('RGB', (width, height * 2))
    
    # past original and composite
    newImage.paste(img, (0, 0, width, height))
    newImage.paste(composite, (0, height, width, height * 2))
    
    # Output
    return newImage

