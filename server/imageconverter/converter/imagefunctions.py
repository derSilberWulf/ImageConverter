## These methods utilize the imageModder 
#
import sys,os
sys.path.append(os.path.abspath('../../../imageModCLI'))

from imageModder import ImageModder

#Map names to methods for RMI (should be moved to a settings file eventually)
methodDictionary = {
                        'remove_red' : ImageModder.removeRedFromImage,
                        'remove_blue' : ImageModder.removeBlueFromImage,
                        'remove_green' : ImageModder.removeGreenFromImage
                    }

def modifyImage(imgpath, methodname):
    """
    Execute the method selected on the image
    (in future, will allow for multiple methods to be
    used at once and will allow parameters)
    """
    modder = ImageModder()
    modder.loadImage(imgpath)
    methodDictionary[methodname](modder)
    modder.saveImage(imgpath)

modifyImage('test.png', 'remove_green')