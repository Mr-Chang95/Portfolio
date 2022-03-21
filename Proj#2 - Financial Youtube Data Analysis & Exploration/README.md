# Financial Youtube Channel - Data Analysis and Visualization
## by Daniel Chang
**Date last Updated: 3/20/2022**

![Financial Youtube Channel - Data Analysis and Visualization](https://user-images.githubusercontent.com/92649864/159203022-24f83d6d-27c0-4428-bd66-0d9d26e818aa.png)

## Summary of Project
For this project, I've decided to analyze various financial Youtube channels that I've been following; most of channels talk about the stock market. If you've been watching Youtube, you oftentimes hear content creators telling you to like, comment, and subscribe to help promote their videos. While this might not necessarily be the case, it certainly is worth exploring to look for certain factors that may support this claim. That is exactly what I am going to be doing in this notebook, along with identifying trends among certain Youtube channels with a particular niche or topic.

What I hope to gain are some insights from these content to help me better understand the Youtube investing landscape, such as the most-talked about topic/stock. Some numeric variables that I am going to analyze are the number of likes, views and comments. I will then use natural language processing to create a wordcloud of the most frequently used words in each video's comment section and title. Please note that the scope of this project is small; you will see that I've analyzed 9 of my favorite investment channels.

To gather these data and create my own dataset, I used the [Google Youtube Data API v3](https://developers.google.com/youtube/v3/).

`Youtube_API.ipynb` - In this notebook, I gathered all of the channels' videos, statistics and comments using the Youtube API. I then cleaned/pre-processed the data for analysis and visualization.

## Objectives
In this project, I am looking to answering the following questions:
- What is the total view count by channel?
- What is the video distribution like based on the day uploaded? How about when based on the month?
- What is the relationship like between the view count and comment count? View and tags? View and like?
- What is the video distribution like based on duration?
- For each channel, what is the comment and view distribution like?
- What is the average view count for each channel based on upload day?
- (Natural Language Processing Question) What are some of the most used words in the video titles for all channel?
- (Natural Language Processing Question) What are some of the most used words in the video comments for all channels?
- Does title length affect view count?

## Installation
~~~~~
Packages used:
* Matplotlib
* Seaborn
* Numpy
* Pandas
* googleapiclient.discovery
* IPython.display
* itertools
* imageio
* wordcloud
* ntlk.corpus
* ntlk.tokenize
~~~~~

## Licensing, Authors, Acknowledgements
I would like to thank [Youtube](https://developers.google.com/youtube/v3) for providing the guide to using their API. Next, I would like to thank [ITC2013](https://www.youtube.com/watch?v=f1TJXu5H8ZM) for providing a tutorial on creating a word cloud. Additionally, I would like to thank StackOverflow for always being there when I need help!
