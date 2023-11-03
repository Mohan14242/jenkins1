import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence

# Load the MP3 audio file
mp3_file = "Desktop/mohan.mp3"  # Replace with your MP3 audio file path
audio = AudioSegment.from_mp3(mp3_file)

# Initialize the recognizer
recognizer = sr.Recognizer()

# Split the audio into segments on silence
audio_segments = split_on_silence(audio, silence_thresh=-40)  # Adjust silence threshold as needed

# Recognize the text from each audio segment
recognized_text = []

for audio_segment in audio_segments:
    with sr.AudioData(audio_segment.raw_data, audio_segment.frame_rate, audio_segment.frame_width) as source:
        try:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
            recognized_text.append(text)
        except sr.UnknownValueError:
            pass  # Handle unknown audio segments

# Combine recognized text from all segments
final_text = " ".join(recognized_text)

print("Text from MP3 audio: ", final_text)
