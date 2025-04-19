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