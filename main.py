import os
from pydub import AudioSegment
import speech_recognition as sr

def mp3_to_text(mp3_file_path):
    # Convert MP3 to WAV
    audio = AudioSegment.from_mp3(mp3_file_path)
    wav_file_path = "converted.wav"
    audio.export(wav_file_path, format="wav")

    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Load the WAV file
    with sr.AudioFile(wav_file_path) as source:
        audio_data = recognizer.record(source)

    # Perform speech recognition
    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        return "Google Speech Recognition could not understand audio"
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"

# Example usage
mp3_file_path = "/Users/omidshojaeianzanjani/Desktop/programmings /Trae/mp3totextproject/transcript.mp3"
text = mp3_to_text(mp3_file_path)
print(text)
