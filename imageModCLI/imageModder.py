import cv2
import copy

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
        """This method increases the intensity of specified channels by 10"""
        if(not self.original_img == None and imgModder.original_img.ndim > 2 and self.original_img.shape[2] >=3):
            self.original_img[:,:,0] += (255 /2)
            self.original_img[:,:,1] += (255 /2)
            self.original_img[:,:,2] += (255 /2)
        else:
            print("ERROR")
        
        


## Test program to be removed
imgModder = ImageModder()
imgModder.loadImage("example.jpg")
imgModder.inverse()
cv2.imshow('hello',imgModder.original_img)
cv2.waitKey(0)
cv2.destroyAllWindows()



