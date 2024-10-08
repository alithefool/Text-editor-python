Text Editor - Python (Tkinter)
Overview

This project is a simple text editor built using Python's Tkinter library. It allows users to open, edit, and save text files, with additional features such as undo and redo. The editor features a minimalistic, dark-themed user interface with customizable shortcuts for quick actions.
Features

    Open Files: Load text files (.txt) into the editor.
    Save Files: Save edited text back to .txt files.
    Undo/Redo: Supports undo and redo functionality.
    Keyboard Shortcuts:
        Ctrl+O: Open a file.
        Ctrl+S: Save a file.
        Ctrl+Z: Undo the last action.
        Ctrl+Y: Redo the last undone action.

Components
Graphical Interface

    Text Area:
        A large, editable text field for entering and editing text.
        Supports syntax highlighting with neon blue text on a dark background.
        Undo/Redo functionality is enabled by default.
    Buttons:
        Open: Opens a file dialog to select and load a text file.
        Save: Saves the current content of the editor into a file.
        Undo: Reverses the last action.
        Redo: Restores the last undone action.

Color Scheme

The text editor uses a dark mode interface:

    Background color: #0d0d0d (very dark gray).
    Text color: #0099FF (neon blue).
    Button background: #1a1a1a (dark gray).
    Button text: Neon blue to maintain visual consistency.

Key Functions

    Open File:
        The open_file function allows users to load a .txt file into the editor. The text area is cleared and filled with the file's content. The window title updates to reflect the opened file.

    Save File:
        The save_file function opens a save dialog and writes the current text from the editor into a .txt file.

    Undo/Redo:
        undo and redo functions allow users to revert changes or redo undone actions within the text area. The editor uses the built-in edit_undo and edit_redo capabilities of Tkinter.

Keyboard Shortcuts

The editor supports commonly used keyboard shortcuts:

    Ctrl+O: Open a file.
    Ctrl+S: Save the current file.
    Ctrl+Z: Undo the last action.
    Ctrl+Y: Redo the last undone action. (CURRENTLY BUGGED ON DEBIAN)


Code Structure

    Main Function:
        Initializes the main Tkinter window and sets up the layout with text fields and buttons.
        Defines the grid layout and binds keyboard shortcuts to their respective functions.

    Core Functions:
        open_file: Opens a .txt file and loads its content into the text editor.
        save_file: Saves the current content to a .txt file.
        undo: Reverts the last action in the text area.
        redo: Re-applies the last undone action.

How to Run

    Prerequisites:
        Ensure that you have Python 3.x installed.
        The Tkinter library is part of the Python Standard Library, so no additional installation is needed.

    Running the Application:
        Simply run the text_editor.py file using any Python environment:

        python text_editor.py

The text editor will launch, and you can begin editing or opening text files.
