"""
NLP Features Demonstration Script
Demonstrates the various NLP capabilities of the chatbot.
"""

import sys


def demo_nlp_features():
    """
    Demonstrate all NLP features including:
    - NLTK: Tokenization, lemmatization, stopword removal, POS tagging
    - spaCy: Named Entity Recognition, similarity
    - Transformers: Sentiment analysis
    """
    print("=" * 70)
    print("NLP Features Demonstration for MyChatBot")
    print("=" * 70)
    print()
    
    try:
        from nlp_utils import get_nlp_processor
        nlp = get_nlp_processor()
    except ImportError as e:
        print("Error: NLP dependencies not installed.")
        print("Please install them with: pip install -r requirements.txt")
        print(f"Details: {e}")
        return
    except Exception as e:
        print(f"Error initializing NLP processor: {e}")
        return
    
    # Example texts
    texts = [
        "Hello! My name is John and I live in New York. I love programming with Python!",
        "I'm feeling great today! The weather is beautiful and sunny.",
        "I'm disappointed with the service. This is terrible.",
        "What is the capital of France? I think it's Paris.",
        "Apple Inc. is a technology company founded by Steve Jobs in California."
    ]
    
    for i, text in enumerate(texts, 1):
        print(f"\n{'=' * 70}")
        print(f"Example {i}: {text}")
        print(f"{'=' * 70}")
        
        # 1. NLTK: Tokenization
        print("\n[NLTK] Tokenization:")
        tokens = nlp.tokenize(text)
        print(f"  Tokens: {tokens[:10]}...")  # Show first 10 tokens
        
        # 2. NLTK: Stopword Removal
        print("\n[NLTK] After Stopword Removal:")
        tokens_no_stop = nlp.remove_stopwords(tokens)
        print(f"  Tokens: {tokens_no_stop[:10]}...")
        
        # 3. NLTK: Lemmatization
        print("\n[NLTK] Lemmatization:")
        lemmatized = nlp.lemmatize(tokens_no_stop)
        print(f"  Lemmas: {lemmatized[:10]}...")
        
        # 4. NLTK: Complete Preprocessing
        print("\n[NLTK] Complete Preprocessing:")
        processed = nlp.preprocess_text(text)
        print(f"  Processed: {processed}")
        
        # 5. NLTK: POS Tagging
        print("\n[NLTK] Part-of-Speech Tagging:")
        pos_tags = nlp.get_pos_tags(text)
        print(f"  POS Tags: {pos_tags[:5]}...")  # Show first 5
        
        # 6. spaCy: Named Entity Recognition
        print("\n[spaCy] Named Entity Recognition:")
        entities = nlp.extract_entities(text)
        if entities:
            for entity_text, entity_label in entities:
                print(f"  - {entity_text}: {entity_label}")
        else:
            print("  No entities detected" + (" (spaCy not available)" if not nlp.nlp_spacy else ""))
        
        # 7. Transformers: Sentiment Analysis
        print("\n[Transformers] Sentiment Analysis:")
        sentiment = nlp.analyze_sentiment(text)
        if sentiment['label'] != 'UNKNOWN':
            print(f"  Sentiment: {sentiment['label']}")
            print(f"  Confidence: {sentiment['score']:.4f}")
        else:
            print("  Sentiment analysis not available")
    
    # 8. spaCy: Similarity
    print(f"\n{'=' * 70}")
    print("Semantic Similarity Demonstration (spaCy)")
    print(f"{'=' * 70}")
    
    similarity_pairs = [
        ("I love programming", "I enjoy coding"),
        ("The cat is sleeping", "The dog is running"),
        ("Paris is beautiful", "The capital of France is nice"),
    ]
    
    for text1, text2 in similarity_pairs:
        similarity = nlp.compute_similarity(text1, text2)
        if similarity is not None:
            print(f"\nText 1: {text1}")
            print(f"Text 2: {text2}")
            print(f"Similarity Score: {similarity:.4f}")
        else:
            print("\nSimilarity calculation not available (spaCy not loaded)")
            break


