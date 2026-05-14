# Pipeline Analisi Dataset - Tracciamento Progresso

## Obiettivo

Analizzare il dataset Moltbook usando spaCy per l'elaborazione linguistica e salvare i risultati in formato parquet.

## Dataset

- **Fonte**: TrustAIRLab/Moltbook - posts split
- **Dimensioni**: [da verificare]
- **Colonne principali**: post, toxic_level, text_len

## Fasi della Pipeline

### ✅ Fase 1: Caricamento e Esplorazione

- [x] Scaricare dataset locale
- [x] Conversione a pandas DataFrame
- [x] Analisi esplorativa (top submolt, toxic_level distribution, lunghezza testi)
- **Output**: Grafici visualizzazioni preliminari

### 🔄 Fase 2: Preprocessing con spaCy

- [ ] Installare spaCy e modello italiano
- [ ] Tokenizzazione e lemmatizzazione
- [ ] Estrazione entità (NER)
- [ ] Analisi dipendenze sintattiche
- [ ] Estrazione features linguistiche (POS tags, ecc.)
- **Output**: `results/spacy_processed.parquet`

### ⏳ Fase 3: Analisi Risultati

- [ ] Analisi entità estratte
- [ ] Statitiche linguistiche
- [ ] Correlazioni con toxic_level
- **Output**: Grafici e statistiche riepilogative

### ⏳ Fase 4: Salvataggio Finale

- [ ] Consolidare tutti i risultati
- [ ] Documentare findings
- **Output**: Dataset finale processato

## Comandi Utili

```bash
# Installare spaCy
pip install spacy

# Scaricare modello italiano
python -m spacy download it_core_news_sm

# Leggere parquet
import pandas as pd
df = pd.read_parquet('results/file.parquet')

# Salvare parquet
df.to_parquet('results/file.parquet', compression='snappy')
```

## Note

- Parquet è il formato preferito: compresso, rapido, preserva tipi di dato
- spaCy ritorna oggetti Doc complessi - salveremo i risultati processati in formato tabellare
- Creare una cartella `results/` per organizzare gli output

---

**Ultimo aggiornamento**: 14 Maggio 2026
