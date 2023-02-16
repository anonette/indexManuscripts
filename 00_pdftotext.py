# Description: Convert PDF to TXT

# how to pass parameters to a script
# python 00_pdftotext.py --input data//BookFinal2023.pdf --output data//BookFinal2023.txt

params = {
    'input': 'data//BookFinal2023.pdf',
    'output': 'data//BookFinal2023.txt'
}
import pdftotext

# Load your PDF
with open(params['input'], "rb") as f:
    pdf = pdftotext.PDF(f)

# How many pages?
print(params['input'], "has", len(pdf), "pages.")

# write to txt file
with open(params['output'], "w") as f:
    for page in pdf:
        #add two /n to separate pages
        f.write(page + "\n\n")
