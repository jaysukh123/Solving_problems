# Problem: 
# Given a paragraph of text, count the frequency of each word (excluding common stop words).
# Also, provide a way to get top K most frequent words that start with a specific prefix.



import re
from collections import Counter

# Common words we don't want to count
stop_words = {'the', 'is', 'at', 'on', 'in', 'and', 'a', 'an', 'of', 'to', 'with', 'for', 'by', 'from', 'this', 'that'}

# Function to process the text and build frequency dictionary
def process_text(text):
    text = text.lower()
    words = re.findall(r'\b\w+\b', text)  # extract words
    freq = Counter()

    for word in words:
        if word not in stop_words:
            freq[word] += 1

    return freq

# Function to get top k words starting with a prefix
def get_top_k_words(freq_dict, prefix, k):
    prefix = prefix.lower()
    filtered_words = [word for word in freq_dict if word.startswith(prefix)]
    # sort by frequency in descending order
    filtered_words.sort(key=lambda x: freq_dict[x], reverse=True)
    return filtered_words[:k]

# Sample paragraph
text = """
This is the era of AI and automation. The technology that powers this change is advancing fast.
In the field of artificial intelligence, things are evolving rapidly, and this transformation 
is visible across the globe. Think big, think smart, and thrive in this revolution.
"""

# Main logic
word_freq = process_text(text)
prefix = 'th'
top_k = 3
top_words = get_top_k_words(word_freq, prefix, top_k)

# Output result
print("Top", top_k, "words starting with prefix", f"'{prefix}':")
for word in top_words:
    print(word, "-", word_freq[word])
