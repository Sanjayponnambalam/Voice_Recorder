#For user speech 
import speech_recognition as sr
#For Graphical User Interface 
import tkinter as tk
from tkinter import*
#Voice Assistant for GUI
import pyttsx3
#To record user's voice
import sounddevice as sound
#To write the audio file as WAV File
from scipy.io.wavfile import write
import wavio as wv
global engine
engine=pyttsx3.init()


global audio

#For GUI
gui=tk.Tk()

#Elements for GUI
gui.title("*VOICE RECORDER*")
gui.geometry("900x500")
gui.resizable(False,False)
gui.configure(bg="black")
img=PhotoImage(file="recorder.png")
gui.iconphoto(False,img)
imgb=PhotoImage(file="recorder.png")
i=Label(image=imgb,height=300,width=225)

i.place(x=330,y=150)

def end():
    #To close the GUI
    engine.say("Thank You")
    engine.runAndWait()
    gui.destroy()
    
def recog():
    #To record user's voice
    hz=44100
    re=sound.rec(50*hz,samplerate=hz,channels=2)
    sound.wait()
    #Write the audio as WAV file
    write("recordings.wav",hz,re)
    if True:
        #Message to user for recording voice successfully.
        engine.say("voice recorded successfully")
        engine.runAndWait()

def startt():
    
    #Voice assisted GUI 
    engine.say("Voice Recorder")
    engine.runAndWait()
    
    def usernam():
    
        with sr.Microphone() as mic:
            engine.say("Welcome")
            engine.runAndWait()
            engine.say("Start speaking by clicking the record button")
            engine.runAndWait()
           
        
        try:
            pass
        except:
            pass

        
    usernam()
    

#Configuration elements For TopFrame of GUI 
top_frame=Frame(gui,bg="red",width=900,height=100)
top_frame.place(x=0,y=0)

#Configuration elements For Title bar
Label(top_frame,text="VOICE RECORDER",font="Algerian 25 bold",bg="yellow",fg="black").place(x=300,y=30)

#Configuration elements for Start button 
s=Button(gui,text="START",width=10,bg="white",font='arial 10 bold',command=startt)
s.place(x=200,y=100)

#Config elements for Exit button       
exit_button = Button(gui, text="EXIT",width=10,bg="white",font='arial 10 bold', command=end)
exit_button.place(x=600,y=100)

#Config elements for Record Button
record=Button(gui,text="RECORD",width=10,font="arial 10 bold",fg="black",command=recog)
record.place(x=400,y=100)

#Run the tkinter GUI
gui.mainloop()

