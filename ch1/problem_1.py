import pyjokes
import pyttsx3
joke = pyjokes.get_joke()
print(joke)
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
engine.say(joke)
engine.runAndWait()