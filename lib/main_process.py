# -*- coding: utf-8 -*-
from PIL import Image
import os
import glob
import sys
import importlib
import imp


def proccessImageModify(completeFileName, path_image_modif):

    global module
    global actualModifType
    
    print "\nWork in progress...\n"

    try:
        # Set filename and get image
        filename = completeFileName.rsplit('/', 1)[1]
        img = Image.open(completeFileName)

        # modification
        img = module.modifyImage(img)

        # Output image modife
        newFilename = filename.rsplit('.', 1)[0] + '_modif_' + actualModifType + '.png'
        img.save(path_image_modif + newFilename)
        reponse = '\n' + newFilename + ' has been create in folder image_modif'
        
    except Exception as ex:
                reponse = "\nError: " + str(ex)
                
    return reponse


def proccessImageModifyAll(path_image_original, path_image_modif):

    global module
    global actualModifType

    print "\nWork in progress...\n"
    compteurSucces = 0
    compteurTotal = 0

    # for each image in forder
    for filename in getFileName(path_image_original):
        if filename != '.DS_Store':
            compteurTotal += 1
            try:
                img = Image.open(path_image_original + filename)
                
                # modification
                img = module.modifyImage(img)

                # Save
                newFilename = filename.rsplit('.', 1)[0] + '_modif_' + actualModifType + '.png'
                img.save(path_image_modif + newFilename)
                compteurSucces += 1
                print 'Succes: \t' + filename
            except:
                print 'Fail: \t' + filename
            
    return '\n' + str(compteurSucces) + ' / ' + str(compteurTotal) + ' images have been created in folder image_modif'


def proccessImageModifyNum(userInput, path_image_modif, path_image_original):

    compteur = 0
    for filename in getFileName(path_image_original):
        if filename != '.DS_Store':
            compteur += 1
            if compteur == int(userInput):
                break
    
    completeFileName = path_image_original + filename
    return proccessImageModify(completeFileName, path_image_modif)
    

def showFilename(path_image_original):
    filenameListeStr = ''
    filenameListeStr += "\n\nimage_orignal folder:\n\n"
    filenameListeStr += "NUM \t NAME \n\n"
    compteur = 0
    for filename in getFileName(path_image_original):
        if filename != '.DS_Store':
            compteur += 1
            filenameListeStr += str(compteur) + ' \t ' + str(filename) + '\n'
    if compteur == 0:
        filenameListeStr = '\nNo image available, please add some to folder image_original\n'
    return filenameListeStr


def showFilenameModif(path_image_modifl):
    filenameListeStr = ''
    filenameListeStr += "\n\nimage_modify folder:\n\n"
    filenameListeStr += "NUM \t NAME \n\n"
    compteur = 0
    for filename in getFileName(path_image_modif):
        if filename != '.DS_Store':
            compteur += 1
            filenameListeStr += str(compteur) + ' \t ' + str(filename) + '\n'
    if compteur == 0:
        filenameListeStr = '\nNo image available in image_modify folder \n'
    return filenameListeStr


def getFileName(path_image_original):
    return os.listdir(path_image_original)


def getNumListe(path_image_original):
    numListe = []
    compteur = 0
    for filename in getFileName(path_image_original):
        if filename != '.DS_Store':
            compteur += 1
            numListe.append(str(compteur))
    return numListe


def commande ():
    commande = '\nCommande:\n\n'
    commande += 'o : \t Show image_original folder\n'
    commande += 'm : \t Show image_modify folder\n'
    commande += 'a : \t Modify all files in image_original folder\n'
    commande += 't : \t Show all modif type \n'
    commande += 'type : \t type + NUM or NAME  to change type  \n'
    commande += 'c : \t commande  \n'
    commande += 'mt : \t Show actual modif type  \n'
    commande += 'q : \t Quite programme\n'
    return commande


