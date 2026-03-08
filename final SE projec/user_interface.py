import tkinter as tk
import pyperclip
import password_generator

# ----------------------------
# Functions
def toggle(button, var):
    if var.get():
        var.set(False)
        button.config(bg="#44475a", fg="white")
    else:
        var.set(True)
        button.config(bg="#2bd1fc", fg="black")

def generate():
    try:
        length = int(length_entry.get())
        password = password_generator.generate_password(
            length,
            upper_var.get(),
            lower_var.get(),
            number_var.get(),
            symbol_var.get(),
            exclude_var.get()
        )

        password_var.set(password)
        strength = password_generator.check_strength(password)

        if strength == "Weak":
            strength_label.config(text="Strength: WEAK", fg="#ff3b3b")
        elif strength == "Moderate":
            strength_label.config(text="Strength: MODERATE", fg="#ff9f1c")
        elif strength == "Strong":
            strength_label.config(text="Strength: STRONG", fg="#2ec4b6")

    except:
        strength_label.config(text="Enter valid length", fg="white")

def copy_password():
    pyperclip.copy(password_var.get())
    strength_label.config(text="Password Copied!", fg="#2ec4b6")


# ----------------------------
# Window
root = tk.Tk()
root.title("Secure Password Generator")
root.geometry("700x550")
root.resizable(True, True)

# ----------------------------
# Center Frame
main_frame = tk.Frame(root)
main_frame.place(relx=0.5, rely=0.5, anchor="center")

# ----------------------------
# Background
bg_image = tk.PhotoImage(file=r"C:\Users\Admin\Desktop\final SE projec\background.png")

background_label = tk.Label(root, image=bg_image)
background_label.place(relwidth=1, relheight=1)

canvas = tk.Canvas(main_frame, width=700, height=550, highlightthickness=0)
canvas.pack()

canvas.create_image(0, 0, image=bg_image, anchor="nw")

# ----------------------------
# Title
title = tk.Label(
    root,
    text="SECURE PASSWORD GENERATOR",
    font=("Segoe UI", 26, "bold"),
    bg="black",
    fg="white"
)

canvas.create_window(350, 60, window=title)

# ----------------------------
# Password Length
length_label = tk.Label(
    root,
    text="PASSWORD LENGTH",
    font=("Segoe UI", 15, "bold"),
    bg="black",
    fg="white"
)

canvas.create_window(240, 140, window=length_label)

length_entry = tk.Entry(
    root,
    font=("Segoe UI", 16, "bold"),
    width=6,
    justify="center"
)

canvas.create_window(420, 140, window=length_entry)

# ----------------------------
# Variables
upper_var = tk.BooleanVar()
lower_var = tk.BooleanVar()
number_var = tk.BooleanVar()
symbol_var = tk.BooleanVar()
exclude_var = tk.BooleanVar()

# ----------------------------
# Toggle Buttons
def create_toggle(text, x, y, var):
    btn = tk.Button(
        root,
        text=text,
        font=("Segoe UI", 13, "bold"),
        bg="#44475a",
        fg="white",
        width=16,
        relief="flat",
        command=lambda: toggle(btn, var)
    )

    canvas.create_window(x, y, window=btn)
    return btn


create_toggle("Uppercase", 200, 230, upper_var)
create_toggle("Lowercase", 500, 230, lower_var)

create_toggle("Numbers", 200, 290, number_var)
create_toggle("Symbols", 500, 290, symbol_var)

create_toggle("Exclude Ambiguous", 350, 350, exclude_var)

# ----------------------------
# Generate Button
generate_btn = tk.Button(
    root,
    text="Generate Password",
    font=("Segoe UI", 15, "bold"),
    bg="#00e5ff",
    fg="black",
    width=20,
    command=generate
)

canvas.create_window(350, 410, window=generate_btn)

# ----------------------------
# Password Output
password_var = tk.StringVar()

password_box = tk.Entry(
    root,
    textvariable=password_var,
    font=("Consolas", 18, "bold"),
    width=24,
    justify="center"
)

canvas.create_window(320, 460, window=password_box)

# ----------------------------
# Copy Button
copy_btn = tk.Button(
    root,
    text="Copy Password",
    font=("Segoe UI", 13, "bold"),
    bg="#ffb703",
    fg="black",
    width=15,
    command=copy_password
)

canvas.create_window(580, 460, window=copy_btn)

# ----------------------------
# Strength Label
strength_label = tk.Label(
    root,
    text="Strength:",
    font=("Segoe UI", 14, "bold"),
    bg="black",
    fg="white"
)

canvas.create_window(350, 505, window=strength_label)

root.mainloop()