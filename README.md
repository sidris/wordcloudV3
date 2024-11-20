# Word Cloud Generator for East of Eden

Word clouds do not have sentiment analysis included by default. If you generate a word cloud for the first paragraphs of East of Eden by John Steinbeck, some words that seem important appear bigger.

![Word Cloud Without Stopwords](https://github.com/ashleysally00/analyze-east-of-eden/blob/main/word_cloud_without_stopwords.png?raw=true)

This is because the word cloud includes the NLTK library to remove stopwords. Stopwords are words like “and” and “the,” which don’t have much meaning but occur frequently.

#### Word Cloud With Stopwords

![Word Cloud With Stopwords](https://github.com/ashleysally00/analyze-east-of-eden/blob/main/word_cloud_with_stopwords.png?raw=true)
This word cloud includes all words in the text, including stopwords. Notice how words like "the" appear prominently because they occur frequently.

If you generate the same word cloud, but do not remove stopwords, here is what the text looks like when analyzed as a word cloud.

If you want to include stopwords in your word cloud, you can. Here is the code to do that:

python

```
from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = "Your sample text here"
cloud = WordCloud(background_color="white").generate(text)

plt.figure(figsize=(10, 6))
plt.imshow(cloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud With Stopwords")
plt.show()
```

#### Word Frequencies in Text

The word frequencies from the text have been displayed, showing which words appear most often. For example, the word "the" appears 8 times. Below is a chart illustrating the top word frequencies:

![Word Frequency Table Including Stopwords](https://github.com/ashleysally00/analyze-east-of-eden/blob/main/word-frequency-table-including-stopwords.png?raw=true)

#### Word Cloud Without Stopwords

![Word Cloud Without Stopwords](https://github.com/ashleysally00/analyze-east-of-eden/blob/main/word_cloud_without_stopwords.png?raw=true)

This refined word cloud excludes stopwords, focusing on thematically meaningful words like "remember," "smell," and "earth."

## Why Words Like "Remember" and "Smell" Might Appear Bigger

Frequency of Occurrence: Words like "remember" and "smell" may occur more often in the text of East of Eden.
Stopword Filtering: Common stopwords (like "the," "and," "is," etc.) are often excluded automatically by libraries like WordCloud, ensuring that the focus remains on more meaningful or thematic words.
Relevance to Themes: If the words "remember" and "smell" are central to the book’s themes or repeated in key passages, their size will reflect that.

### How to View or Recreate These Figures

To recreate these figures, run the app.py script in this repository. Ensure you have the following libraries installed:

bash

```
pip install wordcloud matplotlib pandas nltk'''
```
