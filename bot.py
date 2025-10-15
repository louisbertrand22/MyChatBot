"""
Chatbot Logic Module
Handles the conversation logic and response generation based on patterns.
Enhanced with NLP capabilities using NLTK, spaCy, and transformers.
"""

import json
import random
import os


class ChatBot:
    """Simple rule-based chatbot enhanced with NLP capabilities"""
    
    def __init__(self, faq_file='data/faq.json', use_nlp=False):
        """
        Initialize the chatbot with FAQ data
        
        Args:
            faq_file (str): Path to the FAQ JSON file
            use_nlp (bool): Whether to use NLP features (requires dependencies)
        """
        self.faq_file = faq_file
        self.knowledge_base = self.load_knowledge_base()
        self.use_nlp = use_nlp
        self.nlp_processor = None
        
        if self.use_nlp:
            try:
                from nlp_utils import get_nlp_processor
                self.nlp_processor = get_nlp_processor()
                print("NLP features activated!")
            except ImportError:
                print("Warning: NLP dependencies not installed. Install with: pip install -r requirements.txt")
                self.use_nlp = False
            except Exception as e:
                print(f"Warning: Could not initialize NLP features: {e}")
                self.use_nlp = False
        
    def load_knowledge_base(self):
        """
        Load the knowledge base from JSON file
        
        Returns:
            dict: Knowledge base with patterns and responses
        """
        try:
            with open(self.faq_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Error: Could not find {self.faq_file}")
            return {}
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON in {self.faq_file}")
            return {}
    
    def find_intent(self, user_input):
        """
        Find the intent of user input by matching patterns.
        Uses NLP-enhanced matching if enabled.
        
        Args:
            user_input (str): User's message
            
        Returns:
            str: Intent key or 'default' if no match found
        """
        user_input = user_input.lower().strip()
        
        # Try NLP-enhanced matching first if available
        if self.use_nlp and self.nlp_processor:
            nlp_intent = self._find_intent_nlp(user_input)
            if nlp_intent != 'default':
                return nlp_intent
        
        # Fallback to simple pattern matching
        for intent, data in self.knowledge_base.items():
            if intent == 'default':
                continue
            
            patterns = data.get('patterns', [])
            for pattern in patterns:
                if pattern.lower() in user_input:
                    return intent
        
        return 'default'
    
    def _find_intent_nlp(self, user_input):
        """
        Find intent using NLP-enhanced matching with lemmatization.
        
        Args:
            user_input (str): User's message
            
        Returns:
            str: Intent key or 'default' if no match found
        """
        # Preprocess user input
        user_tokens = self.nlp_processor.preprocess_text(user_input, remove_stopwords=False)
        user_text_processed = ' '.join(user_tokens)
        
        best_match = 'default'
        best_score = 0
        
        for intent, data in self.knowledge_base.items():
            if intent == 'default':
                continue
            
            patterns = data.get('patterns', [])
            for pattern in patterns:
                # Preprocess pattern
                pattern_tokens = self.nlp_processor.preprocess_text(pattern, remove_stopwords=False)
                pattern_text_processed = ' '.join(pattern_tokens)
                
                # Check if pattern tokens are in user tokens
                if pattern_text_processed in user_text_processed:
                    return intent
                
                # Try similarity matching if spaCy is available
                similarity = self.nlp_processor.compute_similarity(user_input, pattern)
                if similarity and similarity > best_score and similarity > 0.7:
                    best_score = similarity
                    best_match = intent
        
        return best_match
    
    def get_response(self, user_input, include_nlp_info=False):
        """
        Generate a response based on user input.
        Optionally includes NLP analysis information.
        
        Args:
            user_input (str): User's message
            include_nlp_info (bool): Whether to include NLP analysis in response
            
        Returns:
            str: Bot's response (with optional NLP info)
        """
        if not user_input.strip():
            return "Je n'ai rien reçu. Pouvez-vous répéter ?"
        
        # Get NLP analysis if enabled
        nlp_info = ""
        if self.use_nlp and self.nlp_processor and include_nlp_info:
            nlp_info = self._get_nlp_analysis(user_input)
        
        intent = self.find_intent(user_input)
        
        if intent in self.knowledge_base:
            responses = self.knowledge_base[intent].get('responses', [])
            if responses:
                response = random.choice(responses)
                return response + nlp_info if nlp_info else response
        
        # Fallback to default response
        default_responses = self.knowledge_base.get('default', {}).get('responses', [])
        if default_responses:
            response = random.choice(default_responses)
            return response + nlp_info if nlp_info else response
        
        return "Je ne sais pas comment répondre à cela."
    
    def _get_nlp_analysis(self, text):
        """
        Get NLP analysis of the input text.
        
        Args:
            text (str): Input text
            
        Returns:
            str: Formatted NLP analysis
        """
        analysis = "\n\n--- Analyse NLP ---"
        
        # Sentiment analysis
        sentiment = self.nlp_processor.analyze_sentiment(text)
        if sentiment['label'] != 'UNKNOWN':
            sentiment_fr = "Positif" if sentiment['label'] == 'POSITIVE' else "Négatif"
            analysis += f"\nSentiment: {sentiment_fr} ({sentiment['score']:.2f})"
        
        # Entity extraction
        entities = self.nlp_processor.extract_entities(text)
        if entities:
            analysis += "\nEntités détectées: " + ", ".join([f"{ent[0]} ({ent[1]})" for ent in entities])
        
        # Tokens
        tokens = self.nlp_processor.preprocess_text(text)
        if tokens:
            analysis += f"\nMots-clés: {', '.join(tokens[:5])}"
        
        return analysis
    
    def chat(self, show_nlp_info=False):
        """
        Start an interactive chat session
        
        Args:
            show_nlp_info (bool): Whether to display NLP analysis with responses
        """
        print("=" * 50)
        print("Chatbot Simple - Tapez 'quit' ou 'exit' pour quitter")
        if self.use_nlp:
            print("Mode NLP activé!")
            if show_nlp_info:
                print("(Affichage de l'analyse NLP activé)")
        print("=" * 50)
        print()
        
        while True:
            try:
                user_input = input("Vous: ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() in ['quit', 'exit', 'quitter']:
                    print("Bot: Au revoir ! À bientôt !")
                    break
                
                response = self.get_response(user_input, include_nlp_info=show_nlp_info)
                print(f"Bot: {response}")
                print()
                
            except KeyboardInterrupt:
                print("\nBot: Au revoir ! À bientôt !")
                break
            except Exception as e:
                print(f"Erreur: {e}")
                break


if __name__ == "__main__":
    bot = ChatBot()
    bot.chat()
