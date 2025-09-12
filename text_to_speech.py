import os
import elevenlabs
from elevenlabs.client import ElevenLabs
import subprocess
import platform
from dotenv import load_dotenv
from pydub import AudioSegment
from pydub.playback import play  # Replaces playsound for Windows MP3
load_dotenv()

ELEVENLABS_API_KEY = os.getenv("ELEVEN_LABS_API_KEY")

def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio = client.text_to_speech.convert(
        text=input_text,
        voice_id="ZF6FPAbjXT4488VcRRnw",
        model_id="eleven_multilingual_v2",
        output_format="mp3_22050_32",
    )
    elevenlabs.save(audio, output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":
            sound = AudioSegment.from_file(output_filepath, format="mp3")
            play(sound)
        elif os_name == "Linux":
            subprocess.run(['aplay', output_filepath])
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

from gtts import gTTS

def text_to_speech_with_gtts(input_text, output_filepath):
    language = "en"

    audioobj = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":
            sound = AudioSegment.from_file(output_filepath, format="mp3")
            play(sound)
        elif os_name == "Linux":
            subprocess.run(['aplay', output_filepath])
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")


