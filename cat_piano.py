import tkinter as tk
from tkinter import PhotoImage
import pygame
from PIL import Image, ImageTk  # Importing Pillow for image resizing

# Initialize pygame mixer
pygame.mixer.init()

# Load sound files
keyboard0_sound = pygame.mixer.Sound("E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/Sounds/keyboard0.wav")
keyboard1_sound = pygame.mixer.Sound("E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/Sounds/keyboard1.wav")
keyboard2_sound = pygame.mixer.Sound("E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/Sounds/keyboard2.wav")
keyboard3_sound = pygame.mixer.Sound("E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/Sounds/keyboard3.wav")
keyboard4_sound = pygame.mixer.Sound("E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/Sounds/keyboard4.wav")
keyboard5_sound = pygame.mixer.Sound("E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/Sounds/keyboard5.wav")
keyboard6_sound = pygame.mixer.Sound("E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/Sounds/keyboard6.wav")
keyboard7_sound = pygame.mixer.Sound("E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/Sounds/keyboard7.wav")
keyboard8_sound = pygame.mixer.Sound("E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/Sounds/keyboard8.wav")
keyboard9_sound = pygame.mixer.Sound("E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/Sounds/keyboard9.wav")
meow_sound = pygame.mixer.Sound("E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/Sounds/meow.wav")

# Create root window
root = tk.Tk()
root.geometry("800x361")  # Set the window size to 800x361 pixels
root.title("Cat Piano")  # Set the title of the window

# Load the original background image
original_bg_image = PhotoImage(file="E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/background.png")

# Load and resize the alternate background image using Pillow
alternate_image_path = "E:/Pratham College/BCA 3RD SEM/PYTHON/LAB/Project/alternate_background.png"
alternate_img = Image.open(alternate_image_path)  # Open the image using Pillow
alternate_img = alternate_img.resize((800, 361), Image.LANCZOS)  # Resize to 800x361
alternate_bg_image = ImageTk.PhotoImage(alternate_img)  # Convert it to ImageTk for tkinter

# Set initial background
background_label = tk.Label(root, image=original_bg_image)
background_label.place(relwidth=1, relheight=1)

# Play sound function
def play_sound(sound):
    pygame.mixer.Sound.play(sound)

# Meow function with background change
def meow():
    # Change background to alternate image
    background_label.config(image=alternate_bg_image)
    
    # Play the meow sound
    play_sound(meow_sound)

    # Get the length of the meow sound in milliseconds and schedule the background change back to original
    meow_duration = int(meow_sound.get_length() * 1000)
    root.after(meow_duration, restore_background)

# Restore original background function
def restore_background():
    background_label.config(image=original_bg_image)

# Handle keyboard press events
def on_key_press(event):
    if event.char == '1':
        play_sound(keyboard1_sound)
    elif event.char == '2':
        play_sound(keyboard2_sound)
    elif event.char == '3':
        play_sound(keyboard3_sound)
    elif event.char == '4':
        play_sound(keyboard4_sound)
    elif event.char == '5':
        play_sound(keyboard5_sound)
    elif event.char == '6':
        play_sound(keyboard6_sound)
    elif event.char == '7':
        play_sound(keyboard7_sound)
    elif event.char == '8':
        play_sound(keyboard8_sound)
    elif event.char == '9':
        play_sound(keyboard9_sound)
    elif event.char == '0':
        play_sound(keyboard0_sound)
    elif event.char == ' ':
        meow()

root.bind('<KeyPress>', on_key_press)

# Create a frame for the keyboard buttons
frame = tk.Frame(root)
frame.pack(pady=20)

# Create black piano key buttons with white text
button_width = 10  # Adjust width of the buttons
button_height = 5  # Adjust height of the buttons

button0 = tk.Button(frame, text="0", width=button_width, height=button_height, command=lambda: play_sound(keyboard0_sound), bg="black", fg="white")
button0.grid(row=0, column=0)
button1 = tk.Button(frame, text="1", width=button_width, height=button_height, command=lambda: play_sound(keyboard1_sound), bg="black", fg="white")
button1.grid(row=0, column=1)
button2 = tk.Button(frame, text="2", width=button_width, height=button_height, command=lambda: play_sound(keyboard2_sound), bg="black", fg="white")
button2.grid(row=0, column=2)
button3 = tk.Button(frame, text="3", width=button_width, height=button_height, command=lambda: play_sound(keyboard3_sound), bg="black", fg="white")
button3.grid(row=0, column=3)
button4 = tk.Button(frame, text="4", width=button_width, height=button_height, command=lambda: play_sound(keyboard4_sound), bg="black", fg="white")
button4.grid(row=0, column=4)
button5 = tk.Button(frame, text="5", width=button_width, height=button_height, command=lambda: play_sound(keyboard5_sound), bg="black", fg="white")
button5.grid(row=0, column=5)
button6 = tk.Button(frame, text="6", width=button_width, height=button_height, command=lambda: play_sound(keyboard6_sound), bg="black", fg="white")
button6.grid(row=0, column=6)
button7 = tk.Button(frame, text="7", width=button_width, height=button_height, command=lambda: play_sound(keyboard7_sound), bg="black", fg="white")
button7.grid(row=0, column=7)
button8 = tk.Button(frame, text="8", width=button_width, height=button_height, command=lambda: play_sound(keyboard8_sound), bg="black", fg="white")
button8.grid(row=0, column=8)
button9 = tk.Button(frame, text="9", width=button_width, height=button_height, command=lambda: play_sound(keyboard9_sound), bg="black", fg="white")
button9.grid(row=0, column=9)

# Add the Meow button centered below the keyboard buttons
meow_button = tk.Button(root, text="Meow", width=20, height=button_height, command=meow, bg="black", fg="white")
meow_button.pack(pady=20)

# Run the tkinter main loop
root.mainloop()

# Quit pygame when done
pygame.quit()
