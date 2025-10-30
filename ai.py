import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# -------------------------------
# 1️⃣ Quiz Data
# -------------------------------
questions = [
    {
        "question": "How do you spend your weekends?",
        "options": ["😴 Chill at home", "💼 Focus on goals", "🎉 Hang with friends", "🎨 Creative projects"],
        "types": ["Chill Saurabh", "Focused Saurabh", "Savage Saurabh", "Creative Saurabh"]
    },
    {
        "question": "What motivates you the most?",
        "options": ["🏆 Success", "🧘 Peace", "💘 Love", "⚡ Challenges"],
        "types": ["Focused Saurabh", "Chill Saurabh", "Romantic Saurabh", "Savage Saurabh"]
    },
    {
        "question": "How would friends describe you?",
        "options": ["😎 Relaxed", "🔥 Determined", "😂 Funny", "💞 Loyal"],
        "types": ["Chill Saurabh", "Focused Saurabh", "Savage Saurabh", "Romantic Saurabh"]
    },
    {
        "question": "Your secret superpower is?",
        "options": ["🧠 Genius mind", "💪 Strength", "💖 Love power", "😏 Saurabh swag"],
        "types": ["Creative Saurabh", "Focused Saurabh", "Romantic Saurabh", "Savage Saurabh"]
    }
]

personality_images = {
    "Chill Saurabh": "chill.png",
    "Focused Saurabh": "focused.png",
    "Savage Saurabh": "savage.png",
    "Romantic Saurabh": "romantic.png",
    "Creative Saurabh": "creative.png"
}

# -------------------------------
# 2️⃣ Application Class
# -------------------------------
class SaurabhQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Which Saurabh Are You? 💫")
        self.root.geometry("600x400")
        self.root.config(bg="#FFDDC1")

        self.current_q = 0
        self.answers = []

        # Question label
        self.question_label = tk.Label(root, text="", wraplength=550, font=("Comic Sans MS", 16), bg="#FFDDC1")
        self.question_label.pack(pady=30)

        # Option buttons
        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(root, text="", width=30, font=("Arial", 14), bg="#FFFFFF",
                            command=lambda i=i: self.select_option(i))
            btn.pack(pady=8)
            self.option_buttons.append(btn)

        # Image label
        self.img_label = tk.Label(root, bg="#FFDDC1")
        self.img_label.pack(pady=10)

        # Start first question
        self.show_question(self.current_q)

    # Handle option click
    def select_option(self, index):
        self.answers.append(questions[self.current_q]["types"][index])
        self.current_q += 1
        if self.current_q < len(questions):
            self.show_question(self.current_q)
        else:
            self.show_result()

    # Show question
    def show_question(self, q_index):
        self.question_label.config(text=questions[q_index]["question"])
        for i, btn in enumerate(self.option_buttons):
            btn.config(text=questions[q_index]["options"][i])
        # Random background color
        colors = ["#FFDDC1", "#C1FFD7", "#C1D4FF", "#FFE1C1"]
        self.root.config(bg=random.choice(colors))

    # Show result
    def show_result(self):
        result = max(set(self.answers), key=self.answers.count)
        message = self.get_result_message(result)

        # Show message
        messagebox.showinfo("Your Saurabh Type", message)

        # Show image if available
        if result in personality_images:
            img_path = personality_images[result]
            try:
                img = Image.open(img_path)
                img = img.resize((200, 200))
                img_tk = ImageTk.PhotoImage(img)
                self.img_label.config(image=img_tk)
                self.img_label.image = img_tk
            except FileNotFoundError:
                print(f"Image {img_path} not found!")

        self.root.destroy()

    # Personality messages
    @staticmethod
    def get_result_message(result):
        messages = {
            "Chill Saurabh": "You are Chill Saurabh 😎 — relaxed, calm, and everyone loves your vibes!",
            "Focused Saurabh": "You are Focused Saurabh 🔥 — driven, ambitious, unstoppable!",
            "Savage Saurabh": "You are Savage Saurabh 🧨 — witty, bold, and unforgettable!",
            "Romantic Saurabh": "You are Romantic Saurabh 💘 — loyal, loving, and full of heart!",
            "Creative Saurabh": "You are Creative Saurabh 🎨 — your imagination knows no limits!"
        }
        return messages.get(result, "You are unique like Saurabh! 😎")

# -------------------------------
# 3️⃣ Run Application
# -------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = SaurabhQuiz(root)
    root.mainloop()