from unittest import TestCase
import YoutubeAnalysis.DataPlotter as dataplotter
from YoutubeAnalysis.DataManager import DataManager


class Test(TestCase):
    '''
    This Test class has three test cases which are built to test the different functions of  DataPlotter() Class
    '''

    def setUp(self):
        self.datamanager=DataManager()

    def test_plotFeatureImportance(self):
        clf = self.datamanager.binaryTree(self.datamanager.cleaned_data)
        val = dataplotter.plotFeatureImportance(self.datamanager.cleaned_data,clf)
        self.assertTrue(val)

    def test_plotNumericalCorrelationMatrix(self):
        val = dataplotter.plotNumericalCorrelationMatrix(self.datamanager.cleaned_data)
        self.assertTrue(val)

    def test_plotGraphicalCorrelationMatrix(self):
        val = dataplotter.plotGraphicalCorrelationMatrix(self.datamanager.cleaned_data)
        self.assertTrue(val)