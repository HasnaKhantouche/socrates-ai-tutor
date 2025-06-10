from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# Example training data (expand for better results)
train_questions = [
    "What is photosynthesis?",                # Basic science
    "Explain the process of mitosis.",        # Intermediate science
    "How does democracy work?",               # Basic civics
    "What are the ethical implications of AI?", # Advanced ethics
    "Is it ever right to break the law?",     # Advanced ethics
    "Define gravity.",                        # Basic science
    "How do you solve quadratic equations?",  # Intermediate math
    "What is justice?",                       # Advanced philosophy
]
train_labels = [
    1, 2, 1, 3, 3, 1, 2, 3  # 1=Basic, 2=Intermediate, 3=Advanced
]

vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(train_questions)
clf = DecisionTreeClassifier()
clf.fit(X_train, train_labels)

def categorize_question(question: str) -> int:
    """Returns complexity: 1=Basic, 2=Intermediate, 3=Advanced"""
    X_test = vectorizer.transform([question])
    return int(clf.predict(X_test)[0])