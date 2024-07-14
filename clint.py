import speech_recognition as sr
import webbrowser
import pyttsx3
import musicliberary as m
import requests

engine = pyttsx3.init()

password = "rashi singh"

def speak(text):
    engine.say(text)
    engine.runAndWait()

newsapi = "d1bf7c863b214d28bd8578a8563c9697"
def news():
    try:
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        r.raise_for_status()  # This will raise an HTTPError if the HTTP request returned an unsuccessful status code
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        exit()

    # Process the response
    try:
        data = r.json()

        # Extract the articles
        articles = data.get("articles", [])

        # Print the headlines
        for article in articles:
            title = article.get('title')
            if title:
                speak(title)
            else:
                print("No title found for article:", article)
    except ValueError as e:
        print(f"Error parsing JSON: {e}")
    except KeyError as e:
        print(f"Error accessing key: {e}")


def open_google_search(query):
    # Create the Google search URL
    url = f"https://www.google.com/search?q={query}"
    print(f"Opening URL: {url}")  # Debugging information
    # Open the URL in a new browser tab
    success = webbrowser.open_new_tab(url)
    if not success:
        print("Failed to open a new tab, trying a new window.")
        webbrowser.open(url)


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    
    elif "open chatgpt" in c.lower():
        webbrowser.open("https://chatgpt.com")
    
    elif "open youtube" in c.lower():
        webbrowser.open_new_tab("https://youtube.com")

    elif "open insta" in c.lower():
        x = input("Enter the password: ")
        if x == password:
            webbrowser.open_new_tab("https://www.instagram.com/")
    
    elif c.lower().startswith("play"):
        l = c.lower().split(" ")
        if len(l) < 2:
            return
        
        elif len(l) == 2:
            song = l[1]
            singer = "0"
            print("not given the name of singer")
        
        else :
            singer = str(l[1])
            song = " ".join(l[2:])

        print(singer)
        print(song)
        webbrowser.open(m.play_songs(singer,song))
   
    elif "news" in c.lower():
        news()

    else:
        #let open ai handle the request
        open_google_search(c)


'''from openai import OpenAI

# client = OpenAI()

client = OpenAI(
    api_key="sk-proj-i1bcsrCv4EXDIQ5B0milT3BlbkFJ7QwKfV6IUVaFKzJYE6ZF",
)


completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant , jarvis , skilled in general tasks like Alexa and Google."},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message)'''