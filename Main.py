import openai
import tkinter as tk
from tkinter import messagebox
from dotenv import load_dotenv
import os

load_dotenv()

#This is the only way i can get chat to work
client = openai.OpenAI(
    api_key = os.getenv("key")
)

apikey = os.getenv("key")

def open_intial_window():
    intial_window = tk.Tk()
    intial_window.title("Window")
    intial_window.geometry("800x500")
    intial_window.config(bg="lightblue")

    intial_window.mainloop()

open_intial_window()