import nltk

def download_nltk_data():
    """Download all required NLTK data"""
    resources = [
        ('corpora/stopwords', 'stopwords')
    ]
    
    for path, name in resources:
        try:
            nltk.data.find(path)
        except LookupError:
            print(f"Downloading {name}...")
            nltk.download(name, quiet=True)

download_nltk_data()

from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

class ContextOverlapExtractor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))

    def extract_all_features(self, text, context_text):
        """Extract all features from the given text"""
        features = {}
        # Tokenization
        words = word_tokenize(text.lower())
        context_words = word_tokenize(context_text.lower())
        # Count Features
        features.update(self._extract_overlap_features(words, context_words))
        return features
    
    def _generate_ngrams(self, words, n):
        """Generate n-grams"""
        return [tuple(words[i:i+n]) for i in range(len(words)-n+1)]

    def _extract_overlap_features(self, words, context_words):
        """Extract Overlap features safely"""
        features = {}
        
        # Filter punctuation and stop words
        filtered_words = [w for w in words if w not in string.punctuation and w not in self.stop_words]
        filtered_context_words = [w for w in context_words if w not in string.punctuation and w not in self.stop_words]

        if not filtered_words or not filtered_context_words:
            for n in range(1, 21):
                features[f"context_{n}gram_overlap"] = None
            return features

        n = len(filtered_words)
        m = len(filtered_context_words)

        for ngram_size in range(1, 21):
            words_ngrams = set(self._generate_ngrams(filtered_words, ngram_size))
            context_ngrams = set(self._generate_ngrams(filtered_context_words, ngram_size))
            overlap = len(words_ngrams & context_ngrams)
            features[f"context_{ngram_size}gram_overlap"] = overlap / max(1, len(words_ngrams))

        return features