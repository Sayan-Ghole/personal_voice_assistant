import speech_recognition as sr
import webbrowser
import pyttsx3
import pygetwindow as gw
import musicplay

# Initialize recognizer and engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def close_window():
    try:
        windows = gw.getWindowsWithTitle("Google Chrome")  # Adjust for your browser
        for window in windows:
            if window.isActive:
                window.close()
        speak("Closed the window.")
    except Exception as e:
        speak("Failed to close the window.")
        print(e)

# Set female voice
voices = engine.getProperty('voices')
for voice in voices:
    if "female" in voice.name.lower() or "zira" in voice.id.lower():  # Adjust based on your OS
        engine.setProperty('voice', voice.id)
        break
# import pygetwindow as gw  
# pip install pygetwindow
#pip install pocketsphinx
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
   engine.say(text)
   engine.runAndWait()


   
def processcommand(command):
    command = command.lower()
    if "google" in command:
        webbrowser.open("https://www.google.com")
    elif "whatsapp" in command:
        webbrowser.open("https://whatsapp.com")
    elif "youtube" in command:
        webbrowser.open("https://youtube.com")
    elif "facebook" in command:
        webbrowser.open("https://facebook.com")
    elif "linkedin" in command:
        webbrowser.open("https://linkedin.com")
    elif "twitter" in command:
        webbrowser.open("https://twitter.com")
    elif "instagram" in command:
        webbrowser.open("https://instagram.com")
        
    elif "chat" in command:
        webbrowser.open("https://chatgpt.com")
        
    elif command.lower().startswith("play"):
        music = command.split(" ")[1]
        link = musicplay.songs[music]
        webbrowser.open(link)
    
    elif "close" in command or "close browser" in command:
        close_window()
        
    elif "invent" in command:
        speak("sayan ghole")
        
    else:
        print("not found..")
        
if __name__ == "__main__" :
    speak("hii i am zippy")
    while True:
    #lisign sand
        
        # Initialize recognizer
        r = sr.Recognizer()
        print("recognizing....")
            
        try:
            
              # Use microphone for input
            with sr.Microphone() as source:
                print("Listening...")
                
                # Capture audio from microphone
                audio = r.listen(source,timeout=5, phrase_time_limit=3)
                word = r.recognize_google(audio)
                
                print(word)
                if(word.lower() == "hey" or "gp" or "jp" or "cp"):
                    speak("yeah i am listening...")
                    
                    with sr.Microphone() as source:
                        print("Listening...")
                        
                        # Capture audio from microphone
                        audio = r.listen(source)
                        command = r.recognize_google(audio)
                        speak(f"my job is{command}")
                        processcommand(command)
                        speak("thank you")
                    
        except Exception as e:
                print("error",e)
