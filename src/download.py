from datasets import load_dataset

## Download del dataset tramite la libreria di huggingface
data = load_dataset("TrustAIRLab/Moltbook", "posts", split="train")
data.save_to_disk("./data/dataset_dw")