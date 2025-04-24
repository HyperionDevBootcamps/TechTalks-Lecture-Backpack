import tkinter as tk
from tkinter import scrolledtext

# Create the main application window
window = tk.Tk()

# Set the window title and dimensions
window.title("ChatBuddy 🤖")
window.geometry("700x500")

# Create a scrollable text area to display the chat
chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, font=("Arial", 16), width=50, height=8)
chat_area.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

# Disable editing in the chat area (only display messages, no direct input from users)
chat_area.config(state='disabled')

# Function to handle sending a message and getting a response
def send_message():
    """
    This function gets the user's input from the entry box, displays the user's message in the chat area,
    and provides an appropriate response based on the input. It then updates the chat area with the bot's response.
    """
    
    # Get the message entered by the user
    user_message = user_input.get()
    
    # If the user did not type anything, do nothing
    if not user_message:
        return

    # Enable editing in the chat area to add the new message
    chat_area.config(state='normal')
    
    # Insert the user's message into the chat area
    chat_area.insert(tk.END, "You: " + user_message + "\n")

    # Define the response to be displayed
    response = ""

    # Provide different responses based on the user's input
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

    # Insert the bot's response into the chat area
    chat_area.insert(tk.END, "ChatBuddy: " + response + "\n")
    
    # Disable editing again to prevent the user from typing directly in the chat area
    chat_area.config(state='disabled')
    
    # Clear the user's input field after sending the message
    user_input.delete(0, tk.END)

# Create an input field where the user can type their message
user_input = tk.Entry(window, font=("Arial", 14))

# Display the input field and make it fill the available horizontal space
user_input.pack(padx=10, pady=10, fill=tk.X)

# Bind the 'Enter' key to trigger the send_message function when pressed
user_input.bind("<Return>", lambda event: send_message())

# Create a button to allow the user to send a message by clicking
send_button = tk.Button(window, text="Send", font=("Arial", 14), command=send_message)

# Display the button below the input field
send_button.pack(padx=10, pady=5)

# Start the application's main loop, which keeps the window open and responsive
window.mainloop()
