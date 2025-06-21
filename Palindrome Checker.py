import tkinter as tk
from tkinter import messagebox
import re

class PalindromeCheckerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Palindrome Checker")
        self.master.geometry("400x250")

        tk.Label(master, text="Enter text to check:", font=("Arial", 12)).pack(pady=10)

        self.input_entry = tk.Entry(master, font=("Arial", 12), width=30)
        self.input_entry.pack()

        tk.Button(master, text="Check Palindrome", font=("Arial", 12), command=self.check_palindrome).pack(pady=10)

        self.result_label = tk.Label(master, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

    def clean_text(self, text):
        return re.sub(r'[^A-Za-z0-9]', '', text).lower()

    def check_palindrome(self):
        text = self.input_entry.get()
        cleaned = self.clean_text(text)
        if not cleaned:
            self.result_label.config(text="Please enter valid characters.", fg="orange")
            return
        if cleaned == cleaned[::-1]:
            self.result_label.config(text="✅ It's a Palindrome!", fg="green")
        else:
            self.result_label.config(text="❌ Not a Palindrome.", fg="red")

# Run the app
root = tk.Tk()
app = PalindromeCheckerApp(root)
root.mainloop()
