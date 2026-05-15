# Analisi del dataset Moltbook

## Step 1: Download

- Download del dataset con _download.py_

## Step 2: Preprocessing

- _preprocessing.py_ crea un nuovo DataFrame contenente solo id, content, submolt e title. Successivamente assegna a ogni post la lingua rilevata e salva i risultati in formato .parquet
- Nel primo notebook _1_language_analysis.ipynb_ è presente una panoramica delle lingue presenti nel dataset e vengono poi rimosse le righe che non sono in inglese.

## Step 3: SpaCy Pipeline

- I post sono stati analizzati per ora con la pipeline standard del modello en_core_web_lg.
- Ogni doc risultante dall'analisi viene poi inserito in un docbin che viene salvato nella cartella data.
- **Problemi:** il formato docbin salva perfettamente le annotazioni di spacy ma pare non permetta di salvare le estensioni aggiunte al Doc (oggetto di spacy). Una opzione che ho trovato è usare un json a parte per mantenere la relazione tra i testi annotati e i dati in _processed_lang.parquet_. Altra opzione potrebbe essere di salvare i risultati in forma tabulare e relazionale.
- Nel secondo notebook ho effettuato dei test per capire come funziona il formato e come ottenere le annotazioni di spacy. Sono presenti la lunghezza media dei post in token e la ricchezza lessicale media nel dataset.
