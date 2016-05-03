import cv2
import copy

class ImageModder:
    """This class opens an image and uses openCV to apply various effects to
    the image"""

    def __init__(self, imageFilePath):
        
        self.original_img = cv2.imread(imageFilePath, cv2.IMREAD_UNCHANGED)
        self.modified_img = copy.deepcopy(self.original_img)

        ## Test Code : to be removed
        cv2.imshow('hello',self.modified_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        ###########################

imgModder = ImageModder("example.jpg")

