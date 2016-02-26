'''
Created on Dec 5, 2015
@author: urjit0209,vec241, mc3784
'''

import sys
from DataExplorer import DataExplorer
from DataSimulator import Video
from DataManager import DataManager
import time
from ExceptionHandler import VideoAnalysisException


class FlowManager():
    '''
    This program enable the user to perform many actions based on an initial data set containing meta data (title, description,
    number of likes, duration,... )on more than 240.000 YouYube videos, such as :
    - Learn about the data set (which features are available, ...) and visualize the raw data set
    - Perform various analysis / plots on the data set
        - General analysis
        - Analysis per video category
        - Analysis per feature
    - Test our model we have built on this data set to predict the category of a video based on the input of its title and description
    '''

    def __init__(self):
        """
            Initialize the program prompting the instruction to the program
        """
        self.printProgramInfos()
        self.datamanager = DataManager()
        self.dataexplorer = DataExplorer()


    def printProgramInfos(self):
        print "\n==========================================="
        print "WELCOME TO THE YOUTUBE VIDEO ANALYSIS PROGRAM"
        print "===========================================\n"

    def InitiateFlow(self):
        """
        Initialize the user interaction
        """
        self.InitialUserOptions()
        self.InitialUserInputLoop()


    def InitialUserOptions(self):
        print "\nYou are currently in the main menu. Please choose one of the options below\n \
               1) press 1 to visualize the data of the training data set \n \
               2) press 2 to explore the data \n \
               3) press 3 to predict the category of a YouTube video \n \
               4) Enter 'quit' to exit from the program "

    def InitialUserInputLoop(self):
        """
            Main menu loop
            Ask the user which action he/she wants to take and send the user to the appropriate option.
            The loop is break (and the program ends) whenever the user types quit.
        """
        userInput = ""
        try:
            while userInput != "quit":
                userInput = raw_input("\nPlease enter the Input: ")
                if userInput == "1":
                    self.DataVisulizerUserInputLoop()
                elif userInput == "2":
                    self.DataExplorerUserInputLoop()
                elif userInput == "3":
                    self.DataSimulatorUserInputLoop()
                elif userInput == "quit":
                    self.ExitProgram()
                else:
                    print "\nOops...Incorrect Input...Please enter correct Input !!!\n"


        except KeyboardInterrupt:
            print "quitting..."
            sys.exit()

    def DataVisulizerUserInputLoop(self):
        """
            Data Visualisation Option loop
            Ask the user which action he/she wants to take and initialize the Data Visualisation if required by user
            The loop is break (and the program ends) whenever the user types quit.
        """
        userInput = ""
        try:
            while userInput != "quit":
                self.printDataVisulizerOptions()
                userInput = raw_input("\nPlease provide the input : ")
                if userInput == "1":
                    self.dataexplorer.visualizeData(self.datamanager.cleaned_data)
                    self.InitiateFlow()
                elif userInput == "4":
                    print "\nYou are now in the previous control"
                    self.InitiateFlow()
                elif userInput == "quit":
                    self.ExitProgram()
                else:
                    print "\nOops...Incorrect Input...Please enter correct Input !!!\n"
                    self.DataVisulizerUserInputLoop()

        except KeyboardInterrupt:
            print "quitting..."
            sys.exit()

    def printDataVisulizerOptions(self):
        print "\nThis part of the program will explain you what are the main characteristics of our data and will show you the first 5 rows of our dataframe\n \
               1) press 1 to start the Visualization \n \
               4) press 4 to go back to main menu \n \
               2) Enter 'quit' to exit from the program "

    def DataExplorerUserInputLoop(self):
        """
            Data Exploration Option loop
            Ask the user which action he/she wants to take and initialize the appropriate analysis.
            The loop is break (and the program ends) whenever the user types quit.
        """
        userInput = ""
        try:
            while userInput != "quit":
                self.printDataExploreOptions()
                userInput = raw_input("\nPlease provide the input : ")
                if userInput == "1":
                    self.dataexplorer.generalAnalysis(self.datamanager.cleaned_data,
                                                 self.datamanager.binaryTree(self.datamanager.cleaned_data))
                elif userInput == "2":
                    self.dataexplorer.printVideoCategories()
                    userInputVideoCatagory = raw_input("\nPlease provide the number of the Video Catagory : ")
                    self.dataexplorer.individual_videocatagory_analysis(self.datamanager.cleaned_data, userInputVideoCatagory)
                elif userInput == "3":
                    self.dataexplorer.printFeatures()
                    userInputfeature = raw_input("\nPlease provide the number of the feature : ")
                    self.dataexplorer.individual_feature_analysis(self.datamanager.cleaned_data, userInputfeature)
                elif userInput == "4":
                    print "\nYou are now in the previous control"
                    self.InitiateFlow()
                elif userInput == "quit":
                    self.ExitProgram()
                else:
                    print "\nOops...Incorrect Input...Please enter correct Input !!!\n"
                    self.DataExplorerUserInputLoop()

        except KeyboardInterrupt:
            print "quitting..."
            sys.exit()

    def printDataExploreOptions(self):
        print "\nThis part of the program allows you to explore the data more deeply and perform many different analysis \n \
               1) press 1 for general analysis \n \
               2) press 2 for individual analyisis of each video catagory \n \
               3) press 3 for individual feature analysis \n \
               4) press 4 to go back to main menu \n \
               5) Enter 'quit' to exit from the program "

    def DataSimulatorUserInputLoop(self):
        """
            Data Simulation Option loop
            Ask the user which action he/she wants to take and send user to appropriate option
            The loop is break (and the program ends) whenever the user types quit.
        """
        userInput = ""
        try:
            while userInput != "quit":
                self.printDataSimulationOptions()
                userInput = raw_input("\nPlease provide the input : ")
                if userInput == "1":
                    self.confirmDataSimulatorUserInputLoop()
                elif userInput == "4":
                    print "\nYou are now in the previous control"
                    self.InitiateFlow()
                elif userInput == "quit":
                    self.ExitProgram()
                else:
                    print "\nOops...Incorrect Input...Please enter correct Input !!!\n"
                    self.DataSimulatorUserInputLoop()

        except KeyboardInterrupt:
            print "quitting..."
            sys.exit()

    def printDataSimulationOptions(self):
        print "\nThis part of the program will allow you to perform Video Category Prediction\n \
               1) press 1 to start the Video Category Prediction \n \
               2) press 4 to go back to main menu \n \
               3) Enter 'quit' to exit from the program "

    def confirmDataSimulatorUserInputLoop(self):
        """
            Data Simulation Option loop
            Ask the user which action he/she wants to take and send user to appropriate option
            The loop is break (and the program ends) whenever the user types quit.
        """
        userInput = ""
        try:
            while userInput != "quit":
                self.printConfirmDataSimulationOptions()
                userInput = raw_input("\nPlease provide the input : ")
                if userInput == "1":
                    # Building the model
                    tree, model_count_title, model_count_description, count_vectorizer_title, count_vectorizer_description = Video.generatePredictingModel(
                        self.datamanager.cleaned_data)
                    print "\nNow give it a try and check out our awesome predictions !!!"
                    time.sleep(3)
                    # Perform as many prediction as required by the user
                    self.performPrediction(tree, model_count_title, model_count_description, count_vectorizer_title,
                                           count_vectorizer_description)
                elif userInput == "4":
                    self.InitiateFlow()
                elif userInput == "quit":
                    self.ExitProgram()
                else:
                    print "\nOops...Incorrect Input...Please enter correct Input !!!\n"
                    self.confirmDataSimulatorUserInputLoop()
        except KeyboardInterrupt:
            print "quitting..."
            sys.exit()

    def printConfirmDataSimulationOptions(self):
        print "\nPlease be aware it will take time to build the model before you can perform any simulation (about 30 sec for 16 Gb of ram)\n \
               1) press 1 to confirm you want to perform the Video Category Prediction  \n \
               2) press 4 to go back to main menu \n \
               3) Enter 'quit' to exit from the program "

    def performPrediction(self, tree, model_count_title, model_count_description, count_vectorizer_title,
                          count_vectorizer_description):
        """
            Data Simulation Option loop
            Ask the user which action he/she wants to take, initialize model construction and perform prediction if required
            The loop is break (and the program ends) whenever the user types quit.
        """
        try:
            userInput = ""
            while userInput != "quit":
                self.printPredictionOptions()
                userInput = raw_input("\nPlease provide the input : ")
                if userInput == "1":
                    print "\nNow please go on YoutTube, chose the video of your choice, and enter the title and the description of that video (for more information, please read the README file)"
                    time.sleep(1.5)
                    title = raw_input("\nPlease provide the title of your video (as one single line) : ")
                    description = raw_input("\nPlease provide the description of the video (as one single line) : ")
                    video = Video(title, description)
                    predicted_category_value = video.predictVideoCategory(tree, model_count_title,
                                                                          model_count_description,
                                                                          count_vectorizer_title,
                                                                          count_vectorizer_description)
                    predicted_category_name = self.dataexplorer.Catagory_mapping[predicted_category_value]
                    print "\nMy prediction is that your video is a {} video".format(predicted_category_name)
                    time.sleep(3)
                elif userInput == "4":
                    self.InitiateFlow()
                elif userInput == "quit":
                    self.ExitProgram()
                else:
                    print "\nOops...Incorrect Input...Please enter correct Input !!!\n"
                    self.performPrediction(tree, model_count_title, model_count_description, count_vectorizer_title,
                                           count_vectorizer_description)
        except KeyboardInterrupt:
            print "quitting..."
            sys.exit()

    def printPredictionOptions(self):
        print "\nThe predicting model is ready to operate. Please choose one of the following options\n \
               1) press 1 to perform a prediction \n \
               2) press 4 to go back to main menu \n \
               3) Enter 'quit' to exit from the program "

    def ExitProgram(self):
        time.sleep(2)
        print "Exiting from the program...See you soon !!!)"
        time.sleep(2)
        sys.exit()


if __name__ == "__main__":
    try:
        flowManager = FlowManager()
        flowManager.InitiateFlow()

    except VideoAnalysisException as exception:
        print "User Defined Exception : ", exception
        time.sleep(2)
        print "Exiting from the program...See you soon !!!)"
        time.sleep(2)
        sys.exit()


