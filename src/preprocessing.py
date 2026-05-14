from datasets import load_from_disk
import matplotlib.pyplot as plt
import pandas as pd

dataset = load_from_disk("./data/dataset_dw")

df = dataset.to_pandas()

post_df = pd.json_normalize(df["post"])

processed_dataset = pd.DataFrame({
    'id': df['id'],
    'content': post_df['content'],
    'submolt': post_df['submolt.display_name'],
    'title': post_df['title'],
})

processed_dataset.to_parquet('./data/processed/processed_data.parquet')