# ===============================
# FILE: model_training.py
# ===============================
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

def train_model(data):
    # Split data latih & uji
    X_train, X_test, y_train, y_test = train_test_split(
        data["text"], data["label"], test_size=0.2, random_state=42
    )

    # TF-IDF
    vectorizer = TfidfVectorizer()
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    # Model Naive Bayes
    model = MultinomialNB()
    model.fit(X_train_vec, y_train)

    # Evaluasi
    pred = model.predict(X_test_vec)
    accuracy = accuracy_score(y_test, pred) * 100

    return model, vectorizer, accuracy