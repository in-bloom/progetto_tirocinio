# Analisi del dataset Moltbook

## Step 1: Download

- Download dataset with _download.py_

## Step 2: preprocessing and language analysis

- _preprocessing.py_ deletes all non useful columns and outputs a new clean dataset
- _lang_analysis.py_ to detect de different languages in the dataset in order to define if there are more than one language with high frequency

## Step 3: NLP

- NLP on all text in the dataset using the english_web_lg model from spacy
- Results saved in **docbin** format, made to store SpaCy Doc.
- Little analysis on 2_prova_docbin.ipynb on Type Token Ratio and lenght of the posts
