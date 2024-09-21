import tkinter as tk
from tkinter import PhotoImage
import pygame

pygame.mixer.init()

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

sounds = {key: pygame.mixer.Sound(file) for key, file in sound_files.items()}

root = tk.Tk()
root.geometry("800x361")
root.title("Cat Piano")

original_bg_image = PhotoImage(file="E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/background.png")
alternate_bg_image = PhotoImage(file="E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/alternate_background.png")

def switch_to_piano():
    main_menu_frame.pack_forget()
    background_label.config(image=original_bg_image)
    piano_frame.pack(fill="both", expand=True)

def show_crazy_mode():
    main_menu_frame.pack_forget()
    crazy_frame.pack(fill="both", expand=True)

def return_to_menu():
    crazy_frame.pack_forget()
    piano_frame.pack_forget()
    main_menu_frame.pack(fill="both", expand=True)

main_menu_frame = tk.Frame(root, bg="black")
main_menu_frame.pack(fill="both", expand=True)

welcome_label = tk.Label(main_menu_frame, text="Welcome to Cat Piano", font=("Arial", 24), bg="black", fg="white")
welcome_label.pack(pady=30)

normal_button = tk.Button(main_menu_frame, text="Normal", font=("Arial", 20), width=10, command=switch_to_piano, bg="black", fg="white")
normal_button.pack(pady=10)

crazy_button = tk.Button(main_menu_frame, text="Crazy", font=("Arial", 20), width=10, command=show_crazy_mode, bg="black", fg="white")
crazy_button.pack(pady=10)

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

crazy_frame = tk.Frame(root, bg="black")
crazy_label = tk.Label(crazy_frame, text="Crazy Mode - Coming Soon", font=("Arial", 24), fg="red", bg="black")
crazy_label.pack(pady=100)

crazy_back_button = tk.Button(crazy_frame, text="Back to Menu", font=("Arial", 14), command=return_to_menu, bg="black", fg="white")
crazy_back_button.pack(pady=10)

root.mainloop()
pygame.quit()
