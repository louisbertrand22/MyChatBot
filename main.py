"""
Main entry point for the Simple Chatbot application
"""

from bot import ChatBot


def main():
    """
    Main function to start the chatbot
    """
    print("Démarrage du chatbot...")
    print()
    
    # Create and start the chatbot
    chatbot = ChatBot()
    chatbot.chat()


if __name__ == "__main__":
    main()
