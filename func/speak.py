import pyttsx3

# Initialize the text-to-speech engine once at the global level
engine = pyttsx3.init('sapi5')

# Function for speak the text response
def speak(text):
    voices = engine.getProperty('voices') # Get the available voices
    engine.setProperty('voice', voices[0].id) # Set the desired voice(0 for make & 1 for female)

    engine.setProperty('rate', 175) # Adjust the speech rate (default is usually around 200)
    engine.setProperty('volume', 1) # Adjust the volume (0.0 to 1.0)

    engine.say(text)
    engine.runAndWait()