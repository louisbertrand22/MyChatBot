"""
NLP Utilities Module
Provides NLP capabilities using NLTK, spaCy, and transformers.
"""

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import spacy
from transformers import pipeline
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')


class NLPProcessor:
    """
    NLP Processor class that integrates NLTK, spaCy, and transformers
    for advanced text processing capabilities.
    """
    
    def __init__(self):
        """
        Initialize NLP tools and download required resources.
        """
        self._download_nltk_resources()
        self.lemmatizer = WordNetLemmatizer()
        self.nlp_spacy = None
        self.sentiment_analyzer = None
        self._initialize_spacy()
        self._initialize_sentiment_analyzer()
    
    def _download_nltk_resources(self):
        """
        Download necessary NLTK resources.
        """
        resources = ['punkt', 'stopwords', 'wordnet', 'averaged_perceptron_tagger', 'punkt_tab']
        for resource in resources:
            try:
                nltk.data.find(f'tokenizers/{resource}')
            except LookupError:
                try:
                    nltk.download(resource, quiet=True)
                except:
                    pass
    
    def _initialize_spacy(self):
        """
        Initialize spaCy model. Loads a small English model if available.
        """
        try:
            self.nlp_spacy = spacy.load('en_core_web_sm')
        except OSError:
            print("Note: spaCy model 'en_core_web_sm' not found.")
            print("To use spaCy features, install it with: python -m spacy download en_core_web_sm")
            self.nlp_spacy = None
    
    def _initialize_sentiment_analyzer(self):
        """
        Initialize sentiment analysis pipeline using transformers.
        """
        try:
            self.sentiment_analyzer = pipeline(
                "sentiment-analysis",
                model="distilbert-base-uncased-finetuned-sst-2-english"
            )
        except Exception as e:
            print(f"Note: Could not load sentiment analyzer: {e}")
            print("Sentiment analysis features will be disabled.")
            self.sentiment_analyzer = None
    
    def tokenize(self, text):
        """
        Tokenize text using NLTK.
        
        Args:
            text (str): Input text
            
        Returns:
            list: List of tokens
        """
        try:
            return word_tokenize(text.lower())
        except:
            # Fallback to simple split if NLTK fails
            return text.lower().split()
    
    def remove_stopwords(self, tokens, language='english'):
        """
        Remove stopwords from tokens.
        
        Args:
            tokens (list): List of tokens
            language (str): Language for stopwords
            
        Returns:
            list: Tokens without stopwords
        """
        try:
            stop_words = set(stopwords.words(language))
            return [token for token in tokens if token not in stop_words]
        except:
            # If stopwords not available, return original tokens
            return tokens
    
    def lemmatize(self, tokens):
        """
        Lemmatize tokens using NLTK WordNet Lemmatizer.
        
        Args:
            tokens (list): List of tokens
            
        Returns:
            list: Lemmatized tokens
        """
        return [self.lemmatizer.lemmatize(token) for token in tokens]
    
    def preprocess_text(self, text, remove_stopwords=True, lemmatize=True):
        """
        Complete preprocessing pipeline: tokenization, stopword removal, lemmatization.
        
        Args:
            text (str): Input text
            remove_stopwords (bool): Whether to remove stopwords
            lemmatize (bool): Whether to lemmatize tokens
            
        Returns:
            list: Preprocessed tokens
        """
        tokens = self.tokenize(text)
        
        if remove_stopwords:
            tokens = self.remove_stopwords(tokens)
        
        if lemmatize:
            tokens = self.lemmatize(tokens)
        
        return tokens
    
    def extract_entities(self, text):
        """
        Extract named entities using spaCy.
        
        Args:
            text (str): Input text
            
        Returns:
            list: List of tuples (entity_text, entity_label)
        """
        if self.nlp_spacy is None:
            return []
        
        try:
            doc = self.nlp_spacy(text)
            return [(ent.text, ent.label_) for ent in doc.ents]
        except Exception as e:
            print(f"Error extracting entities: {e}")
            return []
    
    def analyze_sentiment(self, text):
        """
        Analyze sentiment of text using transformers.
        
        Args:
            text (str): Input text
            
        Returns:
            dict: Sentiment analysis result with 'label' and 'score'
        """
        if self.sentiment_analyzer is None:
            return {'label': 'UNKNOWN', 'score': 0.0}
        
        try:
            # Truncate text if too long
            max_length = 512
            if len(text) > max_length:
                text = text[:max_length]
            
            result = self.sentiment_analyzer(text)[0]
            return result
        except Exception as e:
            print(f"Error analyzing sentiment: {e}")
            return {'label': 'UNKNOWN', 'score': 0.0}
    
    def get_pos_tags(self, text):
        """
        Get part-of-speech tags using NLTK.
        
        Args:
            text (str): Input text
            
        Returns:
            list: List of tuples (word, pos_tag)
        """
        try:
            tokens = word_tokenize(text)
            return nltk.pos_tag(tokens)
        except:
            return []
    
    def compute_similarity(self, text1, text2):
        """
        Compute semantic similarity between two texts using spaCy.
        
        Args:
            text1 (str): First text
            text2 (str): Second text
            
        Returns:
            float: Similarity score (0-1) or None if spaCy unavailable
        """
        if self.nlp_spacy is None:
            return None
        
        try:
            doc1 = self.nlp_spacy(text1)
            doc2 = self.nlp_spacy(text2)
            return doc1.similarity(doc2)
        except Exception as e:
            print(f"Error computing similarity: {e}")
            return None


# Singleton instance for easy access
_nlp_processor = None


def get_nlp_processor():
    """
    Get or create the singleton NLP processor instance.
    
    Returns:
        NLPProcessor: The NLP processor instance
    """
    global _nlp_processor
    if _nlp_processor is None:
        _nlp_processor = NLPProcessor()
    return _nlp_processor
