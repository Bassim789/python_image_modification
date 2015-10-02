# -*- coding: utf-8 -*-
from __future__ import division
from PIL import Image
import os
import glob



# IMAGE MODIFICATION FONCTION
# You can modify this fonction

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




# PROCESSING IMAGE MODIFICATION

def proccessImageModify(completeFileName, path_image_modif):

    # Set filename and get image
    filename = completeFileName.rsplit('/', 1)[1]
    img = Image.open(completeFileName)

    # modification
    img = modifyImage(img)

    # Output image modife
    newFilename = filename.split('.')[0] + '_modife.png'
    img.save(path_image_modif + newFilename)
    return '\n' + newFilename + ' a été créer dans le dossier image_modife'


def proccessImageModifyAll(path_image_original, path_image_modif):

    print "\nTraitement du dossier...\n"
    compteurSucces = 0
    compteurTotal = 0

    # for each image in forder
    for filename in GetFileName(path_image_original):
        if filename != '.DS_Store':
            compteurTotal += 1
            try:
                img = Image.open(path_image_original + filename)
                
                # modification
                img = modifyImage(img)

                # Save
                newFilename = filename.split('.')[0] + '_modife.png'
                img.save(path_image_modif + newFilename)
                compteurSucces += 1
                print 'Succes pour image: ' + filename
            except:
                print 'impossible pour image: ' + filename
            
    return '\n' + str(compteurSucces) + ' images sur ' + str(compteurTotal) + ' ont été crées dans le dossier image_modife'


    

def showFilename(path_image_original):
    print "\nVoici les images originales dispo:\n"
    for filename in GetFileName(path_image_original):
        if filename != '.DS_Store':
            print filename
    print


def GetFileName(path_image_original):
    return os.listdir(path_image_original)



# PROGRAMME START

# Set path
path = os.getcwd()
path_image_original = path + '/image_original/'
path_image_modif = path + '/image_modife/'

# Check and create folder if necessary
if not os.path.isdir(path_image_original):
    os.makedirs(path_image_original)
if not os.path.isdir(path_image_modif):
    os.makedirs(path_image_modif)

# Show filenames in folder image_original
showFilename(path_image_original)   

# process input from user
imageFile = 'start'
while imageFile != '' and imageFile != ' ' and imageFile != 'q':
    print '\nCommande:'
    print 'v pour voir les images dispo'
    print 't pour modifier tout le dossier'
    print 'q pour quitter'
    imageFile = raw_input("\nQuelle image veux-tu modifier: ")
    filenames = GetFileName(path_image_original)
    if imageFile != '' and imageFile != ' ' and imageFile != 'q' and imageFile != 'v' and imageFile != 't':
        if imageFile in filenames:
            try:
                completeFileName = path_image_original + imageFile
                print proccessImageModify(completeFileName, path_image_modif)
            except Exception as ex:
                print "\nErreur: " + str(ex)
        else:
            print "\nJe n'ai pas compris quel image tu veux. Recopie exactement le nom dans la liste dispo."
    elif imageFile == 'v':
        showFilename(path_image_original)
    elif imageFile == 't':
        print proccessImageModifyAll(path_image_original, path_image_modif)
    else:
        print 'a+'
