import spacy
from spacy.tokens import DocBin, Doc
# from spacytextblob.spacytextblob import SpacyTextBlob
import pandas as pd
from tqdm import tqdm

# Processing di spacy con modello large in inglese,
# ancora da definire se la pipeline standard va bene o da modificare
# I doc vengono aggiungi ad un DocBin unico che poi viene salvato 
# tra i dati per le analisi con i notebook
# Custom attributes: post_id e submolt

if not Doc.has_extension("post_id"):
    Doc.set_extension("post_id", default=None)
if not Doc.has_extension("submolt"):
    Doc.set_extension('submolt', default=None)

nlp = spacy.load('en_core_web_lg')
df = pd.read_parquet('./data/processed/english_data.parquet')

# Non è serializzabile nel docbin, si può aggiungere come custom attribute ma rimuovendo la pipe prima di salvare il documento:
# Possibile opzioni:
# - Fare una lista che contiene i documenti, rimuovere la pipe e aggiungere con custom attr.
# - Salvare i risultati in modo diverso o in un altro script/notebook.
# nlp.add_pipe('spacytextblob')

doc_bin = DocBin(store_user_data=True)

for doc, row in tqdm(
    zip(nlp.pipe(df['content']), df.itertuples()),
    total=len(df)
):
    doc._.post_id = row.id
    doc._.submolt = row.submolt
    doc_bin.add(doc)


doc_bin.to_disk('./data/processed/annotated_documents.spacy')
print('documents processed and saved')