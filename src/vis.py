# Import packages
# for loadin data
import os
import pandas as pd
# for visualization
import seaborn as sns
import matplotlib.pyplot as plt


def load_data():
    filename = os.path.join("out", "results.csv")

    # reading "Fake or Real News" dataset as Pandas dataframe
    data = pd.read_csv(filename)

    return data


def visualize(data):
    # defining a colour palette for visualizations
    emotion_palette = {"anger" : "red", 
               "disgust" : "green", 
               "fear" : "purple", 
               "joy" : "orange", 
               "neutral" : "grey", 
               "sadness" : "blue", 
               "surprise" : "yellow"}
    
    # Making a histogram over all data. X-axis shows emotion label. Y-axis show frequency. 
    sns.histplot(data = data, 
                 x = "emotion", 
                 hue = "emotion",
                 palette = emotion_palette,
                shrink = .8) # shrinking the bars to emphasize categories
    # saving histogram
    hist_path = os.path.join("visualizations", "news_histogram_all.png")
    plt.savefig(hist_path)

    # Making a distribution plot to compare results
    # clear plot to make new plot
    plt.clf()
    label_palette = {"FAKE" : "red", "REAL" : "blue"} 
    sns.displot(data = data,
                x = "emotion",  
                hue = "label",
                multiple = "dodge",
                shrink = .5,
                palette = label_palette)
    # saving comparison plot
    comp_path = os.path.join("visualizations", "news_comparison.png")
    plt.savefig(comp_path)

    # Making a violinplot to compare the emotion label scores. 
    # clear plot to make new plot
    plt.clf()
    sns.violinplot(data=data,
                    x = "emotion",
                    y = "score", 
                    hue = "label",
                    palette = label_palette, 
                    split = True, # Draw split violins to take up less space
                    cut = 0, # Prevents the density from smoothing beyond the limits of the data
                    bw = .09 ) # adjusting bandwidth to reduce the amount of smoothing
    # saving score comparison plot
    score_path = os.path.join("visualizations", "news_score_comparison.png")
    plt.savefig(score_path)


def main():
    data = load_data()
    visualize(data)

if __name__=="__main__":
    main()
