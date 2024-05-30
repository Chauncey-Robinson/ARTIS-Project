import subprocess
import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

    try:
        # Use Google's speech recognition
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        if "stop listening" in text.lower():
            print("Stopping listening...")
            return None
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return None
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return None

def respond(text):
    # Use macOS built-in 'say' command to convert text to speech
    subprocess.run(['say', text])

if __name__ == "__main__":
    while True:
        user_input = listen()
        if user_input is not None:
            respond(user_input)
        else:
            break  # Stop the loop if the "stop listening" command is detected



   






