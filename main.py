from audio_utils.speech_to_text import SpeechToText
from audio_utils.text_to_speech import TextToSpeech
from gemini_integration.gemini_client import GeminiClient

class VoiceChatbot:
    def __init__(self):
        self.stt = SpeechToText()
        self.tts = TextToSpeech()
        self.gemini = GeminiClient()
    
    def run(self):
        print("Voice-enabled Chatbot is ready!")
        self.tts.speak("Hello! I'm your voice assistant. How can I help you today?")
        
        while True:
            try:
                # Listen to user
                user_input = self.stt.listen()
                if not user_input:
                    continue
                
                # Exit command
                if user_input.lower() in ["exit", "quit", "bye"]:
                    self.tts.speak("Goodbye! Have a great day!")
                    break
                
                # Get AI response
                response = self.gemini.get_response(user_input)
                self.tts.speak(response)
                
            except KeyboardInterrupt:
                print("\nExiting...")
                self.tts.speak("Goodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")
                self.tts.speak("Sorry, something went wrong. Please try again.")

if __name__ == "__main__":
    chatbot = VoiceChatbot()
    chatbot.run()