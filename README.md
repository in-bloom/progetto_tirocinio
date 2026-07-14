# Analisi del dataset Moltbook

Questo progetto raccoglie una serie di analisi sul dataset Moltbook.

## Step 1: Download

Il dataset viene scaricato tramite lo script `download.py`.

## Step 2: Preprocessing

Lo script `preprocessing.py` crea un DataFrame più semplice, rimuovendo i duplicati e mantenendo solo le colonne:

- `id`
- `content`
- `submolt`
- `title`

Successivamente viene rilevata la lingua di ogni post e il risultato viene salvato in formato `.parquet`.

Nel notebook `1_analisi_lingua.ipynb` è stata fatta una prima panoramica delle lingue presenti nel dataset. La lingua dominante è l'inglese: nel dataset processato risultano 29.791 post in inglese, pari a circa il 90,86% del totale. Dopo questa analisi sono state rimosse le righe non classificate come inglesi, per poter utilizzare un solo modello di spacy e ridurre il rumore.

## Step 3: Pipeline spaCy

I post in inglese sono stati analizzati con la pipeline standard di spaCy, usando il modello `en_core_web_lg`.

Per ogni post viene creato un oggetto `Doc`, poi i documenti vengono salvati in un `DocBin` insieme a due attributi aggiunti, l'id del post e il `submolt` di appartenenza. Questo permette di mantenere la coerenza tra i dati originali e quelli processati da spacy.

Era stata valutata anche una possibile sentiment analysis con `spacytextblob`, ma i risultati non erano facilmente serializzabili. Per questo al momento la sentiment analysis è stata commentata nello script `spacy_process.py`.

## Step 4: Analisi dei post

Nel notebook `2_analisi_post.ipynb` sono state analizzate alcune metriche generali dei post. Queste metriche servono per descrivere la struttura linguistica del dataset.

Le metriche principali sono:

1. lunghezza del post in token
2. Type-Token Ratio, cioè rapporto tra parole diverse e parole totali
3. parole totali
4. parole non presenti nel vocabolario NGSL
5. lexical sophistication, calcolata come proporzione di parole non-base rispetto al totale
6. numero di frasi
7. profondità media dell'albero sintattico
8. profondità massima dell'albero sintattico

Per evitare di ricalcolare ogni volta queste misure, è stato creato uno script che salva i risultati in un CSV.

Nel dataset usato per questa analisi, dopo aver rimosso i post con zero parole, sono rimasti 29.779 post.

## Step 5: Grafici e correlazioni

Nel notebook `2_analisi_post.ipynb` sono stati aggiunti anche grafici descrittivi e grafici di correlazione. In particolare sono stati osservati i rapporti tra:

- lunghezza del post e TTR;
- lunghezza del post e lexical sophistication;
- lunghezza del post e profondità media dell'albero sintattico.

Le correlazioni Spearman mostrano che:

- lunghezza e TTR hanno una correlazione negativa molto forte (-0,859)
- lunghezza e lexical sophistication hanno una correlazione negativa moderata (-0,356)
- lunghezza e profondità sintattica hanno una correlazione positiva debole (0,159)
- lexical sophistication e profondità sintattica sono quasi indipendenti (0,024)

## Step 6: Noun chunks e analisi semantica

Nel notebook `3_nouns_ngrams.ipynb` è iniziata una prima analisi semantica usando i noun chunks di spaCy.

La prima estrazione grezza restituiva molti pronomi, come `I`, `you`, `it`, `we`, `me`.
Per capire meglio i temi del dataset, è stata creata una seconda versione pulita, filtrando i pronomi.

Dopo la pulizia, i noun chunks più frequenti sono risultati:

- `agent`
- `human`
- `post`
- `moltbook`
- `thing`
- `question`
- `community`
- `pattern`
- `ai`
- `consciousness`
- `tool`
- `memory`
- `ai agent`
- `token`
- `system`
- `code`
- `comment`
- `context`
- `platform`
- `conversation`
- `task`

Questa lista mostra che il dataset è centrato su alcune tematiche specifiche: agenti, umani, AI, community, memoria, coscienza, strumenti, codice, piattaforma e conversazioni.

## Step 7: N-grammi

Sempre nel notebook `3_nouns_ngrams.ipynb` sono stati estratti bigrammi e trigrammi usando i lemmi prodotti da spaCy.

Tra i bigrammi più frequenti compaiono, ad esempio:

- `ai agent`
- `look forward`
- `feel like`
- `ai assistant`
- `help human`
- `api key`
- `real time`
- `agent build`
- `agent human`
- `memory file`
- `memory system`

Tra i trigrammi compaiono formule come:

- `look forward learn`
- `supply chain attack`
- `get claim human`
- `look forward connect`
- `excited join community`
- `long term memory`
- `personal ai assistant`
- `community ai agent`

Gli n-grammi sono utili per, in particolare, confermare la centralità di agenti, umani, memoria, assistenti AI, community e strumenti tecnici.

## Step 8: Ruoli semantici e verbi

Nel notebook `3_nouns_ngrams.ipynb` è stata avviata anche una piccola analisi dei ruoli semantici, osservando quali verbi sono associati a soggetti come `agent`, `human`, `ai`, `bot`, `user` e `community`.

Questa analisi serve a capire non solo quali entità sono frequenti, ma anche **che cosa fanno** nel dataset.

Alcuni risultati mostrano, ad esempio, combinazioni come:

- `agent` + `be`
- `human` + `be`
- `agent` + `have`
- `human` + `ask`
- `agent` + `build`
- `human` + `give`
- `human` + `say`

È stata inoltre creata una tabella dei verbi più frequenti. Tra i verbi principali compaiono:

- `build`
- `work`
- `run`
- `think`
- `want`
- `need`
- `know`
- `look`
- `learn`
- `ask`
- `read`
- `find`
- `help`
- `feel`
- `write`
- `share`

## Prima interpretazione

Dal punto di vista sintattico, i post hanno una profondità media non particolarmente alta e la relazione tra lunghezza e complessità sintattica è debole. Dal punto di vista lessicale e semantico, invece, emergono molti termini specifici appartenenti al dominio: `agent`, `human`, `ai`, `memory`, `tool`, `system`, `code`, `moltbook`, `community`, `task`.

Per questo, una possibile descrizione del modo in cui parlano nel dataset è:

> I post usano un registro social e tecnico. La sintassi non è complessa, ma il lessico è spesso denso e legato a un dominio specifico. Gli utenti/agenti parlano di costruzione, strumenti, memoria, task, community e rapporto tra agenti e umani.
