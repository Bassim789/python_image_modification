# python_image_modification

Run exec.py and you can apply diverse type of modification for your images.

You can modify type of modification files or create your own in the lib folder, it will be automaticly added to the available type.

Modification type available:

* mirror1
* mirror2
* mirror3
* mirror4
* differences_recognition1

### mirror1 exemple

#### before
![empire](https://cloud.githubusercontent.com/assets/14947215/10262753/c812658a-69d5-11e5-97d9-07d5d1fe4284.jpg)

#### after
![empire_modif_mirror1](https://cloud.githubusercontent.com/assets/14947215/10262781/cab35870-69d6-11e5-9bb8-5e5d6bf1b3e3.png)

#### mirror1 code

```python
# -*- coding: utf-8 -*-

from PIL import Image

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

```

### mirror1 exemple

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

### differences_recognition1 exemple

#### before
![difference_01](https://cloud.githubusercontent.com/assets/14947215/10262737/0734b85e-69d5-11e5-82da-13ba1971b286.jpg)

#### after
![difference_01_modife](https://cloud.githubusercontent.com/assets/14947215/10262729/8306b118-69d4-11e5-970a-69dea7f6919f.png)

#### differences_recognition1 code
```python
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

```


