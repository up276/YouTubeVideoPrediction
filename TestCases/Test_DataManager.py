from unittest import TestCase
from YoutubeAnalysis.DataManager import DataManager
from sklearn.tree import DecisionTreeClassifier

class Test(TestCase):
    '''
    This Test class has three test cases which are built to test the different functions of  DataManager() Class
    '''


    def setUp(self):
        self.datamanager = DataManager()

    def test_Initialization(self):
        '''
        Loading function is already called during the object creation of DataManager() class
        '''
        data = self.datamanager.raw_data
        self.assertNotEqual(len(data.index),0)


    def test_cleaning_function(self):
        '''
        Cleaning function is already called during the instance creation of DataManager Class
        '''
        columnNames = ['dimension','definition','caption','licensedContent','description']
        for colname in columnNames:
            self.assertEqual(self.datamanager.cleaned_data[colname].isnull().sum(),0)


    def test_binaryTree_function(self):
        TreeToCompare = DecisionTreeClassifier(criterion="entropy",min_samples_split= 2 ,min_samples_leaf= 128 )
        binaryTree = self.datamanager.binaryTree(self.datamanager.cleaned_data)
        self.assertEqual(type(TreeToCompare),type(binaryTree))







'''
import mock
from mock import patch
import unittest
from unittest import TestCase
from YoutubeAnalysis.FlowManager import FlowManager
#import YoutubeAnalysis/FlowManager
import os
import glob

class Test(TestCase):






class MyTestCase(unittest.TestCase):

    @patch('flowManager.InitialUserOptions')
    def test_InitialUserInputLoop(self):
        flowManager=FlowManager()
        flowManager.InitiateFlow()
        self.assertTrue(mock.called)
        #with patch('__builtin__.raw_input', return_value='1'):


if __name__ == "__main__":
    unittest.main()

'''