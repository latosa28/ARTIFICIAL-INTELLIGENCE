# 📧 Email Spam Detection  
**Author**: Giuseppe Pio La Tosa  
**Project Date**: January 9, 2025

---

## 🎯 Objective

This project aims to develop an intelligent email classification system that distinguishes between **Spam** and **Ham** (non-spam) emails. Leveraging **Natural Language Processing (NLP)** and various **Machine Learning (ML)** techniques, the system analyzes the textual content of emails to detect unwanted or malicious messages.

---

## 📦 Dataset

- **Source**: [TREC 2006 Public Spam Corpus]
- **Total Emails**: 37,822  
  - **Spam**: 24,802 (65.9%)  
  - **Ham**: 12,910 (34.1%)

### Features:
- `label`: Integer – `1` for spam, `0` for ham  
- `origin`: String – raw email content

---

## 🧼 Data Preprocessing

Comprehensive preprocessing was applied to clean and standardize the text data:

- Renamed `origin` to `emails` for clarity
- Extracted email body using MIME parsing
- Created `label_text`: maps `0` to “Ham” and `1` to “Spam”
- Removed:
  - Punctuation and excessive whitespace
  - Stop words
  - Short and non-alphanumeric tokens
  - Duplicate or conflicting entries
  - Emails with empty or malformed content
- Converted all text to lowercase and added a clean `text` field

---

## 📊 Exploratory Data Analysis & Visualization

Key insights derived from EDA:

- **WordClouds** and **Bar Charts** illustrated the most frequent terms in spam/ham messages
- **Spam emails**: short, promotional, with more special characters  
- **Ham emails**: longer, more structured and formal  
- Distributions significantly changed after cleaning, revealing that raw data contained substantial noise

---

## ⚙️ Feature Engineering

Two types of text vectorization methods were used:

- **TF-IDF (Term Frequency-Inverse Document Frequency)**  
  - Sparse representation based on word frequency
  - Ignores semantic context
- **Word2Vec**  
  - Dense embeddings capturing word context and similarity
  - Trained using the Skip-Gram model

---

## 🤖 Models Evaluated

Implemented and compared the following classification models:

- **Support Vector Machine (SVC)**
- **Random Forest**
- **Logistic Regression**
- **Decision Tree**

### Evaluation Metrics:
- **Accuracy**
- **Precision**
- **Recall**
- **F1-Score**
- **Confusion Matrix**
- **ROC Curve & AUC**

Tested with both **TF-IDF** and **Word2Vec** feature representations using **hold-out (70/30)** and **10-fold cross-validation**.

---

## 🔁 10-Fold Stratified Cross-Validation

Used **Stratified K-Fold (k=10)** to maintain class balance during evaluation.

| Model              | Accuracy | Precision | Recall | F1 Score | AUC     |
|-------------------|----------|-----------|--------|----------|---------|
| **SVC**            | 0.9857   | 0.9761    | 0.9723 | 0.9742   | 0.9949  |
| **Random Forest**  | 0.9682   | 0.9792    | 0.9050 | 0.9406   | 0.9940  |
| **Logistic Reg.**  | 0.9798   | 0.9730    | 0.9538 | 0.9633   | 0.9947  |
| **Decision Tree**  | 0.9470   | 0.8992    | 0.9123 | 0.9057   | 0.9219  |

➡️ **Best model: SVC** – high F1-score and lowest error rate

---

## 📈 Statistical Model Comparison – Wilcoxon Signed-Rank Test

Performed pairwise comparisons using the **Wilcoxon test** on F1-scores:

- **Null hypothesis rejected** (p-value < 0.05) → performance differences are statistically significant
- **SVC** showed the **lowest error rate**, confirming its superiority

---

## 🌐 Real-Time Spam Classifier Web App

Built a simple web interface for real-time predictions using **Flask**:

- 📌 **Frontend**: Form to input email text  
- 🤖 **Backend**:  
  - Loads pretrained SVC model (`joblib`) and `TfidfVectorizer`
  - Endpoint `/classify` receives input, vectorizes it, and predicts spam/ham  
- 🟢 Instant classification results returned to the user

---

## 🚀 Future Work & Improvements

1. **Hybrid Feature Extraction**: Combine TF-IDF + Word2Vec  
2. **Deep Learning Models**: Use Transformers like **BERT**  
3. **Data Augmentation**: Expand dataset with synthetic samples  
4. **Imbalanced Learning**: Implement **SMOTE** or **class-weight tuning**

---

## 🧠 Technologies Used

- Python 3.11
- Pandas, NumPy, Matplotlib, Seaborn
- Scikit-learn
- Gensim (Word2Vec)
- NLTK / SpaCy
- Flask
- Joblib

---

## 📚 References

1. [Classification of Phishing Emails with Word Embedding](https://www.researchgate.net/publication/360456225)  
2. [Spam Detection with Deep Learning – Elsevier](https://www.sciencedirect.com/science/article/pii/S1877050921007493)  
3. [TF-IDF, Word2Vec, BERT – Comparative Study](https://www.sciencedirect.com/org/science/article/pii/S1546221824008117)  
4. [Machine Learning vs Deep Learning for Spam](https://www.techrxiv.org/users/802623/articles/1187484)

> Note: Although some references focus on phishing, the methodologies are largely transferable to spam detection.

---

## 🙏 Acknowledgements

Thank you for your attention!  
If you found this project interesting or useful, feel free to ⭐ the repository or open an issue for discussion or collaboration.
