'''
Created on Dec 5, 2015
@author: urjit0209,vec241, mc3784
'''

import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from ExceptionHandler import VideoAnalysisException

class DataManager:
    """
        Performs the basic actions on the data set : data loading, cleaning, and basic exploratory model
    """
    def __init__(self):
        """
            Initialize the DataManager instance
        """
        self.raw_data = self.load_data()
        self.cleaned_data = self.clean_data(self.raw_data)

    def load_data(self):
        '''
            Loading data into pandas dataframe
        '''
        try:
            dataframe = pd.read_csv('../YouTubeData/train_sample.csv')
            df_reindex = dataframe.reindex(np.random.permutation(dataframe.index))
            return df_reindex
        except:
            raise VideoAnalysisException(" Error while loading the data ")

    def clean_data(self,data):
        '''
            remove unwanted colums, convert catagorical data into numeric data
            dimension : 2d -> 1 , 3d -> 0
            definition :: hd -> 1 , sd -> 0
            caption : True -> 1 , False -> 0
            licensedContent : True -> 1 , False -> 0
        '''
        try:
            data['dimension'] = (data['dimension'] == '2d')*1
            data['definition'] = (data['definition'] == 'hd')*1
            data['caption'] = (data['caption'])*1
            data['licensedContent'] = (data['licensedContent'])*1
            # Replace the NaN values in 'description'
            data['description'].fillna('No description', inplace=True)
            return data
        except:
            raise VideoAnalysisException(" Error while cleaning the data ")


    def binaryTree(self, data):
        '''
            Building a first exploratory model on non-text data to allow future basic data analytics such as feature importance plottting
            input : dataframe including the data
            output : binary tree trained on the data
        '''


        try:
            # Split Data Set
            target_var = "video_category_id"
            predictor_var = ["viewCount", "likeCount", "dislikeCount", "favoriteCount","commentCount", "caption"]
            X = data[predictor_var]
            Y = data[target_var]
            Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, Y, train_size = 0.80, random_state = 10)

            # Build model
            decision_tree = DecisionTreeClassifier(criterion="entropy",min_samples_split= 2 ,min_samples_leaf= 128 )
            decision_tree.fit(Xtrain, Ytrain)

            return decision_tree

        except:
            raise VideoAnalysisException(" Error while building the decision tree")
