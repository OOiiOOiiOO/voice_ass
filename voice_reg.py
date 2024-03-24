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

    elif 'محمد رضا یحیایی' in text.lower():
        speak = pyttsx3.init()
        voices = speak.getProperty('voices')
        speak.setProperty('voice', voices[2].id)
        speak.setProperty('rate', 150)
        speak.say("         Hello My Lord! , I think this person is ..... .        ha  ha ha ha  ha ha")
        webbrowser.open("https://www.google.com/search?q=%D8%A7%D8%AF%D9%85+%D9%86%D8%A7%D8%AF%D8%A7%D9%86&tbm=isch&ved=2ahUKEwjxy4Hf842FAxUwkP0HHcf1ANMQ2-cCegQIABAA&oq=%D8%A7%D8%AF%D9%85+%D9%86%D8%A7%D8%AF%D8%A7%D9%86&gs_lp=EgNpbWciEdin2K_ZhSDZhtin2K_Yp9mGSPEVUM8HWMoUcAB4AJABAJgBAKABAKoBALgBA8gBAPgBAYoCC2d3cy13aXotaW1niAYB&sclient=img&ei=TqMAZvHsLbCg9u8Px-uDmA0&bih=967&biw=1905&hl=en#imgrc=cz97Lx6JdPtjYM")
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




