import tkinter as tk
from tkinter import messagebox
import random

# ----------------------------
# App Logic
# ----------------------------
TARGET_MIN = 1
TARGET_MAX = 100
random_number = random.randint(TARGET_MIN, TARGET_MAX)
attempts = 0

def check_guess():
    global attempts
    try:
        guess = int(entry.get())
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a number.")
        return

    attempts += 1

    if guess < random_number:
        result_label.config(text="Too low 📉", fg="#e67e22")
    elif guess > random_number:
        result_label.config(text="Too high 📈", fg="#e74c3c")
    else:
        messagebox.showinfo(
            "🎉 You Won!",
            f"Correct! The number was {random_number}.\nAttempts: {attempts}"
        )
        reset_game()


def reset_game():
    global random_number, attempts
    random_number = random.randint(TARGET_MIN, TARGET_MAX)
    attempts = 0
    entry.delete(0, tk.END)
    result_label.config(text="Make a guess!", fg="#2c3e50")

# ----------------------------
# UI Setup
# ----------------------------
root = tk.Tk()
root.title("🎯 Guess the Number")
root.geometry("420x320")
root.configure(bg="#1e272e")

frame = tk.Frame(root, bg="#ecf0f1", bd=0)
frame.place(relx=0.5, rely=0.5, anchor="center", width=360, height=260)

# Title
label_title = tk.Label(
    frame,
    text="Guess the Number",
    font=("Helvetica", 18, "bold"),
    bg="#ecf0f1",
    fg="#2c3e50"
)
label_title.pack(pady=15)

# Instructions
label_info = tk.Label(
    frame,
    text=f"Pick a number between {TARGET_MIN} and {TARGET_MAX}",
    font=("Helvetica", 11),
    bg="#ecf0f1",
    fg="#34495e"
)
label_info.pack()

# Entry
entry = tk.Entry(frame, font=("Helvetica", 14), justify="center")
entry.pack(pady=15)

# Button
button = tk.Button(
    frame,
    text="Check Guess",
    font=("Helvetica", 12, "bold"),
    bg="#3498db",
    fg="white",
    activebackground="#2980b9",
    padx=10,
    command=check_guess
)
button.pack()

# Result label
result_label = tk.Label(
    frame,
    text="Make a guess!",
    font=("Helvetica", 12),
    bg="#ecf0f1",
    fg="#2c3e50"
)
result_label.pack(pady=15)

# Reset button
reset_button = tk.Button(
    frame,
    text="Reset 🔄",
    font=("Helvetica", 10),
    bg="#95a5a6",
    fg="white",
    command=reset_game
)
reset_button.pack()

root.mainloop()
