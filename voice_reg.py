import speech_recognition as sr 
import pyttsx3
import webbrowser
from pydub import AudioSegment
from pydub.playback import play


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

    elif 'سلام کاوایی' in text.lower():
        speak = pyttsx3.init()
        voices = speak.getProperty('voices')
        speak.setProperty('voice', voices[2].id)
        speak.setProperty('rate', 150)
        speak.say("         Hello My Lord! , Have a Good Day, How can I help you?")
        speak.runAndWait()

    elif 'انیمه شیطان کش کی پخش میشه' in text.lower():
        speak = pyttsx3.init()
        voices = speak.getProperty('voices')
        speak.setProperty('voice', voices[2].id)
        speak.setProperty('rate', 150)
        speak.say("         Hello My Lord! , I Search for you about this Anime.        ha  ha ha ha  ha ha")
        webbrowser.open("https://www.google.com/search?q=when+demon+slayer+season+5+release&sca_esv=100a8d72724cfbcd&sxsrf=ACQVn0-KcEtinDHb88paSkCDYfk_VZeEpA%3A1711203613978&source=hp&ei=HeX-ZdbLOfK_xc8P4viMyAg&iflsig=ANes7DEAAAAAZf7zLcJx0S-czAdF0DUXjCWAaCv8WECp&oq=when+demon+slayer+season+5+re&gs_lp=Egdnd3Mtd2l6Ih13aGVuIGRlbW9uIHNsYXllciBzZWFzb24gNSByZSoCCAAyBRAAGIAEMgUQABiABDIFEAAYgAQyBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHkjr3gJQ9AlY19ACcAt4AJABApgBtRagAdyuAaoBEjAuMTYuMy4yLjYtMi4zLjIuNLgBA8gBAPgBAZgCKKACq4ABqAIKwgIHECMY6gIYJ8ICChAjGIAEGIoFGCfCAgQQIxgnwgILEC4YgAQYxwEY0QPCAgUQLhiABMICBxAAGIAEGArCAgcQLhgKGIAEwgIHEC4YgAQYCsICBRAhGKABwgIHEAAYgAQYDcICCxAAGIAEGIoFGIYDmANIkgcRMTEuMTEuOC4yLjYtMi41LjGgB6-SAg&sclient=gws-wiz")
        speak.runAndWait()
        
    elif 'آهنگ' in text.lower():
        speak = pyttsx3.init()
        voices = speak.getProperty('voices')
        speak.setProperty('voice', voices[2].id)
        speak.setProperty('rate', 150)
        speak.say("         Hello My Lord! , this is your music my lord.        ha  ha ha ha  ha ha")
        #song = AudioSegment.from_mp3("test.mp3")
        #play(song)
        #playsound('/home/ooiioooiioo/Music/test.mp3')
        speak.runAndWait()

    elif "hello" in text.lower():
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




