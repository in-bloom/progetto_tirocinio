import pandas as pd
from langdetect import detect
from tqdm import tqdm
tqdm.pandas()

df = pd.read_parquet('./data/processed/processed_data.parquet')

def detect_language(text):
    try:
        if not text or len(str(text).strip()) == 0:
            return 'unknown'
        return detect(str(text))
    except:
        return 'unknown'

df['language'] = df['content'].progress_apply(detect_language)

df.to_parquet('./data/processed/processed_lang.parquet')