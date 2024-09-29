import tkinter as tk
from tkinter import PhotoImage
import pygame
import os

pygame.mixer.init()

sound_base_path = "E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/Sounds/"
crazy_sound_base_path = "E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/Crazy_Sounds/"
image_base_path = "E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/"

sound_files = {str(i): os.path.join(sound_base_path, f"keyboard{i}.wav") for i in range(10)}
sound_files["meow"] = os.path.join(sound_base_path, "meow.wav")

crazy_keys = ["A0", "A1", "A2", "B0", "B1", "B2", "C1", "C2", "C3", "D1", "D2", "E1", "F1", "G1", "G2"]
crazy_filenames = [
    "Compressed - Meowsic_A0.L - 03.wav",
    "Compressed - Meowsic_A1.L - 04.wav",
    "Compressed - Meowsic_A2.L - 05.wav",
    "Compressed - Meowsic_B0.L - 06.wav",
    "Compressed - Meowsic_B1.L - 07.wav",
    "Compressed - Meowsic_B2.L - 08.wav",
    "Compressed - Meowsic_C1.L - 11.wav",
    "Compressed - Meowsic_C2.L - 12.wav",
    "Compressed - Meowsic_C3.L - 13.wav",
    "Compressed - Meowsic_D1.L - 16.wav",
    "Compressed - Meowsic_D2.L - 17.wav",
    "Compressed - Meowsic_E1.L - 18.wav",
    "Compressed - Meowsic_F1.L - 22.wav",
    "Compressed - Meowsic_G1.L - 26.wav",
    "Compressed - Meowsic_G2.L - 27.wav",
]
crazy_sound_files = {key: os.path.join(crazy_sound_base_path, filename) for key, filename in zip(crazy_keys, crazy_filenames)}

sounds = {key: pygame.mixer.Sound(file) for key, file in sound_files.items()}
crazy_sounds = {key: pygame.mixer.Sound(file) for key, file in crazy_sound_files.items()}

root = tk.Tk()
root.geometry("800x361")
root.title("Cat Piano")

original_bg_image = PhotoImage(file=os.path.join(image_base_path, "background.png"))
alternate_bg_image = PhotoImage(file=os.path.join(image_base_path, "alternate_background.png"))

main_menu_frame = tk.Frame(root, bg="black")
piano_frame = tk.Frame(root)
crazy_frame = tk.Frame(root)

# Create background labels
background_label = tk.Label(piano_frame, image=original_bg_image)
background_label.place(relwidth=1, relheight=1)

background_label_crazy = tk.Label(crazy_frame, image=original_bg_image)
background_label_crazy.place(relwidth=1, relheight=1)

def switch_to_piano():
    main_menu_frame.pack_forget()
    piano_frame.pack(fill="both", expand=True)
    root.geometry("800x361")

def show_crazy_mode():
    main_menu_frame.pack_forget()
    crazy_frame.pack(fill="both", expand=True)
    root.geometry("1250x564")

def return_to_menu():
    crazy_frame.pack_forget()
    piano_frame.pack_forget()
    main_menu_frame.pack(fill="both", expand=True)
    root.geometry("800x361")

# Main Menu UI
main_menu_frame.pack(fill="both", expand=True)
welcome_label = tk.Label(main_menu_frame, text="Welcome to Cat Piano", font=("Arial", 24), bg="black", fg="white")
welcome_label.pack(pady=30)

normal_button = tk.Button(main_menu_frame, text="Normal", font=("Arial", 20), width=10, command=switch_to_piano, bg="black", fg="white")
normal_button.pack(pady=10)

crazy_button = tk.Button(main_menu_frame, text="Crazy", font=("Arial", 20), width=10, command=show_crazy_mode, bg="black", fg="white")
crazy_button.pack(pady=10)

# Piano UI
def play_sound(key):
    sound = sounds.get(key)
    if sound:
        sound.play()

def meow():
    background_label.config(image=alternate_bg_image)
    play_sound("meow")
    meow_duration = int(sounds["meow"].get_length() * 1000)
    root.after(meow_duration, restore_background)

def restore_background():
    background_label.config(image=original_bg_image)

def on_key_press(event):
    if event.char in sounds:
        play_sound(event.char)
    elif event.char == ' ':
        meow()

root.bind('<KeyPress>', on_key_press)

keyboard_frame = tk.Frame(piano_frame)
keyboard_frame.pack(pady=20)

for i in range(10):
    tk.Button(keyboard_frame, text=str(i), width=10, height=5,
              command=lambda i=i: play_sound(str(i)), bg="black", fg="white").grid(row=0, column=i)

meow_button = tk.Button(piano_frame, text="Meow", width=20, height=5, command=meow, bg="black", fg="white")
meow_button.pack(pady=20)

back_to_menu_button = tk.Button(piano_frame, text="Back to Menu", font=("Arial", 14), command=return_to_menu, bg="black", fg="white")
back_to_menu_button.pack(pady=10)

# Crazy UI
def play_crazy_sound(key):
    sound = crazy_sounds.get(key)
    if sound:
        sound.play()

crazy_keyboard_frame = tk.Frame(crazy_frame)
crazy_keyboard_frame.pack(pady=20)

for i, key in enumerate(crazy_sounds.keys()):
    tk.Button(crazy_keyboard_frame, text=key, width=10, height=5,
              command=lambda k=key: play_crazy_sound(k), bg="black", fg="white").grid(row=0, column=i)

crazy_back_button = tk.Button(crazy_frame, text="Back to Menu", font=("Arial", 14), command=return_to_menu, bg="black", fg="white")
crazy_back_button.pack(pady=10)

root.mainloop()
pygame.quit()
