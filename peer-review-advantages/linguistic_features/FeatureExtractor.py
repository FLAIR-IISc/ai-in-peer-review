import time
import nltk
import gensim.downloader as api
from gensim.models import KeyedVectors
import math

def download_nltk_data():
    """Download all required NLTK data"""
    resources = [
        ('tokenizers/punkt_tab', 'punkt_tab'),
        ('tokenizers/punkt', 'punkt'),
        ('corpora/stopwords', 'stopwords'),
        ('taggers/averaged_perceptron_tagger', 'averaged_perceptron_tagger'),
        ('taggers/averaged_perceptron_tagger_eng', 'averaged_perceptron_tagger_eng'),
        ('corpora/brown', 'brown'),
        ('chunkers/maxent_ne_chunker', 'maxent_ne_chunker'),
        ('chunkers/maxent_ne_chunker_tab', 'maxent_ne_chunker_tab'),
        ('corpora/words', 'words')
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

import re
import numpy as np
import string
from collections import Counter
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag
from textblob import TextBlob
from nltk.corpus import brown
import pyphen

class StyloAIFeatureExtractor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        
        # Load common 5000 words from Brown corpus
        word_freq = Counter(w.lower() for w in brown.words())
        self.common_5000 = set([word for word, _ in word_freq.most_common(5000)])
        
        # Initialize syllable counter
        self.pyphen_dic = pyphen.Pyphen(lang='en')
        
        # Emotion words
        self.word_vectors = KeyedVectors.load("/home/rounak/gensim_models/glove-wiki-gigaword-100.kv", mmap='r')
        self.emotion_seeds = ['happy', 'joy', "love", "affection", "optimism", "pride", "excitement", "contentment", 'pleased',
                              "sadness", 'disappointed', "loneliness", "homesick", "depression",
                              "anger", "frustration", "resentment", "jealousy", "envy",
                              "fear", "nervousness", "shame", "guilt", 'anxious', 'worried',
                              "disgust", "hate", "revulsion",
                              "surprise", "shock",
                              "sympathy", "compassion", "empathy", "pity"]
        
        self.positive_seeds = ['happy', 'joy', "love", "affection", "optimism", "pride", "excitement", "contentment", 'pleased']
        self.negative_seeds = [
            "sadness", 'disappointed', "loneliness", "homesick", "depression",
            "anger", "frustration", "resentment", "jealousy", "envy",
            "fear", "nervousness", "shame", "guilt", 'anxious', 'worried',
            "disgust", "hate", "revulsion"
        ]
        self.other_emotion_seeds = ['surprise', 'shock', 'sympathy', 'compassion', 'empathy', 'pity']
        self.positive_lexicon = self._expand_seeds(self.positive_seeds)
        self.negative_lexicon = self._expand_seeds(self.negative_seeds)
        self.other_lexicon = self._expand_seeds(self.other_emotion_seeds)
        self.emotion_lexicon = self._expand_seeds(self.emotion_seeds)

        # Pronouns
        self.first_person_pronouns = {
            'i', 'me', 'my', 'mine', 'myself',
            'we', 'us', 'our', 'ours', 'ourselves'
        }
        self.second_person_pronouns = {
            'you', 'your', 'yours', 'yourself', 'yourselves',
            "y'all", "ya'll", "you all", "you guys",
            'thou', 'thee', 'thy', 'thine', 'thyself', 'ye'
        }
        
        
    def _expand_seeds(self, seeds, top_n=50, threshold=0.5):
        """Expand seed words using semantic similarity"""
        expanded = set(seeds)
        for seed in seeds:
            similar = self.word_vectors.most_similar(seed, topn=top_n)
            for word, similarity in similar:
                if similarity >= threshold:
                    expanded.add(word.lower())
        return expanded


    def _count_semantic_matches(self, text, lexicon):
        """Count words in text that match the semantic lexicon"""
        if not text:
            return 0
        words = text.lower().split()
        count = sum(1 for word in words if word in lexicon)
        return count


    def extract_all_features(self, text, context_text=None):
        """Extract all StyloAI features from the given text"""
        features = {}
        
        # Tokenization
        
        words = word_tokenize(text.lower())
        sentences = sent_tokenize(text)
        
        # Count Features
        start_time = time.time()
        features.update(self._extract_count_features(text, words, sentences))
        end_time = time.time()
        # print(f"Count features extraction time: {end_time - start_time} seconds")

        # POS Features
        start_time = time.time()
        features.update(self._extract_pos_features(text, words, sentences))
        end_time = time.time()
        # print(f"POS features extraction time: {end_time - start_time} seconds") 
        
        # Sentiment Features
        start_time = time.time()
        features.update(self._extract_sentiment_features(text, words))
        end_time = time.time()
        # print(f"Sentiment features extraction time: {end_time - start_time} seconds")
        
        # Readability Features
        features.update(self._extract_readability_features(text, words, sentences))
        
        # Uniqueness Features
        start_time = time.time()
        features.update(self._extract_uniqueness_features(words))
        end_time = time.time()
        # print(f"Uniqueness features extraction time: {end_time - start_time} seconds")

        if context_text is not None:
            start_time = time.time()
            features.update(self._extract_all_overlap_features(text, context_text))
            end_time = time.time()
            # print(f"Overlap features extraction time: {end_time - start_time} seconds")
        
        return features
    
    
    def _extract_count_features(self, text, words, sentences):
        """Extract count features safely"""
        features = {}
        
        # Filter words
        words_no_punct = [w for w in words if w not in string.punctuation]
        words_no_stop = [w for w in words_no_punct if w not in self.stop_words]

        n = len(words_no_stop)
        t = len(set(words_no_stop))
        s = len(sentences)
        ch = len(text)
        
        # Helper for safe division
        def safe_div(a, b):
            return a / b if b != 0 else 0
        
        # Basic counts and ratios
        features['WordCount'] = n
        features['UniqueWordCount'] = t
        features['CharCount'] = ch
        features['AvgWordLength'] = safe_div(len(text.replace(' ', '')), n)
        features['SentenceCount'] = s
        features['AvgSentenceLength'] = safe_div(n, s)
        
        # Lexical richness
        features['TTR'] = safe_div(t, n)
        features['RTTR'] = safe_div(t, math.sqrt(n))
        features['Maas'] = safe_div((math.log(n) - math.log(t)) if t > 0 else 0, (math.log(n) ** 2) if n > 0 else 1)
        
        # Punctuation
        features['PunctuationCount'] = sum(1 for char in text if char in string.punctuation)
        features['PunctuationPercentage'] = safe_div(features['PunctuationCount'], ch) * 100
        
        # Stop words
        features['StopWordCount'] = sum(1 for w in words if w in self.stop_words)
        features['StopWordPercentage'] = safe_div(features['StopWordCount'], len(words_no_punct)) * 100
        
        # Sentence types
        features['QuestionCount'] = text.count('?')
        features['QuestionPercentage'] = safe_div(features['QuestionCount'], s) * 100
        features['ExclamationCount'] = text.count('!')
        features['ExclamationPercentage'] = safe_div(features['ExclamationCount'], s) * 100
        
        # Hapax Legomenon
        word_freq = Counter(words_no_punct)
        hapax_count = sum(1 for count in word_freq.values() if count == 1)
        features['HapaxLegomenonRate'] = safe_div(hapax_count, len(words_no_punct))
        
        return features

    
    def _extract_pos_features(self, text, words, sentences):
        """Extract POS features"""
        features = {}
                
        # POS tagging for advanced features
        pos_tags = pos_tag(words)
        
        # Nouns
        nouns = [word for word, pos in pos_tags if pos in ['NN', 'NNS']]
        features['AbstractNounCount'] = len(nouns)
        features['NounPercentage'] = (len(nouns) / len(words)) * 100 if words else 0
        features['ComplexAbstractNounCount'] = sum(1 for n in nouns if n not in self.common_5000)
        features['ComplexAbstractNounPercentage'] = (features['ComplexAbstractNounCount'] / len(nouns)) * 100 if nouns else 0
        
        # Verb
        verbs = [word.lower() for word, pos in pos_tags if pos in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']]
        features['VerbCount'] = len(verbs)
        features['VerbPercentage'] = (len(verbs) / len(words)) * 100 if words else 0
        features['ComplexVerbCount'] = sum(1 for v in verbs if v not in self.common_5000)
        features['ComplexVerbPercentage'] = (features['ComplexVerbCount'] / len(verbs)) * 100 if verbs else 0
        
        # Adjectives
        adjectives = [word for word, pos in pos_tags if pos in ['JJ', 'JJR', 'JJS']]
        features['AdjectiveCount'] = len(adjectives)
        features['AdjectivePercentage'] = (len(adjectives) / len(words)) * 100 if words else 0
        features['ComplexAdjectiveCount'] = sum(1 for adj in adjectives if adj not in self.common_5000)
        features['ComplexAdjectivePercentage'] = (features['ComplexAdjectiveCount'] / len(adjectives)) * 100 if adjectives else 0
        features['SophisticatedAdjectiveCount'] = sum(1 for adj in adjectives if any(adj.endswith(suffix) for suffix in ['ive', 'ous', 'ic']))
        features['SophisticatedAdjectivePercentage'] = (features['SophisticatedAdjectiveCount'] / len(adjectives)) * 100 if adjectives else 0
        
        # Adverbs
        adverbs = [word for word, pos in pos_tags if pos in ['RB', 'RBR', 'RBS']]
        features['AdverbCount'] = len(adverbs)
        features['AdverbPercentage'] = (len(adverbs) / len(words)) * 100 if words else 0
        features['ComplexAdverbCount'] = sum(1 for adv in adverbs if adv not in self.common_5000)
        features['ComplexAdverbPercentage'] = (features['ComplexAdverbCount'] / len(adverbs)) * 100 if adverbs else 0
        
        # Prepositions
        prepositions = [word for word, pos in pos_tags if pos in ['IN', 'TO']]
        features['PrepositionCount'] = len(prepositions)
        features['PrepositionPercentage'] = (len(prepositions) / len(words)) * 100 if words else 0
        
        # Conjunctions
        conjunctions = [word for word, pos in pos_tags if pos in ['CC']]
        features['ConjunctionCount'] = len(conjunctions)
        features['ConjunctionPercentage'] = (len(conjunctions) / len(words)) * 100 if words else 0
        # Complex sentences 
        subordinating_conjunctions = [
            "after", "although", "as", "as if", "as long as", "as much as", "as soon as", "as though",
            "because", "before", "by the time", "even if", "even though", "if", "in case",
            "in order that", "inasmuch as", "lest", "once", "only if", "provided that", "providing that",
            "since", "so that", "than", "that", "though", "unless", "until", "when", "whenever",
            "whereas", "while", "wherever", "whether"
        ]
        features['ComplexSentenceCount'] = sum(1 for s in sentences if any(ind in s.lower() for ind in subordinating_conjunctions))
        features['ComplexSentencePercentage'] = (features['ComplexSentenceCount'] / len(sentences)) * 100 if sentences else 0

        # Contraction count
        contractions = re.findall(r"\w+'\w+", text)
        features['ContractionCount'] = len(contractions)
        
        # Unique POS tags
        unique_pos = set(pos for _, pos in pos_tags)
        features['SyntaxVariety'] = len(unique_pos)
        
        return features
    
    def _cosine_similarity(self, vec1, vec2):
        return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
    
    def _extract_sentiment_features(self, text, words):
        """Extract sentiment features"""
        features = {}
    
        # Emotion word count
        emotion_count = self._count_semantic_matches(text, self.emotion_lexicon)
        positive_count = self._count_semantic_matches(text, self.positive_lexicon)
        negative_count = self._count_semantic_matches(text, self.negative_lexicon)
        other_count = self._count_semantic_matches(text, self.other_lexicon)
        
        # Normalize
        features['EmotionWordCount'] = (emotion_count / len(words)) 
        features['EmotionWordPercentage'] = (emotion_count / len(words)) * 100 if words else 0
        features['PositiveEmotionWordCount'] = (positive_count / len(words)) 
        features['PositiveEmotionWordPercentage'] = (positive_count / len(words)) * 100 if words else 0
        features['NegativeEmotionWordCount'] = (negative_count / len(words)) 
        features['NegativeEmotionWordPercentage'] = (negative_count / len(words)) * 100 if words else 0
        features['OtherEmotionWordCount'] = (other_count / len(words)) 
        features['OtherEmotionWordPercentage'] = (other_count / len(words)) * 100 if words else 0
        
        # First and second person pronoun counts
        features['FirstPersonPronounCount'] = sum(1 for w in words if w in self.first_person_pronouns)
        features['FirstPersonPronounPercentage'] = (features['FirstPersonPronounCount'] / len(words)) * 100 if words else 0
        features['SecondPersonPronounCount'] = sum(1 for w in words if w in self.second_person_pronouns)
        features['SecondPersonPronounPercentage'] = (features['SecondPersonPronounCount'] / len(words)) * 100 if words else 0

        # TextBlob sentiment
        blob = TextBlob(text)
        features['Polarity'] = blob.sentiment.polarity
        features['Subjectivity'] = blob.sentiment.subjectivity
        

        
        return features
    
    def _count_syllables(self, word):
        """Count syllables in a word using pyphen"""
        hyphenated = self.pyphen_dic.inserted(word)
        return max(1, hyphenated.count('-') + 1)
    
    def _extract_readability_features(self, text, words, sentences):
        """Extract readability features"""
        features = {}
        
        words_no_punct = [w for w in words if w not in string.punctuation]
        
        # Calculate syllables
        total_syllables = sum(self._count_syllables(word) for word in words_no_punct)
        complex_words = sum(1 for word in words_no_punct if self._count_syllables(word) >= 3)
        features['TotalSyllables'] = total_syllables
        features['AverageSyllablesPerWord'] = total_syllables / len(words_no_punct) if words_no_punct else 0
        features['ComplexWordCount'] = complex_words
        features['ComplexWordPercentage'] = (complex_words / len(words_no_punct)) * 100 if words_no_punct else 0
        
        # Flesch Reading Ease
        if sentences and words_no_punct:
            features['FleschReadingEase'] = (206.835 
                                             - 1.015 * (len(words_no_punct) / len(sentences))
                                             - 84.6 * (total_syllables / len(words_no_punct)))
            
            features['GunningFog'] = 0.4 * ((len(words_no_punct) / len(sentences)) 
                                            + 100 * (complex_words / len(words_no_punct)))
        else:
            features['FleschReadingEase'] = 0
            features['GunningFog'] = 0

        return features
    
    
    def _extract_uniqueness_features(self, words):
        """Extract uniqueness features"""
        features = {}
        words_no_punct = [w for w in words if w not in string.punctuation]
        # Bigram uniqueness
        bigrams = list(zip(words_no_punct[:-1], words_no_punct[1:]))
        features['BigramUniqueness'] = len(set(bigrams)) / len(bigrams) if bigrams else 0
        # Trigram uniqueness
        trigrams = list(zip(words_no_punct[:-2], words_no_punct[1:-1], words_no_punct[2:]))
        features['TrigramUniqueness'] = len(set(trigrams)) / len(trigrams) if trigrams else 0
        return features
    
    def _extract_all_overlap_features(self, text, context_text):
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