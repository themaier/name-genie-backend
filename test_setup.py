"""
Test script for the Keyword Generator AI
Run this to verify your setup is working correctly
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

print("=" * 60)
print("Keyword Generator AI - Setup Test")
print("=" * 60)

# Check Python imports
print("\n1. Checking Python packages...")
try:
    import fastapi
    print("   ✅ FastAPI installed")
except ImportError:
    print("   ❌ FastAPI not installed - run: pip install fastapi")

try:
    import uvicorn
    print("   ✅ Uvicorn installed")
except ImportError:
    print("   ❌ Uvicorn not installed - run: pip install uvicorn")

try:
    import crewai
    print("   ✅ CrewAI installed")
except ImportError:
    print("   ❌ CrewAI not installed - run: pip install crewai")

try:
    from langchain_openai import ChatOpenAI
    print("   ✅ LangChain OpenAI installed")
except ImportError:
    print("   ❌ LangChain OpenAI not installed - run: pip install langchain-openai")

try:
    from crewai_tools import SerperDevTool
    print("   ✅ CrewAI Tools installed")
except ImportError:
    print("   ❌ CrewAI Tools not installed - run: pip install crewai-tools")

# Check environment variables
print("\n2. Checking environment variables...")
openai_key = os.getenv("OPENAI_API_KEY")
if openai_key and openai_key != "your_openai_api_key_here":
    print(f"   ✅ OPENAI_API_KEY is set ({openai_key[:8]}...)")
else:
    print("   ❌ OPENAI_API_KEY not set in .env file")

serper_key = os.getenv("SERPER_API_KEY")
if serper_key and serper_key != "your_serper_api_key_here":
    print(f"   ✅ SERPER_API_KEY is set ({serper_key[:8]}...)")
else:
    print("   ⚠️  SERPER_API_KEY not set (web search will be disabled)")

# Test creativity tool
print("\n3. Testing Creativity Tool...")
try:
    from tools import creativity_tool
    
    test_topic = "cloud storage"
    suggestions = creativity_tool.get_creative_suggestions(test_topic, count=5)
    
    print("   ✅ Creativity tool working!")
    print(f"   Sample variations: {suggestions.get('variations', [])[:3]}")
    print(f"   Sample combinations: {suggestions.get('combinations', [])[:3]}")
except Exception as e:
    print(f"   ❌ Creativity tool error: {e}")

# Test memory tool
print("\n4. Testing Memory Tool...")
try:
    from tools import memory_store
    
    memory_store.save("test", {"message": "Hello"})
    result = memory_store.retrieve("test")
    
    if result:
        print("   ✅ Memory tool working!")
    else:
        print("   ❌ Memory tool not storing data")
except Exception as e:
    print(f"   ❌ Memory tool error: {e}")

# Summary
print("\n" + "=" * 60)
print("Setup Test Complete!")
print("=" * 60)
print("\nIf all checks passed, you can start the server with:")
print("  python main.py")
print("\nThen open index.html in your browser to use the UI.")
print("=" * 60)
