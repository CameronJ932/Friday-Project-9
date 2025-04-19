import openai
import tkinter as tk
from tkinter import scrolledtext
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

    def get_open_ai_repsonse():
        prompt = entry_prompt.get()

        chat_completion = client.chat.completions.create(
        messages=[
        {
        "role": "user",
        "content": prompt,
        }
        ],
        model="gpt-4o-2024-08-06",
        max_tokens = 50
        )

        print(chat_completion.choices[0].message.content)

    def open_initial_window():
        initial_window = tk.Tk()
        initial_window.title("Initial Window")
        initial_window.geometry("800x500")
        initial_window.config(bg="lightblue")

        label_intro = tk.Label(initial_window, text="Welcome to ChatGPT API Interface", font=("Arial",14))
        label_intro.pack(pady=10)

        label_prompt = tk.Label(initial_window, text="Input your Promt: ", font=("Arial",14))
        label_prompt.pack(pady=20)
        entry_prompt = tk.Entry(initial_window, width = "50")
        entry_prompt.pack(pady=20)

        label_prompt = tk.Label(initial_window, text="Output: ", font=("Arial",14))
        label_prompt.pack(pady=20)
        output_text = scrolledtext.ScrolledText(initial_window, width=60, height=10)
        output_text.pack(padx=10, pady=10)

        initial_window.mainloop()

open_initial_window()