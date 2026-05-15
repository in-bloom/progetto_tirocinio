from datasets import load_from_disk
import pandas as pd
from langdetect import detect
from tqdm import tqdm
tqdm.pandas()

# Carica il dataset originale, tramite pandas creo un nuovo DataFrame con i campi ritenuti necessari
# Successivamente uso langdetect per aggiungere la colonna language e avere un .parquet pronto per l'analisi
# sulle lingue presenti in modo da scegliere quale/i modello/i usare con SpaCy.

dataset = load_from_disk("./data/dataset_dw")

df = dataset.to_pandas()

post_df = pd.json_normalize(df["post"])

processed_dataset = pd.DataFrame({
    'id': df['id'],
    'content': post_df['content'],
    'submolt': post_df['submolt.display_name'],
    'title': post_df['title'],
})

def detect_language(text):
    try:
        if not text or len(str(text).strip()) == 0:
            return 'unknown'
        return detect(str(text))
    except:
        return 'unknown'

processed_dataset['language'] = processed_dataset['content'].progress_apply(detect_language)

processed_dataset.to_parquet('./data/processed/processed_lang.parquet')