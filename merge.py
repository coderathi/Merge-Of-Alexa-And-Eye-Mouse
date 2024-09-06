
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import cv2
import mediapipe as mp
import pyautogui
from PIL.Image import merge

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

listener = sr.Recognizer()
speak("hello sir,am your alexa")
speak("what can i do for you")


def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
       with sr.Microphone() as source:
             print('listening...')
             voice = listener.listen(source)
             command = listener.recognize_google(voice)
             command = command.lower()
             if 'alexa' in command:
                 command = command.replace('alexa','')
                 print(command)

    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime(' %I:%M %p ')
        print(time)
        talk('Current time is'+ time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is','')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry,I have a headache sir')
    elif 'are you single' in command:
        talk('i am in a relationship with wifi sir')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'open youtube' in command:
        talk('open youtube sir')
        webbrowser.open("https://youtube.com")
        mergeimage()
    elif 'open chrome' in command:
        talk('open chrome sir')
        webbrowser.open("https://chrome.com")
        mergeimage()
    elif 'open map' in command:
        talk('open map sir')
        webbrowser.open("https://www.google.com/maps")
        mergeimage()
    elif 'open world map' in command:
        talk('open world map')
        webbrowser.open("https://www.worldometers.info/world-map/")
        mergeimage()
    elif 'open 3d map' in command:
        talk('open 3d map')
        webbrowser.open("https://earth3dmap.com/")
        mergeimage()
    elif 'open weather page' in command:
        talk('open weather page')
        webbrowser.open("https://www.accuweather.com/en/in/india-weather")
        mergeimage()
    elif 'open google' in command:
        talk('open google')
        webbrowser.open("https://www.google.com")
        mergeimage()
    elif 'open instagram ' in command:
        talk('open instagram')
        webbrowser.open("https://www.instagram.com")
        mergeimage()
    elif 'open whatsapp ' in command:
        talk('open whatsapp')
        webbrowser.open("https://www.whatsapp.com")
        mergeimage()
    elif 'open telegram' in command:
        talk('open telegram')
        webbrowser.open("https://www.telegram.com")
        mergeimage()
    elif 'open snapchat' in command:
        talk('open snapchat')
        webbrowser.open("https://www.snapchat.com")
        mergeimage()
    elif 'open facebook' in command:
        talk('open facebook')
        webbrowser.open("https://www.facebook.com")
        mergeimage()
        mergeimage()
    elif 'open vs code' in command:
        talk('open vs code')
        webbrowser.open("https://code.visualstudio.com/")
        mergeimage()
    elif 'open chat gpt' in command:
        talk('open chat gpt')
        webbrowser.open("https://chatgpt.com/")
        mergeimage()

    else:
        talk('please say the command again. ')





def mergeimage():
    cam = cv2.VideoCapture(0)
    face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
    screen_w, screen_h = pyautogui.size()
    while True:
        _, frame = cam.read()
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = face_mesh.process(rgb_frame)
        landmark_points = output.multi_face_landmarks
        frame_h, frame_w, _ = frame.shape
        if landmark_points:
            landmarks = landmark_points[0].landmark
            for id, landmark in enumerate(landmarks[474:478]):
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x, y), 3, (0, 255, 0))
                if id == 1:
                    screen_x = screen_w / frame_w * x
                    screen_y = screen_h / frame_h * y
                    pyautogui.moveTo(screen_x, screen_y)
            left = [landmarks[145], landmarks[159]]
            for landmark in left:
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x, y), 3, (0, 255, 255))
            if (left[0].y - left[1].y) < 0.004:
                pyautogui.click()
                pyautogui.sleep(1)

        cv2.imshow('Eye Controlled Mouse', frame)
        cv2.waitKey(1)


while True:
    run_alexa()