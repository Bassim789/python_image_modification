# python_image_modification

Run main_process.py in the lib folder and you can apply some tyoe of image modification

You can modify type of modification files or create your own in the lib folder, it will be automaticly added to the available type.

Modification type available:

* differences_recognition1
* mirror1
* mirror2
* mirror3
* mirror4


### mirror3 exemple

#### before


#### after
![vidy_modif](https://cloud.githubusercontent.com/assets/14947215/10262640/680841ea-69d1-11e5-9fb0-076a62517bf6.png)

#### mirror3 code

```python
# -*- coding: utf-8 -*-

from PIL import Image

def modifyImage(img):
    
    # get height and width
    x = img.size[0]
    y = img.size[1]

    # get middle witdh and crop if odd
    xMiddle = int(x/2)
    if x % 2 == 1:
        xMiddle = int((x-1) / 2)
        x = x - 1
        img = img.crop((0, 0, x, y))

    # resize with middle dimension
    imgResized1 = img.crop((0, 0, xMiddle, y))
    imgResized2 = img.crop((xMiddle, 0, x, y))

    # create new image double height
    newImg = Image.new('RGB', (x, y * 2))
    
    # image part 1
    box = (0, 0, xMiddle, y)
    region = imgResized1
    newImg.paste(region, box)
    
    # image part 2
    box = (xMiddle, 0, x, y)
    region = imgResized1
    region = region.transpose(Image.FLIP_LEFT_RIGHT)
    newImg.paste(region, box)

    # image part 3
    box = (0, y, xMiddle, y * 2)
    region = imgResized2
    region = region.transpose(Image.FLIP_TOP_BOTTOM)
    newImg.paste(region, box)
    
    # image part 4
    box = (xMiddle, y, x, y * 2)
    region = imgResized2
    region = region.transpose(Image.FLIP_TOP_BOTTOM)
    region = region.transpose(Image.FLIP_LEFT_RIGHT)
    newImg.paste(region, box)

    # Output
    return newImg

```


