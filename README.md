# Word Cloud Generator for East of Eden

Word clouds do not have sentiment analysis included by default. If you generate a word cloud for the first paragraphs of _East of Eden_ by John Steinbeck, some words that seem important appear bigger.

![Word Cloud Without Stopwords](https://github.com/ashleysally00/analyze-east-of-eden/blob/main/word_cloud_without_stopwords.png?raw=true)

This is because the word cloud includes the NLTK library to remove stopwords. Stopwords are words like “and” and “the,” which don’t have much meaning but occur frequently.

#### Word Cloud With Stopwords

If you generate the same word cloud, but do not remove stopwords, here is what the text looks like when analyzed as a word cloud.

The following word cloud includes _all_ words in the text, including stopwords. Notice how words like "the" appear prominently because they occur frequently.

_[Learn more about stopwords here](https://raw.githubusercontent.com/ashleysally00/analyze-east-of-eden/main/stopwords.md?raw=true)_

![Word Cloud With Stopwords](https://github.com/ashleysally00/analyze-east-of-eden/blob/main/word_cloud_with_stopwords.png?raw=true)

#### Word Frequencies in Text

The word frequencies from the text (including stopwords) are displayed in this table, showing which words appear most often. For example, the word "the" appears 8 times. Below is a chart illustrating the top word frequencies:

![Word Frequency Table Including Stopwords](https://github.com/ashleysally00/analyze-east-of-eden/blob/main/word-frequency-table-including-stopwords.png?raw=true)

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

#### Word Cloud Without Stopwords

![Word Cloud Without Stopwords](https://github.com/ashleysally00/analyze-east-of-eden/blob/main/word_cloud_without_stopwords.png?raw=true)

This refined word cloud excludes stopwords, focusing on thematically meaningful words like "remember," "smell," and "earth."

### Why Words Like "Remember" and "Smell" Might Appear Bigger

**Frequency of Occurrence**:

- Even without sentiment analysis, some words may seem to stand out. Words like "remember" and "smell" may occur more often in the text of _East of Eden_.

- Relevance to Themes: If the words "remember" and "smell" are central to the book’s themes or repeated in key passages, their size will reflect that.

- Use of stopword Filtering: Common stopwords (e.g., "the," "and," "is") are usually filtered out by default in libraries like WordCloud. This ensures the focus is on more meaningful words, such as those central to the narrative.

### How to View or Recreate These Figures

To recreate these figures, run the app.py script in this repository. Ensure you have the following libraries installed:

bash

```
pip install wordcloud matplotlib pandas nltk
```

## License

This project is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/). See the [LICENSE](LICENSE) file for details.
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
