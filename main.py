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
        --gpt: Enable GPT text generation
    """
    print("Démarrage du chatbot...")
    print()
    
    # Check for NLP mode
    use_nlp = '--nlp' in sys.argv or '--nlp-info' in sys.argv
    show_nlp_info = '--nlp-info' in sys.argv
    
    # Check for GPT mode
    use_gpt = '--gpt' in sys.argv
    
    # Create and start the chatbot
    chatbot = ChatBot(use_nlp=use_nlp, use_gpt=use_gpt)
    chatbot.chat(show_nlp_info=show_nlp_info, use_generation=use_gpt)


if __name__ == "__main__":
    main()
