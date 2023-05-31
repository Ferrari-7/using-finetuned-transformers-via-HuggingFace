
# Importing packages 
from transformers import pipeline
import os
import pandas as pd

def load_data():
    # defining path
    filename = os.path.join("data", "fake_or_real_news.csv")
    # reading "Fake or Real News" dataset as Pandas dataframe
    data = pd.read_csv(filename)

    # selecting column containing titles and defining a Pandas series.
    headlines = data["title"]

    # adjusting the csv by removing the column with text and the column with id number.
    data = data.drop(columns=['Unnamed: 0', 'text'])

    return data, headlines

def perform(data, headlines):
    # downloading emotions classification model from HuggingFace.
    # reference: Jochen Hartmann, "Emotion English DistilRoBERTa-base". https://huggingface.co/j-hartmann/emotion-english-distilroberta-base/, 2022.
    classifier = pipeline("text-classification", 
                      model="j-hartmann/emotion-english-distilroberta-base", 
                      return_all_scores=False) # when false returns only highest score. # top_k=1

    # making a new list where the results will be appended to
    results = []
    # loop through all headlines. Peform classification on headline. Append results to empty list above.
    for headline in headlines: 
        output = classifier(headline)
        results.append(output)
    
    # variable "results" is a list of list of dicts. It must be flattened into a list of dict to create pandas dataframe.
    results = [dict for sublist in results for dict in sublist]

    # converting the list of dicts to a dataframe using Pandas
    results = pd.DataFrame(results)

    # renaming labels column so that there are not two columns called "label" in final dataset. 
    results = results.rename(columns={"label": "emotion"})

    # joining the results with the original data frame 
    data = data.join(results)

    # saving updated dataframe as a .csv file
    path = os.path.join("out", "results.csv")
    data.to_csv(path)

    return data

 
def main():
    data, headlines = load_data()
    perform(data, headlines)

if __name__=="__main__":
    main()