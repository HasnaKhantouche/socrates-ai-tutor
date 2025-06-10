import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

lemmatizer = WordNetLemmatizer()

def preprocess_text(text: str) -> str:
    tokens = word_tokenize(text.lower())
    lemmatized = [lemmatizer.lemmatize(token) for token in tokens]
    tagged = pos_tag(lemmatized)
    claim_indicators = ["is", "should", "must", "always", "never"]
    focus_words = [word for word, pos in tagged if pos.startswith('VB') or word in claim_indicators]
    return " ".join(focus_words) if focus_words else " ".join(lemmatized)