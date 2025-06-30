import google.generativeai as genai
import time
from config import GEMINI_API_KEY, MAX_CONVERSATION_HISTORY

class GeminiClient:
    def __init__(self):
        if not GEMINI_API_KEY:
            raise ValueError("API key not configured!")
        
        genai.configure(api_key=GEMINI_API_KEY)
        
        # Using the lighter flash model
        self.model = genai.GenerativeModel('models/gemini-1.5-flash-latest')
        self.conversation = self.model.start_chat(history=[])
        self.last_request_time = 0
        print("Initialized Gemini model: gemini-1.5-flash-latest")

    def get_response(self, prompt):
        try:
            # Rate limiting (1 request per second)
            time_since_last = time.time() - self.last_request_time
            if time_since_last < 1.0:
                time.sleep(1.0 - time_since_last)
            
            self.last_request_time = time.time()
            
            response = self.conversation.send_message(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=0.7,  # Balanced creativity
                    top_p=0.95
                )
            )
            
            # Trim history
            if len(self.conversation.history) > MAX_CONVERSATION_HISTORY:
                self.conversation.history = self.conversation.history[-MAX_CONVERSATION_HISTORY:]
            
            return response.text
        
        except Exception as e:
            print(f"Gemini Error: {e}")
            return "I'm reaching my conversation limit. Please try again in a moment."
   