import tkinter as tk
from tkinter import PhotoImage
import pygame

pygame.mixer.init()

# Normal Mode sound files
sound_files = {
    "0": "E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/Sounds/keyboard0.wav",
    "1": "E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/Sounds/keyboard1.wav",
    "2": "E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/Sounds/keyboard2.wav",
    "3": "E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/Sounds/keyboard3.wav",
    "4": "E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/Sounds/keyboard4.wav",
    "5": "E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/Sounds/keyboard5.wav",
    "6": "E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/Sounds/keyboard6.wav",
    "7": "E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/Sounds/keyboard7.wav",
    "8": "E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/Sounds/keyboard8.wav",
    "9": "E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/Sounds/keyboard9.wav",
    "meow": "E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/Sounds/meow.wav"
}

# Crazy Mode sound files
crazy_sound_files = {
    "A0": "E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/Crazy_Sounds/Compressed - Meowsic_A0.L - 03.wav",
    "A1": "E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/Crazy_Sounds/Compressed - Meowsic_A1.L - 04.wav",
    "A2": "E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/Crazy_Sounds/Compressed - Meowsic_A2.L - 05.wav",
    "B0": "E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/Crazy_Sounds/Compressed - Meowsic_B0.L - 06.wav",
    "B1": "E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/Crazy_Sounds/Compressed - Meowsic_B1.L - 07.wav",
    "B2": "E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/Crazy_Sounds/Compressed - Meowsic_B2.L - 08.wav",
    "C1": "E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/Crazy_Sounds/Compressed - Meowsic_C1.L - 11.wav",
    "C2": "E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/Crazy_Sounds/Compressed - Meowsic_C2.L - 12.wav",
    "C3": "E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/Crazy_Sounds/Compressed - Meowsic_C3.L - 13.wav",
    "D1": "E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/Crazy_Sounds/Compressed - Meowsic_D1.L - 16.wav",
    "D2": "E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/Crazy_Sounds/Compressed - Meowsic_D2.L - 17.wav",
    "E1": "E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/Crazy_Sounds/Compressed - Meowsic_E1.L - 18.wav",
    "F1": "E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/Crazy_Sounds/Compressed - Meowsic_F1.L - 22.wav",
    "G1": "E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/Crazy_Sounds/Compressed - Meowsic_G1.L - 26.wav",
    "G2": "E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/Crazy_Sounds/Compressed - Meowsic_G2.L - 27.wav"
}

# Initialize pygame sound objects
sounds = {key: pygame.mixer.Sound(file) for key, file in sound_files.items()}
crazy_sounds = {key: pygame.mixer.Sound(file) for key, file in crazy_sound_files.items()}

root = tk.Tk()
root.geometry("800x361")
root.title("Cat Piano")

# Load images for background
original_bg_image = PhotoImage(file="E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/background.png")
alternate_bg_image = PhotoImage(file="E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/alternate_background.png")

# Define functions for Normal Mode
def switch_to_piano():
    main_menu_frame.pack_forget()
    background_label.config(image=original_bg_image)
    piano_frame.pack(fill="both", expand=True)

# Define functions for Crazy Mode
def show_crazy_mode():
    main_menu_frame.pack_forget()
    background_label.config(image=original_bg_image)
    crazy_frame.pack(fill="both", expand=True)
    root.geometry("1250x564")  # Adjust the size of the window for Crazy Mode

def return_to_menu():
    crazy_frame.pack_forget()
    piano_frame.pack_forget()
    main_menu_frame.pack(fill="both", expand=True)

# Create UI for Main Menu
main_menu_frame = tk.Frame(root, bg="black")
main_menu_frame.pack(fill="both", expand=True)

welcome_label = tk.Label(main_menu_frame, text="Welcome to Cat Piano", font=("Arial", 24), bg="black", fg="white")
welcome_label.pack(pady=30)

normal_button = tk.Button(main_menu_frame, text="Normal", font=("Arial", 20), width=10, command=switch_to_piano, bg="black", fg="white")
normal_button.pack(pady=10)

crazy_button = tk.Button(main_menu_frame, text="Crazy", font=("Arial", 20), width=10, command=show_crazy_mode, bg="black", fg="white")
crazy_button.pack(pady=10)

# Create UI for Normal Mode
piano_frame = tk.Frame(root)
background_label = tk.Label(piano_frame, image=original_bg_image)
background_label.place(relwidth=1, relheight=1)

def play_sound(key):
    sound = sounds.get(key)
    if sound:
        pygame.mixer.Sound.play(sound)

def meow():
    background_label.config(image=alternate_bg_image)
    play_sound("meow")
    meow_duration = int(sounds["meow"].get_length() * 1000)
    root.after(meow_duration, restore_background)

def restore_background():
    background_label.config(image=original_bg_image)

def on_key_press(event):
    if event.char in "0123456789":
        play_sound(event.char)
    elif event.char == ' ':
        meow()

root.bind('<KeyPress>', on_key_press)

keyboard_frame = tk.Frame(piano_frame)
keyboard_frame.pack(pady=20)

for i in range(10):
    tk.Button(keyboard_frame, text=str(i), width=10, height=5, command=lambda i=i: play_sound(str(i)), bg="black", fg="white").grid(row=0, column=i)

meow_button = tk.Button(piano_frame, text="Meow", width=20, height=5, command=meow, bg="black", fg="white")
meow_button.pack(pady=20)

back_to_menu_button = tk.Button(piano_frame, text="Back to Menu", font=("Arial", 14), command=return_to_menu, bg="black", fg="white")
back_to_menu_button.pack(pady=10)

crazy_frame = tk.Frame(root)

# Add the background image to the crazy_frame
background_label_crazy = tk.Label(crazy_frame, image=original_bg_image)
background_label_crazy.place(relwidth=1, relheight=1)

crazy_keyboard_frame = tk.Frame(crazy_frame)
crazy_keyboard_frame.pack(pady=20)

# Function to play crazy sounds
def play_crazy_sound(key):
    sound = crazy_sounds.get(key)
    if sound:
        pygame.mixer.Sound.play(sound)

# Create buttons for Crazy Mode
for i, key in enumerate(crazy_sounds):
    tk.Button(crazy_keyboard_frame, text=key, width=10, height=5, command=lambda k=key: play_crazy_sound(k), bg="black", fg="white").grid(row=0, column=i)

# Add back button in Crazy Mode
crazy_back_button = tk.Button(crazy_frame, text="Back to Menu", font=("Arial", 14), command=return_to_menu, bg="black", fg="white")
crazy_back_button.pack(pady=10)


root.mainloop()
pygame.quit()
