# python_image_modification

Run main_process.py in the lib folder and you can apply some type of modification on your images.

You can modify type of modification files or create your own in the lib folder, it will be automaticly added to the available type.

Modification type available:

* differences_recognition1
* mirror1
* mirror2
* mirror3
* mirror4


### mirror3 exemple

#### before
![vidy](https://cloud.githubusercontent.com/assets/14947215/10262699/68009c18-69d3-11e5-8ae8-351b6cb348ff.jpg)

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


### mirror4 exemple

#### before
![capture d ecran 2015-04-26 a 04 46 55](https://cloud.githubusercontent.com/assets/14947215/10262692/114a8d20-69d3-11e5-88fd-d18f7468c3e3.png)

#### after
![capture d ecran 2015-04-26 a 04 46 55_modif](https://cloud.githubusercontent.com/assets/14947215/10262673/7b70fb2c-69d2-11e5-8aaf-5f63674e3edd.png)

#### mirror4 code

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
    region = region.transpose(Image.FLIP_LEFT_RIGHT)
    region = region.transpose(Image.FLIP_TOP_BOTTOM)
    newImg.paste(region, box)
    
    # image part 4
    box = (xMiddle, y, x, y * 2)
    region = imgResized2
    region = region.transpose(Image.FLIP_TOP_BOTTOM)
    newImg.paste(region, box)

    # Output
    return newImg
````

### differenceRecognition1 exemple

#### before


#### after
![difference_01_modife](https://cloud.githubusercontent.com/assets/14947215/10262729/8306b118-69d4-11e5-970a-69dea7f6919f.png)

#### differenceRecognition1 code



