from datasets import load_dataset

data = load_dataset("TrustAIRLab/Moltbook", "posts", split="train")
data.save_to_disk("./dataset_dw")