import nltk
import tkinter as tk
from tkinter import ttk
from utils.nlp_utils import pos_tag_sentence, tokenizer
from data.data_loader import *

def perform_pos_tagging(input_text, output_text, choice_var, custom_pos_tags):
    user_input = input_text.get("1.0", tk.END).strip()  

    if choice_var.get() == 1:
        result = pos_tag_sentence(user_input, custom_pos_tags)  
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"{result}")    
        mots_tokenises = tokenizer(user_input.lower()) 

    elif choice_var.get() == 2:
        sentences = nltk.sent_tokenize(user_input)
        output_text.delete("1.0", tk.END)
        for sentence in sentences:
            result = pos_tag_sentence(sentence, custom_pos_tags)  
            output_text.insert(tk.END, f"{result}\n")


def create_gui(root):
    input_frame = ttk.Frame(root)
    input_frame.pack(pady=10)

    input_text = tk.Text(input_frame, width=60, height=15, wrap="word")
    input_text.grid(row=0, column=0, padx=5, pady=5)

    choice_frame = ttk.Frame(root)
    choice_frame.pack(pady=5)

    choice_var = tk.IntVar()
    choice_var.set(1)

    phrase_radio = ttk.Radiobutton(choice_frame, text="Fehezanteny iray", variable=choice_var, value=1)
    phrase_radio.grid(row=0, column=0, padx=5, pady=5)

    text_radio = ttk.Radiobutton(choice_frame, text="Fehezanteny maromaro", variable=choice_var, value=2)
    text_radio.grid(row=0, column=1, padx=5, pady=5)

    submit_button = ttk.Button(choice_frame, text="Jerena", command=lambda: perform_pos_tagging(input_text, output_text, choice_var, custom_pos_tags))
    submit_button.grid(row=0, column=3, padx=5, pady=5)

    output_frame = ttk.Frame(root)
    output_frame.pack(pady=10)

    output_text = tk.Text(output_frame, width=60, height=20, wrap="word")
    output_text.grid(row=0, column=0, padx=5, pady=5)
