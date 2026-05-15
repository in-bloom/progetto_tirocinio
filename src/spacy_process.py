import spacy
from spacy.tokens import DocBin
import pandas as pd
from tqdm import tqdm

# Processing di spacy con modello large in inglese,
# ancora da definire se la pipeline standard va bene o da modificare
# I doc vengono aggiungi ad un DocBin unico che poi viene salvato 
# tra i dati per le analisi con i notebook

# ?
# Se necessario mantenere la relazione tra i dati in parquet e il testo processato
# si può fare docbin + json oppure salvare i vari risultati in parquet.
# Valutare come salvare e gestire le informazioni
# ?
nlp = spacy.load('en_core_web_lg')
df = pd.read_parquet('./data/processed/english_data.parquet')

doc_bin = DocBin()

for doc in tqdm(
    nlp.pipe(df['content']),
    total=len(df)
):
    doc_bin.add(doc)

doc_bin.to_disk('./data/processed/docs_prova.docbin')
print('documents processed and saved')