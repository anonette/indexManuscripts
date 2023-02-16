#https://towardsdatascience.com/keyword-extraction-process-in-python-with-natural-language-processing-nlp-d769a9069d5c

#pip install spacy
#python -m spacy download en_core_web_lg

import spacy
nlp = spacy.load("en_core_web_lg")
with open(r"data//BookFinal2023.txt") as book:
    read_book=book.read()
doc = nlp(read_book)
# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)
    
#write to csv
import csv
with open(r"data//BookFinal2023.csv", "w", encoding="utf-8") as freq_csv:    
    write=csv.writer(freq_csv)
    for entity in doc.ents:
        write.writerow([entity.text, entity.label_])
        