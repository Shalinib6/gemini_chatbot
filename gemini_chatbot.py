# Gemini AI Chatbot
# File: gemini_chatbot.py

import google.generativeai as genai

# STEP 1: Put your API key here
API_KEY = "AIzaSyAe8faZWf23mozw3LVeYk0JXZiKoV0chDc"  # Replace with your real API key

print("🚀 Starting Gemini Chatbot...")

# Check API key
if API_KEY == "AIzaSyAe8faZWf23mozw3LVeYk0JXZiKoV0chDc":
    print("❌ ERROR: Please replace YOUR_API_KEY_HERE with your real API key!")
    print("Get it from: https://aistudio.google.com/app/apikey")
    exit()

# Configure Gemini
try:
    genai.configure(api_key=API_KEY)
    print("✅ Connected to Gemini!")
    
    # Create model
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # Test connection
    response = model.generate_content("Say hello!")
    print(f"🤖 Gemini says: {response.text}")
    
except Exception as e:
    print(f"❌ Error: {e}")
    exit()

# Chat function
def chat_with_gemini(question):
    try:
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        return f"Error: {e}"

# Interactive chat
def start_chat():
    print("\n💬 Chat started! Type 'quit' to exit.")
    print("-" * 40)
    
    while True:
        user_input = input("\nYou: ")
        
        if user_input.lower() == 'quit':
            print("👋 Goodbye!")
            break
            
        answer = chat_with_gemini(user_input)
        print(f"🤖 Gemini: {answer}")

# Run the chatbot
if __name__ == "__main__":
    start_chat()
