"""
Main entry point for the Simple Chatbot application
"""

import sys
from bot import ChatBot


def main():
    """
    Main function to start the chatbot.
    
    Command line arguments:
        --nlp: Enable NLP features
        --nlp-info: Enable NLP features with detailed analysis display
    """
    print("Démarrage du chatbot...")
    print()
    
    # Check for NLP mode
    use_nlp = '--nlp' in sys.argv or '--nlp-info' in sys.argv
    show_nlp_info = '--nlp-info' in sys.argv
    
    # Create and start the chatbot
    chatbot = ChatBot(use_nlp=use_nlp)
    chatbot.chat(show_nlp_info=show_nlp_info)


if __name__ == "__main__":
    main()
