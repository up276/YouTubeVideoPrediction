from unittest import TestCase
from YoutubeAnalysis.DataSimulator import Video
from YoutubeAnalysis.DataManager import DataManager
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB
from sklearn.tree import DecisionTreeClassifier

class Test(TestCase):
    '''
    This Test class has a test case which are built to test the prediction model of  DataSimulator() Class
    '''

    def setUp(self):
        self.video=Video('Title','Description')
        self.datamanager=DataManager()

    def test_generatePredictingModel(self):
        tree, model_count_title, model_count_description,count_vectorizer_title,count_vectorizer_description = self.video.generatePredictingModel(self.datamanager.cleaned_data)

        self.count_vectorizer_compare = CountVectorizer()
        self.model_count_compare = BernoulliNB()
        self.tree_compare = DecisionTreeClassifier()

        self.assertEqual(type(tree),type(self.tree_compare))
        self.assertEqual(type(model_count_title),type(self.model_count_compare))
        self.assertEqual(type(model_count_description),type(self.model_count_compare))
        self.assertEqual(type(count_vectorizer_title),type(self.count_vectorizer_compare))
        self.assertEqual(type(count_vectorizer_description),type(self.count_vectorizer_compare))