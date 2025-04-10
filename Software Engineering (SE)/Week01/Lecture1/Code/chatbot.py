import tkinter as tk
from tkinter import scrolledtext

window = tk.Tk()

window.title("ChatBuddy 🤖")
window.geometry("700x500")

chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, font=("Arial", 16), width=50, height=8)
chat_area.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

chat_area.config(state='disabled')

def send_message():
    """
    This function gets the user's input from the entry box, displays the user's message in the chat area,
    and provides an appropriate response based on the input. It then updates the chat area with the bot's response.
    """
    user_message = user_input.get()
    
    if not user_message:
        return

    chat_area.config(state='normal')
    chat_area.insert(tk.END, "You: " + user_message + "\n")
    response = ""
    if user_message.lower() == "hey" or user_message.lower() == "hi":
        response = "Hello! How can I assist you today?"
    elif user_message.lower() == "bye":
        response = "Goodbye! Have a great day!"
    elif "name" in user_message.lower():
        response = "I'm ChatBuddy! Your friendly Python chatbot."
    elif "weather" in user_message.lower():
        response = "I'm not connected to the internet... but I bet it's sunny somewhere!"
    elif "joke" in user_message.lower():
        response = "Why did the developer go broke? Because they used up all their cache!"
    else:
        response = "Hmm... I don't understand that yet. I'm still learning!"

    chat_area.insert(tk.END, "ChatBuddy: " + response + "\n")
    chat_area.config(state='disabled')

    user_input.delete(0, tk.END)

user_input = tk.Entry(window, font=("Arial", 14))
user_input.pack(padx=10, pady=10, fill=tk.X)
user_input.bind("<Return>", lambda event: send_message())
send_button = tk.Button(window, text="Send", font=("Arial", 14), command=send_message)
send_button.pack(padx=10, pady=5)
window.mainloop()