def demo_chatbot_nlp():
    """
    Demonstrate the chatbot with NLP features enabled.
    """
    print("\n" + "=" * 70)
    print("Chatbot with NLP Features Demonstration")
    print("=" * 70)
    print()
    
    try:
        from bot import ChatBot
        
        # Create chatbot with NLP enabled
        bot = ChatBot(use_nlp=True)
        
        # Test messages
        test_messages = [
            "Hello, how are you today?",
            "What is your name?",
            "Thank you so much for your help!",
            "I'm feeling great today!",
            "Goodbye, see you later!"
        ]
        
        print("Testing chatbot responses with NLP analysis:\n")
        
        for msg in test_messages:
            print(f"User: {msg}")
            response = bot.get_response(msg, include_nlp_info=True)
            print(f"Bot: {response}")
            print()
        
    except ImportError as e:
        print("Error: Could not import chatbot or NLP dependencies.")
        print(f"Details: {e}")
    except Exception as e:
        print(f"Error: {e}")


def demo_gpt_generation():
    """
    Demonstrate GPT-2 text generation capabilities.
    """
    print("\n" + "=" * 70)
    print("GPT-2 Text Generation Demonstration")
    print("=" * 70)
    print()
    
    try:
        from nlp_utils import get_nlp_processor
        nlp = get_nlp_processor()
        
        if not nlp.text_generator:
            print("GPT text generation not available.")
            print("Make sure transformers and torch are installed.")
            return
        
        print("Demonstrating text generation with various prompts:\n")
        
        # Test prompts
        prompts = [
            "Once upon a time",
            "The future of artificial intelligence is",
            "In the world of technology",
            "A chatbot can help users by"
        ]
        
        for prompt in prompts:
            print(f"{'=' * 70}")
            print(f"Prompt: {prompt}")
            print(f"{'=' * 70}")
            
            # Generate multiple variations
            generated = nlp.generate_text(
                prompt,
                max_length=50,
                num_return_sequences=2,
                temperature=0.8
            )
            
            for i, text in enumerate(generated, 1):
                print(f"\nGeneration {i}:")
                print(f"  {text}")
            print()
    
    except ImportError as e:
        print("Error: NLP dependencies not installed.")
        print(f"Details: {e}")
    except Exception as e:
        print(f"Error: {e}")


def demo_chatbot_gpt():
    """
    Demonstrate the chatbot with GPT text generation enabled.
    """
    print("\n" + "=" * 70)
    print("Chatbot with GPT Text Generation Demonstration")
    print("=" * 70)
    print()
    
    try:
        from bot import ChatBot
        
        # Create chatbot with GPT enabled
        bot = ChatBot(use_gpt=True)
        
        if not bot.use_gpt:
            print("GPT mode could not be enabled.")
            print("Make sure transformers and torch are installed.")
            return
        
        # Test messages
        test_messages = [
            "Tell me about artificial intelligence",
            "What do you think about the weather",
            "Can you help me with programming"
        ]
        
        print("Testing chatbot with GPT generation:\n")
        
        for msg in test_messages:
            print(f"User: {msg}")
            response = bot.get_response(msg, use_generation=True)
            print(f"Bot: {response}")
            print()
        
    except ImportError as e:
        print("Error: Could not import chatbot or NLP dependencies.")
        print(f"Details: {e}")
    except Exception as e:
        print(f"Error: {e}")


def main():
    """
    Main function to run demonstrations.
    """
    print("\nNLP Integration Demonstration for MyChatBot")
    print("This script demonstrates NLTK, spaCy, and transformers integration.\n")
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "--chatbot":
            demo_chatbot_nlp()
        elif sys.argv[1] == "--gpt":
            demo_gpt_generation()
        elif sys.argv[1] == "--chatbot-gpt":
            demo_chatbot_gpt()
        else:
            print(f"Unknown option: {sys.argv[1]}")
            print("\nAvailable options:")
            print("  (no option)      - Show all NLP features")
            print("  --chatbot        - Demo chatbot with NLP")
            print("  --gpt            - Demo GPT text generation")
            print("  --chatbot-gpt    - Demo chatbot with GPT generation")
    else:
        demo_nlp_features()
        print("\n" + "=" * 70)
        print("\nTo see more demonstrations, run:")
        print("  python nlp_demo.py --chatbot      (Chatbot with NLP)")
        print("  python nlp_demo.py --gpt          (GPT text generation)")
        print("  python nlp_demo.py --chatbot-gpt  (Chatbot with GPT)")
        print("\nOr start an interactive session:")
        print("  python main.py --nlp              (Interactive NLP mode)")
        print("  python main.py --gpt              (Interactive GPT mode)")
        print("=" * 70)


if __name__ == "__main__":
    main()
