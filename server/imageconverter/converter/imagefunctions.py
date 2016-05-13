## These methods utilize the imageModder 
#
import sys,os
sys.path.append(os.path.abspath('../../imageModCLI'))

from imageModder import ImageModder

def removeRed(modder, arguments):
    """
    wrapper for ImageModder.removeRedFromImage
    This method uses none of the arguments
    """
    modder.removeRedFromImage()
def removeGreen(modder, arguments):
    """
    wrapper for ImageModder.removeGreenFromImage
    This method uses none of the arguments
    """
    modder.removeGreenFromImage()
def removeBlue(modder, arguments):
    """
    wrapper for ImageModder.removeBlueFromImage
    This method uses none of the arguments
    """
    modder.removeBlueFromImage()

def makeColorTransparent(modder, arguments):
    """
    wrapper for ImageModder.makeColorTransparent
    This method uses three arguments to determine
    what color to make transparent:
    t_red : a number between 0-255
    t_green : a number between 0-255
    t_blue : a number between 0-255
    """
    alpha_color = [float(arguments['t_blue']), float(arguments['t_green']), float(arguments['t_red'])]
    modder.makeColorTransparent(alpha_color)

#Map names to methods for RMI
methodDictionary = {
                        'remove_red' : removeRed,
                        'remove_blue' : removeBlue,
                        'remove_green' : removeGreen,
                        'transparent' : makeColorTransparent
                    }

def modifyImage(imgpath, methods, arguments):
    """
    Execute the method selected on the image
    (in future, will allow for multiple methods to be
    used at once and will allow parameters)
    """
    modder = ImageModder()
    modder.loadImage(imgpath)
    for methodname in methods:
        methodDictionary[methodname](modder, arguments)
    modder.saveImage(imgpath)

#modifyImage('test.png', ['remove_green', 'transparent'], {'t_blue' : 0, 't_red' : 255, 't_green' : 0})
