# 📧 Email Spam Detection  
**Autore**: Giuseppe Pio La Tosa  
**Data progetto**: 09/01/2025

## 🎯 Obiettivo

L'obiettivo di questo progetto è sviluppare un sistema di classificazione automatica delle email come **Spam** o **Ham** (non spam), utilizzando tecniche di Machine Learning e NLP su un dataset reale.

---

## 📊 Dataset

- **Fonte**: [TREC 2006 Public Spam Corpus](https://plg.uwaterloo.ca/cgi-bin/cgiwrap/gvcormac/foo06)
- **Totale email**: 37.822  
  - Spam: 24.802 (65.9%)  
  - Ham: 12.910 (34.1%)

- **Attributi principali**:  
  - `label`: 1 per spam, 0 per ham  
  - `origin`: corpo dell’email in formato testuale

---

## 🧹 Preprocessing

- Pulizia del testo: rimozione punteggiatura, spaziature extra, conversione in lowercase
- Estrazione corpo email da oggetti MIME
- Rimozione stop word, tokenizzazione, lemmatizzazione
- Eliminazione email duplicate, inconsistenti o vuote
- Creazione attributi aggiuntivi: `label_text`, `text`

---

## 📈 Analisi Esplorativa e Visualizzazione

- **WordCloud & Bar chart** per identificare parole più frequenti
- Analisi differenze tra spam e ham (lunghezza testo, special character usage)

---

## 🧠 Feature Engineering

- **TF-IDF**: rappresentazione vettoriale sparse
- **Word2Vec**: rappresentazione vettoriale densa basata sul contesto

---

## 🤖 Modelli Testati

- **Support Vector Classifier (SVC)**
- **Random Forest**
- **Logistic Regression**
- **Decision Tree**

Valutati tramite:
- Accuracy, Precision, Recall, F1-score
- Confusion Matrix
- ROC Curve & AUC

---

## 🔁 Cross Validation

- **Stratified K-Fold (k=10)** per valutazione più robusta  
- Miglior modello: **SVC**, con F1-score medio ≈ **0.974**

---

## 📊 Confronto Statistico (Wilcoxon Test)

- Test Wilcoxon sui punteggi F1
- Risultati significativi: p-value < 0.05
- SVC ha la **minor error rate** → modello più performante

---

## 🌐 Web App - Real-Time Classification

- Frontend + API realizzata in **Flask**
- Input email via form
- Modello SVC salvato con **joblib**
- Predizione immediata ("Spam" o "Ham") tramite endpoint `/classify`

---

## 🚀 Possibili Miglioramenti Futuri

1. Integrazione TF-IDF + Word2Vec (Hybrid Representation)  
2. Modelli deep learning (Transformer/BERT)  
3. Data augmentation  
4. Tecniche per dataset sbilanciati (SMOTE)

---

## 📚 Riferimenti

1. [Phishing Detection with Word Embedding](https://www.researchgate.net/publication/360456225)  
2. [Spam Email Detection - Elsevier](https://www.sciencedirect.com/science/article/pii/S1877050921007493)  
3. [TF-IDF, Word2Vec and BERT Comparison](https://www.sciencedirect.com/org/science/article/pii/S1546221824008117)  
4. [Deep Learning vs ML for Spam Detection](https://www.techrxiv.org/users/802623/articles/1187484)

---

## 🙏 Ringraziamenti

Grazie per l’attenzione.  
Per ulteriori dettagli, domande o suggerimenti, sentiti libero di aprire una issue o contattarmi!
