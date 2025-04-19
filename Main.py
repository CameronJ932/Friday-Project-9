import openai
import tkinter as tk
from tkinter import scrolledtext
from dotenv import load_dotenv
import os

# loading the .env file
load_dotenv()

# This is the only way i can get chat to work
client = openai.OpenAI(
    api_key = os.getenv("key")
)

apikey = os.getenv("key")

# checking if apikey is actually there
if apikey is None:
    print("Error: API key not found in environment variable 'key'")

# running the program
else:
    # setting the api key so the program can use it
    openai.api_key = apikey

    # Send our prompt to the Openai api and get its response 
    def get_openai_response():
        prompt = entry_prompt.get()

        # sending our prompt and defining what model to use as well as max tokens allowed
        chat_completion = client.chat.completions.create(
        messages=[
        {
        "role": "user",
        "content": prompt,
        }
        ],
        # model selection
        model="gpt-4o-2024-08-06",
        # max tokens allowed
        max_tokens = 50
        )

        # print to the GUI
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END,chat_completion.choices[0].message.content.strip())

    # running the code for the GUI    
    initial_window = tk.Tk()
    initial_window.title("Initial Window")
    initial_window.geometry("800x500")
    initial_window.config(bg="lightblue")

    # welcoming label
    label_intro = tk.Label(initial_window, text="Welcome to ChatGPT API Interface", font=("Arial",14))
    label_intro.pack(pady=10)

    # Label and entry section for the prompt
    label_prompt = tk.Label(initial_window, text="Input your Promt: ", font=("Arial",14))
    label_prompt.pack(pady=20)
    entry_prompt = tk.Entry(initial_window, width = "50")
    entry_prompt.pack(pady=20)

    #submit button
    submit_button = tk.Button(initial_window, text="Submit", command=get_openai_response)
    submit_button.pack(padx=10, pady=10)

    # Label and entry section for the output
    label_output = tk.Label(initial_window, text="Output: ", font=("Arial",14))
    label_output.pack(pady=20)
    output_text = scrolledtext.ScrolledText(initial_window, width=60, height=10)
    output_text.pack(padx=10, pady=10)

    # Setting the mainloop
    initial_window.mainloop()

# Running the code
initial_window()