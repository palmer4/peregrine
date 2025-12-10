import tkinter as tk
import random
import messages as user


class peregrine():
    def __init__(self, root):
        self.root = root
        self.root.title("chat")
        self.root.geometry("400x500")
        self.root.resizable(True, True)

        self.display = tk.Text(root, height=20, width=30)
        self.display.pack(pady=10)
        self.display.insert(tk.END, "Peregrine: Hello! How can I assist you today?\n")
        self.display.config(state=tk.DISABLED)


        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.send_message)
        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack()


def reply(self, event=None):
    user.msg = self.entry.get()
    if not user.msg.strip:
        return
    
    msg = user_msg.lower()
    if "hello" in msg or "hi" in msg:
            response = "Hi there!"
    elif "how are you" in msg:
            response = "I'm good, thanks!"
    elif "your name" in msg:
            response = "I'm a simple chatbot"
    elif "bye" in msg:
            response = "Goodbye!"
            self.root.after(1000, self.root.quit)
    else:
            responses = ["Interesting!", "Tell me more", "I see", "Okay"]
            response = random.choice(responses)


    self.display.insert(tk.END, f"You: {user.msg}\n")
    self.display.config(state=tk.DISABLED)
    self.display.see(tk.END)



    self.entry.delete(0, tk.END)


root = tk.Tk()
root.mainloop()