"""
Chatbot Logic Module
Handles the conversation logic and response generation based on patterns.
"""

import json
import random
import os


class ChatBot:
    """Simple rule-based chatbot"""
    
    def __init__(self, faq_file='data/faq.json'):
        """
        Initialize the chatbot with FAQ data
        
        Args:
            faq_file (str): Path to the FAQ JSON file
        """
        self.faq_file = faq_file
        self.knowledge_base = self.load_knowledge_base()
        
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
        Find the intent of user input by matching patterns
        
        Args:
            user_input (str): User's message
            
        Returns:
            str: Intent key or 'default' if no match found
        """
        user_input = user_input.lower().strip()
        
        for intent, data in self.knowledge_base.items():
            if intent == 'default':
                continue
            
            patterns = data.get('patterns', [])
            for pattern in patterns:
                if pattern.lower() in user_input:
                    return intent
        
        return 'default'
    
    def get_response(self, user_input):
        """
        Generate a response based on user input
        
        Args:
            user_input (str): User's message
            
        Returns:
            str: Bot's response
        """
        if not user_input.strip():
            return "Je n'ai rien reçu. Pouvez-vous répéter ?"
        
        intent = self.find_intent(user_input)
        
        if intent in self.knowledge_base:
            responses = self.knowledge_base[intent].get('responses', [])
            if responses:
                return random.choice(responses)
        
        # Fallback to default response
        default_responses = self.knowledge_base.get('default', {}).get('responses', [])
        if default_responses:
            return random.choice(default_responses)
        
        return "Je ne sais pas comment répondre à cela."
    
    def chat(self):
        """
        Start an interactive chat session
        """
        print("=" * 50)
        print("Chatbot Simple - Tapez 'quit' ou 'exit' pour quitter")
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
                
                response = self.get_response(user_input)
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
