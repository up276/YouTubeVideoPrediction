'''
Created on Dec 5, 2015
@author: urjit0209,vec241, mc3784

Gather all the plot functions necessary for the program
'''

import seaborn as sns
import time
import numpy as np
import matplotlib.pyplot as plt
from ExceptionHandler import VideoAnalysisException


def featuresBarPlot(barNames,barValues):
    """
        Display a bar plot with the barValues as the length of the bars and barNames as the name of the bars.
        Input: name of the bars, value of the bars
        Output: bar plot
    """

    plt.bar(range(0,len(barNames)),barValues)
    plt.xticks(range(0,len(barNames)), barNames,rotation='vertical')
    plt.show()


def plotFeatureImportance(data,clf):
    '''
        Plot barchart showing numerical feature importance for predicting video categories
        Input : classifier
        Output : bar chart showing the importance of features according to the classifier
    '''
    try:
        print "Generating the Feature Importance bar chart...\n"
        time.sleep(3)

        # Plot
        predictor_var = ["viewCount", "likeCount", "dislikeCount", "favoriteCount","commentCount", "caption"]
        fig, ax = plt.subplots(figsize=(15, 15))
        width=0.7
        ax.bar(np.arange(len(clf.feature_importances_)), clf.feature_importances_, width, color='b')
        ax.set_xticks(np.arange(len(clf.feature_importances_)))
        ax.set_xticklabels(predictor_var,rotation=45)
        plt.title('Numerical Features Importance', fontsize=20)
        ax.set_ylabel('Normalized Entropy Importance')
        name = "../YoutubeData/feature_importance.pdf"
        plt.savefig(name)
        print "\nPlease close the Bar Chart when you want to move ahead..."
        plt.show()

        print "You can always retrieve the Feature Importance bar chart in YoutubeData folder.\n"
        time.sleep(3)
        return True
    except:
        raise VideoAnalysisException(" Error while ploating Feature Importance Graph ")



def plotNumericalCorrelationMatrix(data):
    '''
        Input : data
        Output : numerical correlation matrix
    '''
    try:
        print "Displaying numerical correlation matrix...\n"
        time.sleep(3)
        corr = data.corr()
        print corr
        time.sleep(3)
        return True
    except:
        raise VideoAnalysisException(" Error while Displaying numerical correlation matrix ")


def plotGraphicalCorrelationMatrix(data):
    '''
        Input : data
        Output : graphical correlation matrix
        Inspired from : https://stanford.edu/~mwaskom/software/seaborn/examples/many_pairwise_correlations.html
    '''
    try:
        print "\nGenerating the graphical correlation matrix...\n"
        time.sleep(3)

        corr = data.corr()
        f, ax = plt.subplots(figsize=(20, 20))
        # Generate a custom diverging colormap
        cmap = sns.diverging_palette(220, 10, as_cmap=True)
        # Draw the heatmap with the mask and correct aspect ratio
        sns.heatmap(corr, cmap=cmap,
                    square=True, xticklabels=False, yticklabels=False,
                    linewidths=.5, cbar_kws={"shrink": .5}, ax=ax)
        plt.title('Correlation Matrix', fontsize=30)
        ax.set_ylabel('Features', fontsize=20)
        ax.set_xlabel('Features', fontsize=20)
        xticklabels = ['video_category_id','viewCount','likeCount','dislikeCount','favoriteCount','commentCount','dimension','definition','caption','licensedContent']
        ylabel = xticklabels[::-1]
        ax.set_xticklabels(xticklabels, rotation=45)
        ax.set_yticklabels(ylabel, rotation=0)
        name = "../YoutubeData/correlation_matrix.pdf"
        plt.savefig(name)
        print "\nPlease close the Bar Chart when you want to move ahead..."
        plt.show()

        print "You can always retrieve the graphical correlation matrix in YoutubeData folder.\n"
        time.sleep(3)
        return True
    except:
        raise VideoAnalysisException(" Error while Generating the graphical correlation matrix")




