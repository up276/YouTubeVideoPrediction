from unittest import TestCase
from YoutubeAnalysis.DataExplorer import DataExplorer
from YoutubeAnalysis.DataManager import DataManager

class TestDataExplorer(TestCase):
    '''
    This Test class has three test cases which are built to test the different functions of  DataExplorer() Class
    '''

    def setUp(self):
        self.dataexplorer = DataExplorer()
        self.datamanager = DataManager()

    def test_individual_videocatagory_analysis(self):
        VideoID = 1
        Val = self.dataexplorer.individual_videocatagory_analysis(self.datamanager.cleaned_data, VideoID)
        self.assertTrue(Val)

    def test_individual_feature_analysis(self):
        FeatureNumber = '1'
        Val = self.dataexplorer.individual_feature_analysis(self.datamanager.cleaned_data, FeatureNumber)
        self.assertTrue(Val)

    def test_individual_visulizer_function(self):
        Val = self.dataexplorer.visualizeData(self.datamanager.cleaned_data)
        self.assertTrue(Val)
