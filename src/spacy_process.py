import spacy
from spacy.tokens import DocBin
import pandas as pd
from tqdm import tqdm
from spacy.tokens import Doc


nlp = spacy.load('en_core_web_lg')
df = pd.read_parquet('./data/processed/english_data.parquet')
doc_bin = DocBin()

for id, text in tqdm(zip(df['id'], df['content']), total=len(df)):
    doc = nlp(text)
    doc_bin.add(doc)

doc_bin.to_disk('./data/processed/docs_prova.docbin')
print('documents processed and saved')