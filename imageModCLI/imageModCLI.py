#import cv2
import argparse



class CommandLineInterface:
    """This class is for interpretting the arguments passed through
the command line and selecting what the program should do"""
    
    def __init__(self):
        # set up argument parser
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("--grayscale", help="flag for converting the file specified to grayscale", action="store_true")
        
        self.parser.add_argument("filename",help="the path to a file", type=file)

    def parseCommand(self):
        args = self.parser.parse_args()
        if(args.grayscale):
            pass
    

    







cli = CommandLineInterface()
cli.parseCommand()


#parser = argparse.ArgumentParser()
#parser.add_argument("-s","--square", help="display a square of a given number", type=int)

#args = parser.parse_args()
#print args.square**2

        




