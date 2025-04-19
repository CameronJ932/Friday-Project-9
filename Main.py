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

if apikey is None:
    print("Error: API key not found in environment variable 'key'")

else:
    openai.api_key = apikey

    def open_initial_window():
        initial_window = tk.Tk()
        initial_window.title("Initial Window")
        initial_window.geometry("800x500")
        initial_window.config(bg="lightblue")

        label_intro = tk.Label(initial_window, text="Welcome to ChatGPT API Interface", font=("Arial",14))
        label_intro.pack(pady=10)

        label_prompt = tk.Label(initial_window, text="Input your Promt: ", font=("Arial",14))
        label_prompt.pack(pady=20)
        entry_prompt = tk.Entry(initial_window, font =("Arial", 14), show="*")
        entry_prompt.pack(pady=20)

        label_output = tk.Label(initial_window, text="Output: ", font=("Arial",14))
        label_output.pack(pady=20)
        output = tk.Entry(initial_window, font =("Arial", 14), show="*")
        output.pack(pady=20)

        initial_window.mainloop()

open_initial_window()