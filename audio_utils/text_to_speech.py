from gtts import gTTS
import os
import tempfile

class TextToSpeech:
    def speak(self, text):
        """Use Google's TTS service"""
        print(f"Bot: {text}")
        try:
            tts = gTTS(text=text, lang='en')
            with tempfile.NamedTemporaryFile(delete=True) as fp:
                temp_path = f"{fp.name}.mp3"
                tts.save(temp_path)
                os.system(f"afplay {temp_path}")
                os.remove(temp_path)
        except Exception as e:
            print(f"TTS Error: {e}")