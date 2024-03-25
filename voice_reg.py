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
        #text = recognizer.recognize_google(audio)          #for English Command
        print("You said: " + text)
    except sr.UnknownValueError:
        text = ""
        print("Sorry, I didn't understand that.")
    except sr.RequestError as e:
        text = ""
        print("Error; {0}".format(e))
    return text



# Main commands
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

    elif 'نظرت راجع به محمدرضا چیه' in text.lower():
        speak = pyttsx3.init()
        voices = speak.getProperty('voices')
        speak.setProperty('voice', voices[2].id)
        speak.setProperty('rate', 150)
        speak.say("         ok My Lord! , I think this person is ..... .        ha  ha ha ha  ha ha")
        webbrowser.open("https://www.google.com/search?q=%D8%A7%D8%AF%D9%85+%D9%86%D8%A7%D8%AF%D8%A7%D9%86&tbm=isch&ved=2ahUKEwjxy4Hf842FAxUwkP0HHcf1ANMQ2-cCegQIABAA&oq=%D8%A7%D8%AF%D9%85+%D9%86%D8%A7%D8%AF%D8%A7%D9%86&gs_lp=EgNpbWciEdin2K_ZhSDZhtin2K_Yp9mGSPEVUM8HWMoUcAB4AJABAJgBAKABAKoBALgBA8gBAPgBAYoCC2d3cy13aXotaW1niAYB&sclient=img&ei=TqMAZvHsLbCg9u8Px-uDmA0&bih=967&biw=1905&hl=en#imgrc=cz97Lx6JdPtjYM")
        speak.runAndWait()

    elif 'نظرت راجع به داوود رمضانی چیه' in text.lower():
        speak = pyttsx3.init()
        voices = speak.getProperty('voices')
        speak.setProperty('voice', voices[2].id)
        speak.setProperty('rate', 150)
        speak.say("         yes My Lord! , I think this person is ..... .        ha  ha ha ha  ha ha")
        webbrowser.open("https://img.ketabrah.ir/img/l/8232521548900865.jpg")
        speak.runAndWait()

    elif 'وضعیت آب و هوای چالوس رو بهم بگو' in text.lower():
        speak = pyttsx3.init()
        voices = speak.getProperty('voices')
        speak.setProperty('voice', voices[2].id)
        speak.setProperty('rate', 150)
        speak.say("         yes My Lord! , This is the weather condition of Chalus this week.")
        webbrowser.open("https://www.google.com/search?q=%D8%A7%D8%A8+%D9%87%D9%88%D8%A7%DB%8C+%DA%86%D8%A7%D9%84%D9%88%D8%B3&oq=%D8%A7%D8%A8+%D9%87%D9%88%D8%A7%DB%8C+%DA%86%D8%A7%D9%84%D9%88%D8%B3&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQRRg8MgYIAhBFGDwyBggDEEUYPDIGCAQQLhhA0gEIMzMxN2owajGoAgCwAgA&sourceid=chrome&ie=UTF-8")
        speak.runAndWait()
    
    elif 'وضعیت آب و هوای نوشهر رو بهم بگو' in text.lower():
        speak = pyttsx3.init()
        voices = speak.getProperty('voices')
        speak.setProperty('voice', voices[2].id)
        speak.setProperty('rate', 150)
        speak.say("         yes My Lord! , This is the weather condition of Nowshahr this week.")
        webbrowser.open("https://www.google.com/search?q=%D8%A7%D8%A8+%D9%87%D9%88%D8%A7%DB%8C+%D9%86%D9%88%D8%B4%D9%87%D8%B1&sca_esv=aab80bd44fbfc9fb&sxsrf=ACQVn0-oiMEYf1P2fvBbQEwz26puR2ugJw%3A1711349643752&ei=ix8BZsy8LeSDxc8PnISV6Ak&ved=0ahUKEwiMruic6o6FAxXkQfEDHRxCBZ0Q4dUDCBA&uact=5&oq=%D8%A7%D8%A8+%D9%87%D9%88%D8%A7%DB%8C+%D9%86%D9%88%D8%B4%D9%87%D8%B1&gs_lp=Egxnd3Mtd2l6LXNlcnAiGNin2Kgg2YfZiNin24wg2YbZiNi02YfYsTIEEAAYRzIEEAAYRzIEEAAYRzIEEAAYRzIEEAAYRzIEEAAYRzIEEAAYRzIEEAAYR0ihHFDKCliWG3AAeASQAQCYAQCgAQCqAQC4AQPIAQD4AQGYAgOgAo0BmAMAiAYBkAYIkgcBM6AHAA&sclient=gws-wiz-serp")
        speak.runAndWait()

        
    elif "hello" in text.lower():
        print("Hello! How can I help you?")
    elif "خداحافظ" in text.lower():
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

