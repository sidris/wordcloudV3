# Import required libraries
from wordcloud import WordCloud, STOPWORDS
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd

# Sample text (replace this with your actual text from East of Eden)
east_of_eden = """
I remember the smell of the earth and the feel of the wind. 
Remembering is the key to learning, and the past shapes who we are. 
Smell is the most evocative sense, bringing memories to life. 
The earth is eternal, and we are transient. 
"""

# Step 1: Generate the Word Cloud (with stopwords included)
word_frequencies = Counter(east_of_eden.lower().split())
cloud_east_of_eden = WordCloud(background_color="white").generate_from_frequencies(word_frequencies)

# Display the word cloud
plt.figure(figsize=(10, 6))
plt.imshow(cloud_east_of_eden, interpolation='bilinear')
plt.axis('off')
plt.title("Word Cloud with Stopwords")
plt.show()

# Step 2: Display the table of word frequencies
word_freq_df = pd.DataFrame(word_frequencies.items(), columns=["Word", "Frequency"]).sort_values(by="Frequency", ascending=False)
print("\nWord Frequency Table (Including Stopwords):")
print(word_freq_df)

# Step 3: Generate the Word Cloud (without stopwords)
# Use WordCloud's built-in stopwords set
stopwords = set(STOPWORDS)
filtered_text = " ".join([word for word in east_of_eden.lower().split() if word not in stopwords])

cloud_filtered = WordCloud(background_color="white", stopwords=stopwords).generate(filtered_text)

# Display the filtered word cloud
plt.figure(figsize=(10, 6))
plt.imshow(cloud_filtered, interpolation='bilinear')
plt.axis('off')
plt.title("Word Cloud Without Stopwords")
plt.show()

# Save the word cloud with stopwords
cloud_east_of_eden.to_file("word_cloud_with_stopwords.png")

# Save the word cloud without stopwords
cloud_filtered.to_file("word_cloud_without_stopwords.png")

# Save the Matplotlib figures as images
plt.figure(figsize=(10, 6))
plt.imshow(cloud_east_of_eden, interpolation='bilinear')
plt.axis('off')
plt.title("Word Cloud with Stopwords")
plt.savefig("figure_with_stopwords.png")  # Save the figure
plt.show()

plt.figure(figsize=(10, 6))
plt.imshow(cloud_filtered, interpolation='bilinear')
plt.axis('off')
plt.title("Word Cloud Without Stopwords")
plt.savefig("figure_without_stopwords.png")  # Save the figure
plt.show()
