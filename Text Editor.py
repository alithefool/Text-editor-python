import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file(window, text_edit):
    # Load file
    filepath = askopenfilename(filetypes=[("Text Files", ".txt")])
    if not filepath:
        return
    
    text_edit.delete(1.0, tk.END)
    with open(filepath, "r") as f:
        content = f.read()
        text_edit.insert(tk.END, content)
    window.title(f"Open File: {filepath}")

def save_file(window, text_edit):
    # Save file
    filepath = asksaveasfilename(filetypes=[("Text Files", ".txt")])
    if not filepath:
        return
    
    with open(filepath, "w") as f:
        content = text_edit.get(1.0, tk.END)
        f.write(content)
    window.title(f"Open File: {filepath}")

def undo(text_edit):
    try:
        text_edit.edit_undo()
    except tk.TclError:
        pass

def redo(text_edit):
    try:
        text_edit.edit_redo()
    except tk.TclError:
        pass

def main():
    # Run the text editor application
    window = tk.Tk()
    window.title("Text Editor")
    
    frame = tk.Frame(window, bg="#1a1a1a", relief=tk.RAISED, bd=2)
    frame.grid(row=0, column=0, columnspan=4, sticky="ew")

    neon_blue = "#0099FF"

    text_edit = tk.Text(window, font=("Courier New", 12), undo=True,
                        bg="#0d0d0d", fg=neon_blue, insertbackground='white') 
    text_edit.grid(row=1, column=0, columnspan=4, sticky="nsew")

    open_button = tk.Button(frame, text="Open", command=lambda: open_file(window, text_edit),
                             bg="#1a1a1a", fg=neon_blue, activebackground="#1a1a1a", activeforeground=neon_blue)
    open_button.grid(row=0, column=0, padx=2, pady=2)

    save_button = tk.Button(frame, text="Save", command=lambda: save_file(window, text_edit),
                             bg="#1a1a1a", fg=neon_blue, activebackground="#1a1a1a", activeforeground=neon_blue)
    save_button.grid(row=0, column=1, padx=2, pady=2)

    undo_button = tk.Button(frame, text="Undo", command=lambda: undo(text_edit),
                             bg="#1a1a1a", fg=neon_blue, activebackground="#1a1a1a", activeforeground=neon_blue)
    undo_button.grid(row=0, column=2, padx=2, pady=2)

    redo_button = tk.Button(frame, text="Redo", command=lambda: redo(text_edit),
                            bg="#1a1a1a", fg=neon_blue, activebackground="#1a1a1a", activeforeground=neon_blue)
    redo_button.grid(row=0, column=3, padx=2, pady=2)

    window.rowconfigure(1, weight=1)
    window.columnconfigure([0, 1, 2, 3], weight=1)

    window.bind("<Control-s>", lambda x: save_file(window, text_edit))
    window.bind("<Control-o>", lambda x: open_file(window, text_edit))
    window.bind("<Control-z>", lambda x: undo(text_edit))
    window.bind("<Control-y>", lambda x: redo(text_edit))

    window.configure(bg="#0d0d0d")
    window.mainloop()

main()
