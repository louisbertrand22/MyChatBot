"""
GPT Text Generation Example
This script demonstrates how to use GPT-2 text generation in the chatbot.
"""

def example_basic_generation():
    """
    Example 1: Basic text generation with GPT-2
    """
    print("=" * 70)
    print("Example 1: Basic GPT-2 Text Generation")
    print("=" * 70)
    print()
    
    try:
        from nlp_utils import get_nlp_processor
        
        nlp = get_nlp_processor()
        
        if not nlp.text_generator:
            print("❌ GPT text generation is not available.")
            print("Please install dependencies: pip install -r requirements.txt")
            return
        
        print("✓ GPT-2 model loaded successfully!\n")
        
        # Example prompts
        prompts = [
            "The future of artificial intelligence is",
            "A chatbot can help users by",
            "Once upon a time in a digital world",
        ]
        
        for prompt in prompts:
            print(f"Prompt: '{prompt}'")
            print("-" * 70)
            
            # Generate text
            generated_texts = nlp.generate_text(
                prompt,
                max_length=50,
                num_return_sequences=1,
                temperature=0.7
            )
            
            if generated_texts:
                print(f"Generated: {generated_texts[0]}")
            else:
                print("No text generated")
            print()
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()


def example_chatbot_with_gpt():
    """
    Example 2: Using chatbot with GPT generation mode
    """
    print("\n" + "=" * 70)
    print("Example 2: Chatbot with GPT Generation")
    print("=" * 70)
    print()
    
    try:
        from bot import ChatBot
        
        # Create chatbot with GPT enabled
        print("Creating chatbot with GPT mode...")
        bot = ChatBot(use_gpt=True)
        
        if not bot.use_gpt:
            print("❌ GPT mode is not available.")
            print("Please install dependencies: pip install -r requirements.txt")
            return
        
        print("✓ Chatbot created with GPT mode!\n")
        
        # Test with predefined responses (default mode)
        print("Mode 1: Predefined Responses")
        print("-" * 70)
        test_input = "Hello, how are you?"
        print(f"User: {test_input}")
        response = bot.get_response(test_input, use_generation=False)
        print(f"Bot: {response}\n")
        
        # Test with GPT generation
        print("Mode 2: GPT Generation")
        print("-" * 70)
        test_input = "Tell me about the weather"
        print(f"User: {test_input}")
        response = bot.get_response(test_input, use_generation=True)
        print(f"Bot: {response}\n")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()


def example_advanced_generation():
    """
    Example 3: Advanced text generation with different parameters
    """
    print("\n" + "=" * 70)
    print("Example 3: Advanced GPT Generation Parameters")
    print("=" * 70)
    print()
    
    try:
        from nlp_utils import get_nlp_processor
        
        nlp = get_nlp_processor()
        
        if not nlp.text_generator:
            print("❌ GPT text generation is not available.")
            return
        
        prompt = "In the world of technology"
        print(f"Prompt: '{prompt}'\n")
        
        # Different temperature values
        temperatures = [0.3, 0.7, 1.0]
        
        for temp in temperatures:
            print(f"Temperature: {temp} ({'low=focused' if temp < 0.5 else 'medium=balanced' if temp < 0.9 else 'high=creative'})")
            print("-" * 70)
            
            generated = nlp.generate_text(
                prompt,
                max_length=40,
                num_return_sequences=1,
                temperature=temp
            )
            
            if generated:
                print(f"{generated[0]}\n")
        
    except Exception as e:
        print(f"❌ Error: {e}")


def main():
    """
    Run all examples
    """
    print("\n" + "=" * 70)
    print("GPT-2 Text Generation Examples for MyChatBot")
    print("=" * 70)
    print("\nThis script demonstrates how to use GPT-2 for text generation.")
    print("Make sure you have installed: pip install -r requirements.txt\n")
    
    example_basic_generation()
    example_chatbot_with_gpt()
    example_advanced_generation()
    
    print("\n" + "=" * 70)
    print("Examples Complete!")
    print("=" * 70)
    print("\nTo use GPT generation interactively, run:")
    print("  python main.py --gpt")
    print("\nFor more examples, run:")
    print("  python nlp_demo.py --gpt")
    print("  python nlp_demo.py --chatbot-gpt")
    print("=" * 70)


if __name__ == "__main__":
    main()
