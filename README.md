# Assignment 4 - Using finetuned transformers via HuggingFace

*Is there a difference between what emotions are displayed in the headlines of fake news and real news?*

This repository contains a python code which uses the ```HuggingFace``` library to peform emotion classification on the *Fake or Real News* dataset. The dataset contains 6335 examples. More specifically, the code will use the ```j-hartmann/emotion-english-distilroberta-base``` model[^1]. Link to model can be found [here](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base). The model can extract seven different emotions: 
1. anger
2. disgust
3. fear
4. joy
5. neutral
6. sadness
7. surprise

The code and documentation in this repository address the following tasks:

- Initalize a ```HuggingFace``` pipeline for emotion classification
- Perform emotion classification for every *headline* in the data
- Assuming the most likely prediction is the correct label, create **tables** and **visualizations** which show the following:
  - Distribution of emotions across all of the data
  - Distribution of emotions between real news and fake news
- Comparing the results

The repository is structured in the following manner:

| contents | description | 
| --- | --- | 
| data | contains a csv file with the *Fake or Real News* dataset |
| out | contains a modified version of the *Fake or Real News* dataset with the results of the emotion classification appended |
| src | contains two .py scripts. One which creates the modified dataset and one which produces visualizations. |
| visualizations | contains visualizations produced by the vis.py script in src folder |
| requirements | txt file listing the necessary packages to run the scripts |
| run.sh | shell file the user may use to run the scripts in the src folder |
| setup.sh | shell script which sets up a virtual enviroment and installs the packages listed in the requirements file |

## User instructions

In order to produce the results presented in this repository, the user may do the following steps: 

1. install the necessary packages by running the setup script from command line like so: 

```bash setup.sh```

2. run the two scripts in the src folder by using the run.sh script like so: 

```bash run.sh```

## Results

The figure below shows the distribution of emotion across the dataset in its entirety.  

![histogram showing distribution of emotions across fake and real news combined.](/visualizations/news_histogram_all.png)

In short, the emotion classification reveals that the most prominent emotion in the news headlines (besides neutral) is fear. This is then followed by anger and sadness. Conversely, the least prominent emotion displayed is joy. These results seem to be congruent with the general assumption that news tend to be mostly negative. It should be noted, however, that the vast majority of the headlines appear to have a neutral tone. 

Are these emotions distributed differently when we separate the headlines into real news and fake news? 
(Since the distribution of fake and real news in the dataset is almost equal, with 3171 real news headlines and 3164 fake news headlines, I determined that it was reasonable to compare the amount of occurrences.)

![comparison](/visualizations/news_comparison.png)

The figure shows that the distribution appear to be more similar than one might expect. This may suggest that emotionally charged language is not the most revealing factor when it comes to determining the credibility of news articles. That being said, the real news headline does tend to have an overall more neutral tone which I had personally anticipated. In most other categories, except for fear and sadness (just narrowly), fake news seem to utilize more emotionally charged language.

But what if we were to assume that the score attached to the label might give an indication as to how intense the emotion displayed is? Perhaps this could provide some insight as to how emotionally charged language might vary in intensity between fake news and real news.

![score comparison](/visualizations/news_score_comparison.png)

There does not seem to be a discernible differnce between the label scores between fake news headlines and real news headlines. However, this kind of comparison does not take into consideration that a lower score could also mean that the headline expresses two or more emotions simultaneously and that it does not necessarily reveal anything about the intensity of the emotion displayed.

In conlusion, it appears as if real news and fake news headlines might be relatively similar in regards to how they display emotions. Namely, that they prodominantly have a neutral emotional tone. This is then in both instances followed by a similar distribution of fear, anger and sadness. Therefore, one can infer that there may be other factors that might be more revealing when it comes to determining the validity of a news article based on the headline.

Lastly, it should be noted that the accuracy of the language model should not be exaggerated. For instance, the first headline in the dataset is a fake news article with the headline "You Can Smell Hillary’s Fear" which has been labeled as "fear". The model seems to have picked up on the word "fear", but to a human reader it seems more likely that the headline is conveing schadenfreude. Therefore, one has to be aware of the fact the the model may not yet be able to decipher this kind of emotional nuance. Moreover, it does not have the same contextual knowledge to base its judgements on as a human might. 
Keeping that in mind, the model does make it possible to peform feature extraction and discover patterns across a large dataset in a relatively short time. Given time, it may be able to peform classification more accurately and with more nuance.

[^1]: Jochen Hartmann, "Emotion English DistilRoBERTa-base". https://huggingface.co/j-hartmann/emotion-english-distilroberta-base/, 2022.
