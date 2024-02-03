import speech_recognition as sr

def test_google_speech_recognition(audio_path=None):
    r = sr.Recognizer()

    if audio_path:
        # If you want to test with an audio file, provide the path
        with sr.AudioFile(audio_path) as source:
            audio = r.record(source)
    else:
        # If you want to test with a live microphone input
        with sr.Microphone() as source:
            print("Please speak something...")
            audio = r.listen(source, timeout=5)

    try:
        print("Trying to Understand...")
        # Use recognize_google_v2
        query = r.recognize_google_v2(audio, language='en-in')
        print(f"You Said: {query}\n")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

# Test with a live microphone input
test_google_speech_recognition()

# Uncomment the line below to test with an audio file (replace 'path/to/audio/file.wav' with your file path)
# test_google_speech_recognition(audio_path='path/to/audio/file.wav')
