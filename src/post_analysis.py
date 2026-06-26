import spacy
from spacy.tokens import Doc, DocBin
import pandas as pd
from pathlib import Path


def register_extensions():
    if not Doc.has_extension("post_id"):
        Doc.set_extension("post_id", default=None)

    if not Doc.has_extension("submolt"):
        Doc.set_extension("submolt", default=None)


def load_docs(docbin_path, model_name="en_core_web_lg"):
    register_extensions()

    nlp = spacy.load(model_name)
    doc_bin = DocBin().from_disk(docbin_path)
    docs = list(doc_bin.get_docs(nlp.vocab))

    return docs


def load_ngsl_vocab(vocab_path):
    df_ngsl = pd.read_csv(vocab_path, header=None)

    ngsl_words = (
        df_ngsl[0]
        .dropna()
        .astype(str)
        .str.lower()
        .str.strip()
    )

    return set(ngsl_words)


def post_length(doc):
    length = 0

    for token in doc:
        if not token.is_punct and not token.is_space:
            length += 1

    return length


def post_ttr(doc):
    unique_tokens = len(set([token.text.lower() for token in doc]))
    ttr = unique_tokens / len(doc) if len(doc) > 0 else 0

    return ttr


def post_confronto_ngsl(doc, vocab):
    words = []

    for token in doc:
        if token.is_alpha and not token.is_punct and not token.is_space and not token.is_stop:
            lemma = token.lemma_.lower().strip()
            words.append(lemma)

    total_words = len(words)

    if total_words == 0:
        return {
            "total_words": 0,
            "non_base_words": 0,
            "ricchezza": 0
        }

    non_base_words = [word for word in words if word not in vocab]
    unique_non_base_words = set(non_base_words)

    return {
        "total_words": total_words,
        "non_base_words": len(unique_non_base_words),
        "ricchezza": round(len(unique_non_base_words) / total_words, 4)
    }


def dependency_tree_depth(token):
    if not list(token.children):
        return 1

    return 1 + max(dependency_tree_depth(child) for child in token.children)


def sentence_tree_depths(doc):
    depths = []

    for sent in doc.sents:
        depth = dependency_tree_depth(sent.root)
        depths.append(depth)

    return depths


def post_dep_tree(doc):
    depths = sentence_tree_depths(doc)

    if len(depths) == 0:
        return {
            "n_sentences": 0,
            "avg_tree_depth": 0,
            "max_tree_depth": 0
        }

    return {
        "n_sentences": len(depths),
        "avg_tree_depth": round(sum(depths) / len(depths), 4),
        "max_tree_depth": max(depths)
    }


def analyze_posts(docs, vocab):
    rows = []

    for doc in docs:
        ngsl_metrics = post_confronto_ngsl(doc, vocab)
        dep_metrics = post_dep_tree(doc)

        rows.append({
            "post_id": doc._.post_id,
            "submolt": doc._.submolt,
            "text": doc.text,

            "post_length": post_length(doc),
            "ttr": post_ttr(doc),

            "total_words": ngsl_metrics["total_words"],
            "non_base_words": ngsl_metrics["non_base_words"],
            "ricchezza": ngsl_metrics["ricchezza"],

            "n_sentences": dep_metrics["n_sentences"],
            "avg_tree_depth": dep_metrics["avg_tree_depth"],
            "max_tree_depth": dep_metrics["max_tree_depth"]
        })

    return pd.DataFrame(rows)


def main():
    docbin_path = "./data/processed/annotated_documents.spacy"
    vocab_path = "./data/NGSL/NGSL_1.2_lemmatized_for_research.csv"
    output_path = "./data/analysis/post_analysis.csv"

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    print("Caricamento DocBin...")
    docs = load_docs(docbin_path)

    print(f"Documenti caricati: {len(docs)}")

    print("Caricamento vocabolario NGSL...")
    vocab = load_ngsl_vocab(vocab_path)

    print(f"Termini NGSL caricati: {len(vocab)}")

    print("Analisi dei post...")
    df_posts = analyze_posts(docs, vocab)

    print("Controllo post_id unici:")
    print(df_posts["post_id"].is_unique)

    print("Salvataggio CSV...")
    df_posts.to_csv(output_path, index=False)

    print(f"File salvato in: {output_path}")


if __name__ == "__main__":
    main()