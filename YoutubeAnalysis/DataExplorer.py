'''
Created on Dec 5, 2015
@authors: urjit0209,vec241, mc3784
'''
import matplotlib.pyplot as plt
import DataPlotter as dataplotter
import time
from ExceptionHandler import VideoAnalysisException

class DataExplorer():
    '''
        Enable the user to explore the data set by :
            - giving various information on the data
            - showing the first lines of the data set
            - displaying many various plots
    '''

    features = {"1": "viewCount", "2": "likeCount", "3": "dislikeCount", "4": "favoriteCount", "5": "commentCount",
                "6": "dimension", "7": "definition", "8": "caption"}
    Catagory_mapping = {2: 'Autos & Vehicles', 23: 'Comedy', 27: 'Education', 24: 'Entertainment',
                        1: 'Film & Animation', 20: 'Gaming', 26: 'Howto & Style', 10: 'Music', 25: 'News & Politics',
                        29: 'Nonprofits & Activism', 22: 'People & Blogs', 15: 'Pets & Animals',
                        28: 'Science & Technology', 17: 'Sports', 19: 'Travel & Events'}


    def individual_videocatagory_analysis(self, data, video_id):
        """
        Input : cleaned data set, video id
        Output : Analysis of data in form of matrices and numerical values for chosen Video Catagory
        This function takes the Video_catagory_id from the user, and analyze the data for that Video Catagory.
        """

        try:
            video_id = int(video_id)
            VideoCatagory = self.Catagory_mapping[video_id]
            dataframe = data
            count_features = ["viewCount", "likeCount", "dislikeCount", "favoriteCount", "commentCount"]
            time.sleep(2)
            print "\n==============="
            print "Analysis for video catagory = ", VideoCatagory
            print "===============\n"
            VideoCatagoryData = dataframe[dataframe["video_category_id"] == video_id]
            VideoCatagory_CountData = VideoCatagoryData[count_features]
            description = VideoCatagoryData.describe()
            correlation = VideoCatagory_CountData.corr(method='pearson', min_periods=1)
            time.sleep(2)
            print "\ndescription of each feature - \n"
            time.sleep(3)
            print description
            time.sleep(3)
            print "\ncorrelation within count features - \n"
            time.sleep(3)
            print correlation
            time.sleep(3)

            print "\nAnalysis based on count for Binary features :------> \n"
            time.sleep(3)

            print "\nDimension analysis: 2d(1) , 3d(0)\n"
            time.sleep(2)
            dimensionCount = VideoCatagoryData.groupby('dimension')['video_category_id'].count()
            print dimensionCount
            time.sleep(2)
            print "\nWe have ", dimensionCount[0], " 3D videos and ", dimensionCount[
                1], " 2D videos for catagory ", VideoCatagory
            time.sleep(4)

            print "\ndefinition analysis: hd(1) , sd(0)\n"
            time.sleep(2)
            DefinitionCount = VideoCatagoryData.groupby('definition')['video_category_id'].count()
            print DefinitionCount
            time.sleep(2)
            print "\nWe have ", DefinitionCount[0], " SD videos and ", DefinitionCount[
                1], " HD videos for catagory ", VideoCatagory
            time.sleep(4)

            print "\ncaption : TRUE(1) , FALSE(0)\n"
            time.sleep(2)
            CaptionCount = VideoCatagoryData.groupby('caption')['video_category_id'].count()
            print CaptionCount
            time.sleep(2)
            print "\nWe have ", CaptionCount[1], " videos with the caption and ", CaptionCount[
                0], " videos without the caption for catagory ", VideoCatagory
            time.sleep(4)

            print "\ncaption analysis: TRUE(1) , FALSE(0)\n"
            time.sleep(2)
            licenseCount = VideoCatagoryData.groupby('licensedContent')['video_category_id'].count()
            print licenseCount
            time.sleep(2)
            print "\nWe have ", licenseCount[1], " videos with the License and ", CaptionCount[
                0], " videos without the License for catagory ", VideoCatagory
            time.sleep(4)
            return True

        except:
            raise VideoAnalysisException(" Error while analyzing data for individual video catagory ")

    def printVideoCategories(self):
        """
            Print the list of features in the dataset
        """
        try:
            for key in self.Catagory_mapping:
                print key, "-->", self.Catagory_mapping[key]
        except:
            raise VideoAnalysisException(" Error while printing video catagories ")

    def printFeatures(self):
        """
            Print the list of the existing YouTube categories, in order to allow the user to chose the one on which
            he wants to perform analysis
        """
        try:
            for key in self.features:
                print key, "-->", self.features[key]
        except:
            raise VideoAnalysisException(" Error while printing different features of the data ")

    def individual_feature_analysis(self, data, chosenFeature):
        """
            Compute a group by on the chosenFeature and call featuresBarPlot to plot the result
        """
        try:
            print "chosen feature: ", self.features[chosenFeature]
            featuresMeans = data.groupby(['video_category_id'])[self.features[chosenFeature]].mean()
            featuresNames = [self.Catagory_mapping[x] for x in featuresMeans.index]
            name = "../YoutubeData/FeatureBarChart.pdf"
            plt.savefig(name)
            print "\nPlease close the Bar Chart when you want to move ahead..."
            dataplotter.featuresBarPlot(featuresNames, featuresMeans.values)
            print "You can always retrieve the Feature Importance bar chart in YoutubeData folder.\n"
            time.sleep(3)
            return True
        except:
            raise VideoAnalysisException(" Error while performing individual feature analysis ")

    def generalAnalysis(self, data, clf):
        """
            Perform general analysis
        """
        try:
            dataplotter.plotFeatureImportance(data, clf)
            dataplotter.plotNumericalCorrelationMatrix(data)
            dataplotter.plotGraphicalCorrelationMatrix(data)
            return True
        except:
            raise VideoAnalysisException(" Error while performing general analysis ")


    def visualizeData(self, data):
        """
		    Display general information on the data and show the 5 first rows
		"""
        try:
            print "\n The data we are using are metadata on YouTube videos..."
            time.sleep(3)
            print "\n The metadata we have on the videos are the following: "
            time.sleep(3)
            for col in data.columns:
                print "\n > " + col
                time.sleep(1.5)
            print "\n We use these data to build a model able to perform prediction on the category to which each video belong..."
            time.sleep(3)
            print "\n The possible categories to which a video can belong are the following (only one category per video): "
            time.sleep(3)
            print "\n > Autos & Vehicles, Comedy, Education, Entertainment, Film & Animation, Gaming, Howto & Style, Music, " \
                  "News & Politics, Nonprofits & Activism, People & Blogs, Pets & Animals, Science & Technology, Sports, Travel & Events "
            time.sleep(6)
            print "\n In order to do that, we have a data set of about 240.000 YouTube videos..."
            time.sleep(3)
            print "\n Now here is what the first five rows of our data set look like --> ..."
            time.sleep(3)
            print "\n (You can always go check the full file : YouTubeData/train_sample.csv ...)"
            time.sleep(3)
            print data.head()
            time.sleep(6)
            return True
        except:
            raise VideoAnalysisException(" Error while Performing Data Visualization ")


