# -*- coding: utf-8 -*-

global modifName
modifName = 'mirror1'

def modifyImage(img):
    
    # get height and width
    x = img.size[0]
    y = img.size[1]

    # get middle witdh
    xMiddle = x/2
    if x % 2 == 1:
        xMiddle = (x-1) / 2
        x = x - 1
    xMiddle = int(xMiddle)

    # get middle height
    yMiddle = y/2
    if y % 2 == 1:
        yMiddle = (y-1) / 2
        y = y - 1
    yMiddle = int(yMiddle)

    # resize with middle dimension
    imgResized = img.resize((xMiddle, yMiddle), Image.BICUBIC)
    
    # image part 1
    box = (0, 0, xMiddle, yMiddle)
    region = imgResized
    region = region.convert('L')
    img.paste(region, box)
    
    # image part 2
    box = (xMiddle, 0, x, yMiddle)
    region = imgResized
    region = region.transpose(Image.FLIP_LEFT_RIGHT)
    img.paste(region, box)

    # image part 3
    box = (0, yMiddle, xMiddle, y)
    region = imgResized
    region = region.transpose(Image.FLIP_TOP_BOTTOM)
    img.paste(region, box)

    # image part 4
    box = (xMiddle, yMiddle, x, y)
    region = imgResized
    region = region.convert('1').rotate(180)
    img.paste(region, box)

    # Crop img for impair size
    img = img.crop((0, 0, x, y))
    
    # Output
    return img


execfile('process.py')

