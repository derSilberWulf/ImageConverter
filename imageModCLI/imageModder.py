import cv2
import numpy
#import copy

class ImageModder:
    """This class opens an image and uses openCV to apply various effects to
    the image"""

    

    def __init__(self):
        
        self.original_img = None
            


    def loadImage(self, imageFilePath, flag=cv2.IMREAD_UNCHANGED):
        """Loads an image using the given file path, replacing any image already
        loaded in this class.  The flag is used to determine how openCV loads it"""
        if(not imageFilePath==None):
            self.original_img = cv2.imread(imageFilePath, flag)
        else:
            print("ERROR: no file path provided, image not loaded")


    def loadImageInGrayscale(self, imageFilePath):
        self.loadImage(imageFilePath,  flag=cv2.IMREAD_GRAYSCALE)
        
        

    def saveImage(self, filePath):
        if(not filePath==None):
            cv2.imwrite(filePath,self.original_img)
        else:
            print("ERROR: no file path provided, image not written")


    def removeRedFromImage(self):
        """This method removes red from the image by setting all values in
        the red channel to zero"""
        if(not self.original_img == None and imgModder.original_img.ndim > 2 and self.original_img.shape[2] >=3):
            self.original_img[:,:,2] = 0
        else:
            print("ERROR: image does not contain a red channel")
            

    def removeGreenFromImage(self):
        """This method removes green from the image by setting all values in
        the green channel to zero"""
        if(not self.original_img == None and imgModder.original_img.ndim > 2 and self.original_img.shape[2] >=3):
            self.original_img[:,:,1] = 0
        else:
            print("ERROR: image does not contain a green channel")

    def removeBlueFromImage(self):
        """This method removes blue from the image by setting all values in
        the blue channel to zero"""
        if(not self.original_img == None and imgModder.original_img.ndim > 2 and self.original_img.shape[2] >=3):
            self.original_img[:,:,0] = 0
        else:
            print("ERROR: image does not contain a blue channel")


    def inverse(self):
        """reverses the colors in the picture"""
        if(not self.original_img == None and imgModder.original_img.ndim > 2 and self.original_img.shape[2] >=3):
            self.original_img[:,:,0] += (255 /2)
            self.original_img[:,:,1] += (255 /2)
            self.original_img[:,:,2] += (255 /2)
            
        else:
            print("ERROR")

    def addAlphaChannel(self):
        b , g , r = cv2.split(self.original_img)
        alpha = numpy.zeros(b.shape, dtype=b.dtype)
        self.original_img = cv2.merge((b,g,r,alpha))
        self.original_img[:,:,3] = 50
        print(self.original_img[0,0,3])
        """cv2.imshow('b',b)
        cv2.imshow('g', b)
        cv2.imshow('r', r)
        cv2.imshow('a', alpha)
        cv2.imshow('image', self.original_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()"""
        


## Test program to be removed
imgModder = ImageModder()
imgModder.loadImage("example.jpg")
imgModder.addAlphaChannel()
imgModder.saveImage("Example2.jpg")


print type(imgModder.original_img)



