import cv2
import numpy

class ImageModder:
    """This class opens an image and uses openCV to apply various effects to
    the image."""

    def __init__(self, filepath=None):
        """init method includes an optional filepath argument to open an image file as is"""
        
        self.original_img = None
        if(not filepath is None):
            self.loadImage(filepath)
    


    def loadImage(self, imageFilePath, flag=cv2.IMREAD_UNCHANGED):
        """Loads an image using the given file path, replacing any image already
        loaded in this class.  The optional flag is used to determine how openCV loads it"""

        self.original_img = cv2.imread(imageFilePath, flag)
        # check for an error opening the file: this openCV function returns none if the file did not load

        if self.original_img is None:
            raise IOError("OpenCV failed to load an image using this file path: " + imageFilePath)
            
        


    def loadImageInGrayscale(self, imageFilePath):
        """This method calls the loadImage method with the flag set to the openCV constant for loading in grayscale"""
        self.loadImage(imageFilePath,  flag=cv2.IMREAD_GRAYSCALE)
        
        

    def saveImage(self, filepath):
        """This method saves the image loaded into this class to the specified filepath, which should have
           an extension for one of the image types openCV can handle"""
        if(self.imageLoaded()):
            cv2.imwrite(filepath,self.original_img)
        else:
            raise IOError("No image was loaded so it could not be saved")


    def removeRedFromImage(self):
        """This method removes red from the image by setting all values in
        the red channel to zero"""
        if(not self.original_img is None and self.original_img.ndim > 2 and self.original_img.shape[2] >=3):
            self.original_img[:,:,2] = 0
        else:
            print("ERROR: image does not contain a red channel")
            

    def removeGreenFromImage(self):
        """This method removes green from the image by setting all values in
        the green channel to zero"""
        if(not self.original_img is None and self.original_img.ndim > 2 and self.original_img.shape[2] >=3):
            self.original_img[:,:,1] = 0
        else:
            print("ERROR: image does not contain a green channel")

    def removeBlueFromImage(self):
        """This method removes blue from the image by setting all values in
        the blue channel to zero"""
        if(not self.original_img is None and self.original_img.ndim > 2 and self.original_img.shape[2] >=3):
            self.original_img[:,:,0] = 0
        else:
            print("ERROR: image does not contain a blue channel")


    def inverse(self):
        """reverses the colors in the picture by subtracting BGR values from the max value (255)"""
        if(not self.original_img is None and self.original_img.ndim > 2 and self.original_img.shape[2] >=3):
            
            self.original_img[:,:,0] = 255 - self.original_img[:,:,0]          
            self.original_img[:,:,1] = 255 - self.original_img[:,:,1]
            self.original_img[:,:,2] = 255 - self.original_img[:,:,2]
            
            
        else:
            print("ERROR")

    def addAlphaChannel(self):
        """Converts the BGR image to the BGRA colorspace"""
        self.original_img = cv2.cvtColor(self.original_img, cv2.COLOR_BGR2BGRA)
        
        

    def makeColorTransparent(self, bgrColor):
        """This method accepts a BGR color as a list (ex: [100, 250, 0] ) and then makes the alpha channel transparent for any
        color that matches in the image"""
        img = self.original_img
        # loop across the image, setting all pixels of this color to completely transparent
        for x in range(0, img.shape[0]):
            for y in range(0, img.shape[1]):
                if bgrColor[0] == img.item(x,y,0) and bgrColor[1] == img.item(x,y,1) and bgrColor[2] == img.item(x,y,2):
                    self.original_img.itemset(x,y,3, 0)


    def imageLoaded(self):
        return not self.original_img is None
    
    def isGrayscaleImage(self):
        if self.imageLoaded():
            return self.original_img.ndim == 2
        else:
            return False

    def isBGRImage(self):
        if self.imageLoaded():
            return self.original_img.ndim == 3 and self.original_img.shape[2] == 3
        else:
            return False

    def isBGRAImage(self):
        if self.imageLoaded():
            return self.original_img.ndim == 3 and self.original_img.shape[2] == 4
        else:
            return False


    
           

                    

        
def testBooleanMethods(imgModder):
    print("isLoaded : " +str(imgModder.imageLoaded()))
    print("isGrayscale : " +str(imgModder.isGrayscaleImage()))
    print("isBGRImage : " +str(imgModder.isBGRImage()))
    print("isBGRAImage : " +str(imgModder.isBGRAImage()))
    print("----------------------------------------------")  

if __name__ == '__main__':
    ## Test program to be removed
    imgModder = ImageModder()
    print("None loaded")
    testBooleanMethods(imgModder)
    
    imgModder.loadImageInGrayscale("example.png")
    print("Grayscale loaded")
    testBooleanMethods(imgModder)
    
    imgModder.loadImage("example.png")
    print("BGR loaded")
    imgModder.inverse()
    testBooleanMethods(imgModder)

    
    imgModder.addAlphaChannel()
    print("BGRA loaded")
    testBooleanMethods(imgModder)

    #imgModder.makeColorTransparent((0,0,0))
    imgModder.saveImage("example2.png")

    









