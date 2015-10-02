# -*- coding: utf-8 -*-
from __future__ import division
from PIL import Image
import os
import glob

from PIL import ImageChops


# IMAGE MODIFICATION FONCTION
# You can modify this fonction

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

