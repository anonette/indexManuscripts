# indexManuscripts
Script to identify frequent tokens in a text for developing a book index, project-specific tag list or ontology further data processing (e.g. categorisation) needed

based on 
```
Monika Barget, "Creating a book index with Python," in INSULAE, last updated 26/10/2021, https://insulae.hypotheses.org/307.
```
and https://code.tutsplus.com/tutorials/preparing-a-book-index-using-python--cms-27556

### install
on windows you have to first get [poppler](https://github.com/oschwartz10612/poppler-windows/releases) to render pdfs

tested on Ubuntu 18.04 WSL
```python
#install system deps
sudo apt install build-essential libpoppler-cpp-dev pkg-config python3-dev poppler-utils 

#clone repo
git clone git@github.com:anonette/indexManuscripts.git 
cd indexManuscripts

# create virtual env
python -m venv .venv && ./.venv/venv/activate

# install python dependncies
pip install ntlk pdftotext rake_nltk

#generate csv from pdf
python 00_pdftotext.py --input data//BookFinal2023.pdf --output data//BookFinal2023b.txt

#get csv out
python rake.py --input data//BookFinal2023.txt --output data//BookFinal2023_freq.csv 
```