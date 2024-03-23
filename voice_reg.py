import speech_recognition as sr 
import pyttsx3
import webbrowser



recognizer = sr.Recognizer()

def capture_voice_input():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    return audio



def convert_voice_to_text(audio):
    try:
        text = recognizer.recognize_google(audio, language ='fa-IR')
        #text = recognizer.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        text = ""
        print("Sorry, I didn't understand that.")
    except sr.RequestError as e:
        text = ""
        print("Error; {0}".format(e))
    return text




def process_voice_command(text):
    
    if 'یوتیوب رو باز کن' in text.lower():
        speak = pyttsx3.init()
        voices = speak.getProperty('voices')
        speak.setProperty('voice', voices[2].id)
        speak.setProperty('rate', 150)
        speak.say("                Yes my lord! , Here you go to Youtube\n")
        speak.runAndWait()
        webbrowser.open("youtube.com")
    if "hello" in text.lower():
        print("Hello! How can I help you?")
    elif "goodbye" in text.lower():
        print("Goodbye! Have a great day!")
        return True
    else:
        print("I didn't understand that command. Please try again.")
    return False
    


def main():
    end_program = False
    while not end_program:
        audio = capture_voice_input()
        text = convert_voice_to_text(audio)
        end_program = process_voice_command(text)

        




if __name__ == "__main__":
    main()



#import pyttsx3
#import time
#engine = pyttsx3.init()
#
#engine.say("                   I will speak this text")
#engine.runAndWait()




