import os
from gtts import gTTS
import subprocess
import platform

def text_to_speech_with_gtts(input_text, output_filepath):
    language = "en"
    audio_obj = gTTS(text=input_text, lang=language, slow=False)
    audio_obj.save(output_filepath)
    
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            os.startfile(output_filepath)  # This will play the MP3 file using the default media player
        elif os_name == "Linux":  # Linux
            subprocess.run(['mpg123', output_filepath])  # This will play the MP3 file using mpg123
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

#input_text = "Hi this is Shreesha, From India!"
#text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing_autoplay.mp3")

