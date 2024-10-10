import speech_recognition as sr
from .speak import speak

# Initialize the speech recognizer
r = sr.Recognizer()
r.energy_threshold = 300 # Adjust for silence detection
r.dynamic_energy_threshold = True

# Function for listen the input-voice and recognize it
def listen():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1) # Adjustment for ambient noises
            print("    Listening...")
            audio = r.listen(source, timeout=5, phrase_time_limit=10)

        print("    Recognizing...")
        command = r.recognize_google(audio) # Use the speech recognizer to convert speech to text
        print(command)
    except Exception as e:
        speak("Sorry, I didn't catch that!")
        return ""
    
    return command