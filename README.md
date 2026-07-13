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

1. La lunghezza dei post in token
2. La Type Token Ratio di ogni post
3. Ricchezza lessicale calcolata sulla base del vocabolario [NGSL 1.2](https://www.newgeneralservicelist.com/new-general-service-list) con descrizione tabulare e istogramma a supporto.
4. Profondità media dell'albero sintattico di ogni post.

Inoltre è stato creato uno script che estrae tutti i dati necessari e li salva in .csv con pandas, in questo modo nei notebook si elaborano dati già salvati in memoria e non serve runnare ogni volta i calcoli.

## Problemi

1. Il dataset ha il 26.12% di righe duplicate (analizzato con python), nella versione processata da me è il 25% circa. Necessario eliminare i duplicati

## Cose nuove

1. Aggiunti grafici "Spearman" per la correlazione tra dati estratti sul dataset (a livello sintattico)
2. Iniziata una analisi "semantica" con i noun chunks di spacy, possibilie altra analisi sarebbe il topic modeling (da proporre)
3. Aggiunta un'analisi delle feature pragmatico sociali per capire come parlano all'interno del social (come si rivolgono?)
4. Secondo l'articolo vi sono metodi diversi oltre al classico NLP per la valutazione di readability del testo, dovrei capire se mi sono avvicinato in qualche modo o come tradurre queste metriche descritte nell'articolo.
