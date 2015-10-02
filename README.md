# python_image_modification

Les scripts présents permettent d'appliquer une modification à une image ou un ensemble d'image.

Pour personnaliser votre modification vous pouvez changer le contenu de la fonction modifyImage(img) en début de script.

Les scripts disponibles sont les suivants:

* mirror1.py
* differences_recognition1.py




# mirror1.py

```

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




# differences_recognition1.py

```
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