def showType(path):
    reponse =  '\nModification type:\n\n'
    reponse += "NUM \t NAME \n\n"
    modifTypeNumListe = []
    compteur = 0
    for modifType in os.listdir(path + '/lib'):
        if modifType[-3:] == '.py' and modifType !=  '__init__.py' and modifType !=  'main_process.py' :
            compteur += 1
            modifTypeNumListe.append(str(compteur))
            reponse += str(compteur) + '\t' + modifType.rsplit('.', 1)[0] + ' \n'
    return reponse


def changeType(userInput, path):
    global actualModifType
    global module
    path = path + '/lib'
    typeFromUser = userInput.split(' ', 1)[1].strip()
    reponse = ''
    compteur = 0
    find = False
    for modifType in os.listdir(path):
        
        if modifType[-3:] == '.py' and modifType !=  '__init__.py' and modifType !=  'main_process.py' :
            compteur += 1
            modifTypeClean = modifType.rsplit('.', 1)[0]
            
            if str(compteur) == typeFromUser or modifTypeClean == typeFromUser:
                actualModifType = modifTypeClean
                #module = __import__(actualModifType)
                module = imp.load_source(actualModifType, path + '/' + modifType)
                find = True
                break
            
    if find:
        reponse += '\nModif type: ' + modifTypeClean + ' \n'
        
    else:
        reponse += '\nI cant find this type of modification. \n'
        
    return reponse


def setDefaultModifType(path):
    global module
    global actualModifType
    path = path + '/lib'
    for modifType in os.listdir(path):
        if modifType[-3:] == '.py' and modifType !=  '__init__.py' and modifType !=  'main_process.py' :
            actualModifType = modifType.rsplit('.', 1)[0]
            moduleName = actualModifType
            #module = __import__(moduleName)
            module = imp.load_source(moduleName, path + '/' + modifType)
            break


def getActualModifType():
    global actualModifType
    return '\n' + 'modif type: ' + '\t' + actualModifType


# PROGRAMME START

# Set path
path = os.path.dirname(os.path.abspath('__file__'))
path = path.rsplit('/lib', 1)[0]
os.chdir(path + '/lib/')
path_image_original = path + '/image_original/'
path_image_modif = path + '/image_modif/'


# Set modifType
global actualModifType
setDefaultModifType(path)

# Set global
global module


# Check and create folder if necessary
if not os.path.isdir(path_image_original):
    os.makedirs(path_image_original)
    print '\nFolder image_original has been created. \n'
if not os.path.isdir(path_image_modif):
    os.makedirs(path_image_modif)
    print '\nFolder image_modif has been created. \n'


# Show filenames in folder image_original
print showFilename(path_image_original)   


# First instructions
userInput = 'Start'
print getActualModifType()
print commande()


# process input from user
while userInput != 'q':
    
    userInput = raw_input("\nWhich image would like to modify (NUM or NAME): ").strip()

    filenames = getFileName(path_image_original)
    numListe = getNumListe(path_image_original)
    
    if userInput.lower() == 'o':
        reponse = showFilename(path_image_original)

    elif userInput.lower() == 'm':
        reponse = showFilenameModif(path_image_modif)

    elif userInput.lower() == 'c':
        reponse = commande()

    elif userInput.lower() == 'mt':
        reponse = getActualModifType()
        
    elif userInput.lower() == 'a':
        reponse = proccessImageModifyAll(path_image_original, path_image_modif)
        
    elif userInput.lower() == 'q':
        reponse = '\nBye!\n'

    elif userInput.lower() == 't':
        reponse = showType(path)

    elif userInput.lower()[:5] == 'type ':
        reponse = changeType(userInput, path)

    elif userInput in numListe:
        reponse = proccessImageModifyNum(userInput, path_image_modif, path_image_original)

    else:
        if userInput in filenames:
            completeFileName = path_image_original + userInput
            reponse = proccessImageModify(completeFileName, path_image_modif)
        else:
            reponse = "\nI dont understand what you want."
            
    print reponse

