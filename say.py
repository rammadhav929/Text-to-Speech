import pyttsx3


def generate_audio(text, filename):
    play = pyttsx3.init()  # Added initialization of pyttsx3 engine inside the function
    play.setProperty("rate", 100)
    voices = play.getProperty("voices")
    play.setProperty("voice", voices[1].id)
    play.save_to_file(text, filename)
    play.say(text)

    play.runAndWait()  # Removed redundant call to runAndWait
