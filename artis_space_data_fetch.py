import subprocess
import speech_recognition as sr
import requests

# Initialize the recognizer
recognizer = sr.Recognizer()

def fetch_space_data(study_id):
    url = f"https://osdr.nasa.gov/osdr/data/osd/files/{study_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching space data for study ID {study_id}: {response.status_code}")
        return None

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
        elif "space data" in text.lower():
            # Extract the study ID from the user's input (assuming it's in the format "study ID XXX")
            study_id = text.split()[-1]
            space_data = fetch_space_data(study_id)
            if space_data:
                print("Space data:")
                print(space_data)
                return space_data
            else:
                print("Failed to fetch space data.")
                return None
        else:
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
