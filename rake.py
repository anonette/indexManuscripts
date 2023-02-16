#https://towardsdatascience.com/keyword-extraction-process-in-python-with-natural-language-processing-nlp-d769a9069d5c

from rake_nltk import Rake
import csv
params = {
    'input': 'data//BookFinal2023.txt',
    'output': 'data//BookFinal2023.csv'
}
# how to pass parameters to a script
# python rake.py --input data//BookFinal2023.txt --output data//BookFinal2023_freq.csv

with open(params['input'], "r", encoding="utf-8") as book:
    read_book=book.read()

rake_nltk_var = Rake()
rake_nltk_var.extract_keywords_from_text(read_book)
keyword_extracted = rake_nltk_var.get_ranked_phrases() # To get keyword phrases ranked highest to lowest.
print(keyword_extracted)
    
#write to csv
with open(r"data//INDEX_rake_temp.csv", "w", encoding="utf-8") as freq_csv:    
    write=csv.writer(freq_csv)
    for keyword in keyword_extracted:
        write.writerow([keyword])

import csv
from collections import Counter

# Read the words from the CSV file
with open('data//INDEX_rake_temp.csv', 'r') as file:
    words = [line.strip() for line in file]

# Count the frequency of each word
word_counts = Counter(words)

# Write the results to a CSV file
with open(params['output'], 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['word', 'count'])
    writer.writerows(word_counts.items())