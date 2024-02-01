import time
import requests
import json


def Speak(a):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SPVoice")
    speak.Speak(a)


req = requests.get(
    # "https://newsapi.org/v2/top-headlines?country=us&apiKey=4fa33d39840c41d0be613d3e88af5802"
    # "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=4fa33d39840c41d0be613d3e88af5802"
    # "https://newsapi.org/v2/top-headlines?country=us&apiKey=4fa33d39840c41d0be613d3e88af5802"
    # "https://newsapi.org/v2/everything?q=tesla&from=2022-09-29&sortBy=publishedAt&apiKey=4fa33d39840c41d0be613d3e88af5802"
    #  "https://newsapi.org/v2/everything?q=tesla&from=2022-09-29&sortBy=publishedAt&apiKey=4fa33d39840c41d0be613d3e88af5802"
    "https://newsapi.org/v2/everything?q=bitcoin&apiKey=4fa33d39840c41d0be613d3e88af5802"
)
tex = req.text
txt = json.loads(tex)
# txt = req.json()
for i in txt["articles"]:
    t = i["title"]
    d = i["description"]
    final = f"The title is {t} the news description is {d}"
    print(f"The title is {t}\nThe news description is {d}\n")
    Speak(final)
    # time.sleep(5.0)
Speak("Ho gya aaje ka")
print("Khatam")
Speak("Khhtam")
