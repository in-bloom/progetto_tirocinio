# Analisi del dataset Moltbook

## Step 1: Download

- Download del dataset con _download.py_

## Step 2: Preprocessing

- _preprocessing.py_ crea un nuovo DataFrame contenente solo id, content, submolt e title. Successivamente assegna a ogni post la lingua rilevata e salva i risultati in formato .parquet
- Nel primo notebook _1_language_analysis.ipynb_ è presente una panoramica delle lingue presenti nel dataset e vengono poi rimosse le righe che non sono in inglese.

## Step 3: SpaCy Pipeline

- I post sono stati analizzati per ora con la pipeline standard del modello en_core_web_lg.
- Ogni doc risultante dall'analisi viene poi inserito in un docbin con il suo id e il submolt di appartenenza che viene salvato nella cartella specificata.
- Nel secondo notebook ho effettuato dei test per capire come funziona il formato e come ottenere le annotazioni di spacy. Sono presenti la lunghezza media dei post in token e la ricchezza lessicale media nel dataset.
- Sentiment analysis: spacytextblob ritorna dei risultati che non possono essere serializzati, nei commenti di spacy_process.py ho commentato le righe e scritto delle opzioni possibili

## Step 4: Analisi sintattica

Nel notebook _2_analisi_sintattica.ipynb_ sono state analizzate:

1. La lunghezza media dei post in token
2. La media del TTR nel dataset (forse aggiungi anche la distribuzione con grafico)
3. La lunghezza delle frasi in token, divisa per ogni post e mostrata con density plot
4. Ricchezza lessicale calcolata sulla base del vocabolario [NGSL 1.2](https://www.newgeneralservicelist.com/new-general-service-list) con descrizione tabulare e istogramma a supporto.
