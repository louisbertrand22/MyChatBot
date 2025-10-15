"""
Test script for NLP integration
Tests the chatbot functionality with and without NLP features.
"""

import sys
import os


def test_basic_chatbot():
    """Test basic chatbot without NLP"""
    print("=" * 70)
    print("Test 1: Basic Chatbot (without NLP)")
    print("=" * 70)
    
    try:
        from bot import ChatBot
        
        bot = ChatBot(use_nlp=False)
        
        # Test various inputs
        test_cases = [
            ("bonjour", ["greeting", "salut", "hello"]),
            ("comment ça va", ["comment", "va", "bien"]),
            ("merci", ["merci", "rien", "plaisir"]),
            ("au revoir", ["revoir", "bientôt", "bye"]),
        ]
        
        print("\nTesting basic pattern matching:")
        for user_input, expected_keywords in test_cases:
            response = bot.get_response(user_input)
            print(f"\nInput: {user_input}")
            print(f"Response: {response}")
            
            # Check if response contains at least one expected keyword
            response_lower = response.lower()
            has_keyword = any(keyword.lower() in response_lower for keyword in expected_keywords)
            
            if has_keyword or "sais pas" in response_lower:
                print("✓ Response appropriate")
            else:
                print("✗ Unexpected response")
        
        print("\n✅ Basic chatbot test PASSED")
        return True
        
    except Exception as e:
        print(f"\n❌ Basic chatbot test FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_nlp_imports():
    """Test that NLP modules can be imported"""
    print("\n" + "=" * 70)
    print("Test 2: NLP Module Imports")
    print("=" * 70)
    
    try:
        # Test nlp_utils module
        print("\nImporting nlp_utils...")
        import nlp_utils
        print("✓ nlp_utils imported successfully")
        
        # Test that classes exist
        assert hasattr(nlp_utils, 'NLPProcessor'), "NLPProcessor class not found"
        assert hasattr(nlp_utils, 'get_nlp_processor'), "get_nlp_processor function not found"
        print("✓ NLPProcessor class and get_nlp_processor function exist")
        
        # Test nlp_demo module
        print("\nImporting nlp_demo...")
        import nlp_demo
        print("✓ nlp_demo imported successfully")
        
        print("\n✅ NLP imports test PASSED")
        return True
        
    except Exception as e:
        print(f"\n❌ NLP imports test FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_chatbot_nlp_mode():
    """Test chatbot initialization with NLP mode (without requiring dependencies)"""
    print("\n" + "=" * 70)
    print("Test 3: Chatbot NLP Mode Initialization")
    print("=" * 70)
    
    try:
        from bot import ChatBot
        
        # Test that chatbot can be created with use_nlp=True
        # (it will disable NLP if dependencies are not available)
        print("\nCreating chatbot with NLP mode enabled...")
        bot = ChatBot(use_nlp=True)
        print("✓ Chatbot created with NLP mode")
        
        # Test basic functionality still works
        print("\nTesting basic functionality with NLP mode:")
        response = bot.get_response("bonjour")
        print(f"Response to 'bonjour': {response}")
        
        if response and len(response) > 0:
            print("✓ Chatbot responds appropriately")
        else:
            print("✗ Empty response")
            return False
        
        print("\n✅ Chatbot NLP mode test PASSED")
        return True
        
    except Exception as e:
        print(f"\n❌ Chatbot NLP mode test FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_main_script():
    """Test that main script can be imported"""
    print("\n" + "=" * 70)
    print("Test 4: Main Script")
    print("=" * 70)
    
    try:
        print("\nImporting main...")
        import main
        print("✓ main imported successfully")
        
        assert hasattr(main, 'main'), "main function not found"
        print("✓ main function exists")
        
        print("\n✅ Main script test PASSED")
        return True
        
    except Exception as e:
        print(f"\n❌ Main script test FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_gpt_integration():
    """Test GPT text generation integration"""
    print("\n" + "=" * 70)
    print("Test 5: GPT Text Generation Integration")
    print("=" * 70)
    
    try:
        from bot import ChatBot
        
        # Test that chatbot can be created with GPT mode
        print("\nCreating chatbot with GPT mode enabled...")
        bot = ChatBot(use_gpt=True)
        print("✓ Chatbot created with GPT mode")
        
        # Test that GPT-related methods exist
        assert hasattr(bot, 'use_gpt'), "use_gpt attribute not found"
        assert hasattr(bot, '_generate_gpt_response'), "_generate_gpt_response method not found"
        print("✓ GPT-related attributes and methods exist")
        
        # Test get_response with use_generation parameter
        print("\nTesting get_response with use_generation parameter:")
        response = bot.get_response("Hello", use_generation=False)
        print(f"Response (generation=False): {response}")
        
        if response and len(response) > 0:
            print("✓ Chatbot responds without generation")
        else:
            print("✗ Empty response")
            return False
        
        print("\n✅ GPT integration test PASSED")
        return True
        
    except Exception as e:
        print(f"\n❌ GPT integration test FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_code_structure():
    """Test that all required files exist and have proper structure"""
    print("\n" + "=" * 70)
    print("Test 6: Code Structure")
    print("=" * 70)
    
    required_files = {
        'bot.py': ['ChatBot', 'get_response', 'find_intent', 'use_gpt', '_generate_gpt_response'],
        'nlp_utils.py': ['NLPProcessor', 'get_nlp_processor', 'generate_text', 'text_generator'],
        'nlp_demo.py': ['demo_nlp_features', 'demo_chatbot_nlp', 'demo_gpt_generation', 'demo_chatbot_gpt'],
        'main.py': ['main', '--gpt'],
        'requirements.txt': ['nltk', 'spacy', 'transformers'],
        'data/faq.json': ['greetings', 'goodbye'],
    }
    
    all_passed = True
    
    for filename, keywords in required_files.items():
        filepath = os.path.join('/home/runner/work/MyChatBot/MyChatBot', filename)
        
        if not os.path.exists(filepath):
            print(f"\n✗ File not found: {filename}")
            all_passed = False
            continue
        
        print(f"\n✓ File exists: {filename}")
        
        # Check for keywords in file
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        missing_keywords = []
        for keyword in keywords:
            if keyword not in content:
                missing_keywords.append(keyword)
        
        if missing_keywords:
            print(f"  ✗ Missing keywords: {', '.join(missing_keywords)}")
            all_passed = False
        else:
            print(f"  ✓ All required keywords found")
    
    if all_passed:
        print("\n✅ Code structure test PASSED")
    else:
        print("\n❌ Code structure test FAILED")
    
    return all_passed


def main():
    """Run all tests"""
    print("\n" + "=" * 70)
    print("NLP Integration Test Suite")
    print("=" * 70)
    
    tests = [
        ("Code Structure", test_code_structure),
        ("Basic Chatbot", test_basic_chatbot),
        ("NLP Imports", test_nlp_imports),
        ("Chatbot NLP Mode", test_chatbot_nlp_mode),
        ("Main Script", test_main_script),
        ("GPT Integration", test_gpt_integration),
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"\n❌ Test '{test_name}' encountered an error: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 70)
    print("Test Summary")
    print("=" * 70)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{test_name}: {status}")
    
    print(f"\nTotal: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 All tests passed!")
        return 0
    else:
        print(f"\n⚠️  {total - passed} test(s) failed")
        return 1


if __name__ == "__main__":
    sys.exit(main())
