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

def open_initial_window():
    initial_window = tk.Tk()
    initial_window.title("Initial Window")
    initial_window.geometry("800x500")
    initial_window.config(bg="lightblue")

    initial_window.mainloop()

open_initial_window()