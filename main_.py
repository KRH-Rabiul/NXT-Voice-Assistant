import speech_recognition as sr
import pyttsx3
import webbrowser
import musicLibrary
import requests
import datetime
import sys
from openai import OpenAI

# -----------------------------
# Initial Setup
# -----------------------------
recognizer = sr.Recognizer()
recognizer.energy_threshold = 400
recognizer.pause_threshold = 0.8

newsapi = "ff2be5743f2342b284461738a833b9ac"

# -----------------------------
# OpenRouter Setup
# -----------------------------
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)

def ask_ai(question):
    try:
        completion = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": question}
            ],
            max_tokens=200
        )

        return completion.choices[0].message.content

    except Exception as e:
        print("AI Error:", e)
        return "AI service unavailable."


# -----------------------------
# Fresh Engine Speak Function
# -----------------------------
def speak(text):
    try:
        engine = pyttsx3.init(driverName='sapi5')
        engine.setProperty('rate', 170)
        engine.setProperty('volume', 1)

        engine.say(text)
        engine.runAndWait()

        engine.stop()
        del engine

    except Exception as e:
        print("Speak Error:", e)


# -----------------------------
# Listen Function
# -----------------------------
def listen(timeout=5, phrase_time_limit=5):
    with sr.Microphone() as source:
        audio = recognizer.listen(
            source,
            timeout=timeout,
            phrase_time_limit=phrase_time_limit
        )
    return recognizer.recognize_google(audio).lower()


# -----------------------------
# Command Processing
# -----------------------------
def process_command(command):

    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "open facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://facebook.com")

    elif "open linkedin" in command:
        speak("Opening LinkedIn")
        webbrowser.open("https://linkedin.com")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    elif command.startswith("play"):
        parts = command.split()
        if len(parts) > 1:
            song = parts[1]
            if song in musicLibrary.music:
                speak(f"Playing {song}")
                webbrowser.open(musicLibrary.music[song])
            else:
                speak("Song not found")
        else:
            speak("Please say the song name")

    elif "news" in command:
        try:
            speak("Here are the top headlines")
            url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}"
            r = requests.get(url)

            if r.status_code == 200:
                data = r.json()
                articles = data.get("articles", [])

                if not articles:
                    speak("No news found")
                else:
                    for article in articles[:5]:
                        speak(article["title"])
            else:
                speak("News service unavailable")

        except Exception as e:
            print("News Error:", e)
            speak("Failed to fetch news")

    elif "exit" in command or "stop" in command:
        speak("Shutting down")
        sys.exit()

    else:
        speak("Thinking...")
        reply = ask_ai(command)
        speak(reply)


# -----------------------------
# Main Program
# -----------------------------
if __name__ == "__main__":
    speak("Initializing NXT")

    with sr.Microphone() as source:
        print("Calibrating microphone...")
        recognizer.adjust_for_ambient_noise(source, duration=3)

    while True:
        try:
            print("Waiting for wake word...")
            wake_word = listen(timeout=5, phrase_time_limit=3)
            print("Heard:", wake_word)

            if "nxt" in wake_word:
                speak("Yes Boss")
                print("Listening for command...")
                command = listen(timeout=5, phrase_time_limit=5)
                print("Command:", command)
                process_command(command)

        except sr.WaitTimeoutError:
            print("Listening timeout...")

        except sr.UnknownValueError:
            print("Could not understand audio")

        except sr.RequestError:
            print("Internet connection problem")

        except Exception as e:
            print("Error:", e)
