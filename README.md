# Cat Piano Project

Welcome to the **Cat Piano** project! This interactive application allows you to play piano sounds with a fun, feline twist. Built using Python's Tkinter library for the graphical user interface (GUI) and Pygame for sound playback, the Cat Piano offers two engaging modes: **Normal** and **Crazy**.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [Credits](#credits)

## Features

- **Normal Mode**:
  - Play piano notes using the number keys (0-9).
  - Special "Meow" sound effect with visual background change.
- **Crazy Mode**:
  - Access a variety of unique cat sounds mapped to custom keys.
- **Interactive GUI**:
  - User-friendly interface with clickable buttons and keyboard support.
- **Visual Effects**:
  - Background image changes dynamically during certain interactions.

## Prerequisites

- **Python 3.x**: Make sure Python is installed on your system.
- **Pygame**: Install the Pygame library for sound playback.
- **Tkinter**: Usually included with Python; used for the GUI.

## Installation

### 1. Clone or Download the Project

Download the project files and ensure they are saved in a directory accessible to your Python environment.

### 2. Install Required Libraries

Open your terminal or command prompt and run:

```bash
pip install pygame
```

### 3. Verify File Paths and Structure

Ensure that the file paths in the script match the locations of your sound and image files. The project uses **relative paths**, so it's important that your directory structure matches the expected layout.

## Usage

### 1. Run the Application

Navigate to the directory containing `cat_piano.py` and execute:

```bash
python cat_piano.py
```

### 2. Navigate the Interface

- **Main Menu**:
  - Choose between "Normal" and "Crazy" modes.
- **Normal Mode**:
  - Click buttons labeled 0-9 or press corresponding number keys to play sounds.
  - Click the "Meow" button or press the spacebar for a special meow sound with visual effects.
- **Crazy Mode**:
  - Click on the custom-labeled buttons to play unique cat sounds.
- **Return to Main Menu**:
  - Click the "Back to Menu" button to return to the main menu from any mode.

## Project Structure

```
CatPianoProject/
├── cat_piano.py
├── Sounds/
│   ├── keyboard0.wav
│   ├── keyboard1.wav
│   ├── keyboard2.wav
│   ├── keyboard3.wav
│   ├── keyboard4.wav
│   ├── keyboard5.wav
│   ├── keyboard6.wav
│   ├── keyboard7.wav
│   ├── keyboard8.wav
│   ├── keyboard9.wav
│   └── meow.wav
├── Crazy_Sounds/
│   ├── Compressed - Meowsic_A0.L - 03.wav
│   ├── Compressed - Meowsic_A1.L - 04.wav
│   ├── Compressed - Meowsic_A2.L - 05.wav
│   ├── Compressed - Meowsic_B0.L - 06.wav
│   ├── Compressed - Meowsic_B1.L - 07.wav
│   ├── Compressed - Meowsic_B2.L - 08.wav
│   ├── Compressed - Meowsic_C1.L - 11.wav
│   ├── Compressed - Meowsic_C2.L - 12.wav
│   ├── Compressed - Meowsic_C3.L - 13.wav
│   ├── Compressed - Meowsic_D1.L - 16.wav
│   ├── Compressed - Meowsic_D2.L - 17.wav
│   ├── Compressed - Meowsic_E1.L - 18.wav
│   ├── Compressed - Meowsic_F1.L - 22.wav
│   ├── Compressed - Meowsic_G1.L - 26.wav
│   └── Compressed - Meowsic_G2.L - 27.wav
└── Images/
    ├── background.png
    └── alternate_background.png
```

**Important**: Ensure that your directory structure matches this layout for the application to locate all required resources.

## Customization

### Changing Sound Files

You can replace the existing `.wav` files with your own sounds. Make sure the filenames remain the same or update the paths in the script accordingly.

### Modifying Key Bindings

To change which keys are associated with sounds:

- **Normal Mode**: Modify the `on_key_press` function and the button commands.
- **Crazy Mode**: Adjust the `crazy_keys` and `crazy_filenames` lists to map new keys to different sounds.

### Updating Images

Replace `background.png` and `alternate_background.png` in the `Images/` directory with your own images if desired.

## Troubleshooting

### Application Not Running

- **Error**: `RuntimeError: Too early to create image: no default root window`
  - **Solution**: Ensure that `root = tk.Tk()` is called before creating any `PhotoImage` objects.
- **File Not Found Errors**:
  - Verify that all sound and image files are in their correct directories.
  - Ensure the directory structure matches the project's expected layout.

### Module Not Found Error

- **Issue**: Missing modules like Pygame.
- **Solution**: Install missing modules using `pip install pygame`.

### Sound Not Playing

- Check that your audio device is functioning properly.
- Ensure sound files are not corrupted and are in the correct format.

### General Tips

- Run the script from the command line to see error messages.
- Double-check that all relative paths are correct and that directories exist.

## Credits

- **Developer**: Your Name or Team Name
- **Acknowledgments**:
  - Pygame community for the sound library.
  - Tkinter documentation for GUI guidelines.
- **Institution**: Pratham College, BCA 3rd Semester, Python Lab Project

---

Enjoy making music with a catty twist!

---

**Note**: Remember to ensure that all sound and image files are in the correct directories relative to `cat_piano.py`. Using relative paths enhances portability and privacy by avoiding exposure of personal directory structures.

---

## Additional Resources

- **Pygame Documentation**: [https://www.pygame.org/docs/](https://www.pygame.org/docs/)
- **Tkinter Documentation**: [https://docs.python.org/3/library/tkinter.html](https://docs.python.org/3/library/tkinter.html)

## License

This project is open-source and available under the [MIT License](LICENSE).

---

Enjoy your musical journey with the Cat Piano!
