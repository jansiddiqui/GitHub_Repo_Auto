import tkinter as tk
from tkinter import PhotoImage, messagebox
import requests
from spellchecker import SpellChecker

spell = SpellChecker()

def create_repository():
    ACCESS_TOKEN = entry_token.get()
    repo_name = entry_name.get()
    repo_description = entry_description.get()
    repo_private = var_private.get()

    headers = {
        'Authorization': f'token {ACCESS_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }

    data = {
        'name': repo_name,
        'description': repo_description,
        'private': repo_private
    }

    response = requests.post('https://api.github.com/user/repos', headers=headers, json=data)

    if response.status_code == 201:
        messagebox.showinfo("Success", "Repository created successfully")
        entry_name.delete(0, tk.END)
        entry_description.delete(0, tk.END)
    else:
        messagebox.showerror("Error", f"Failed to create repository: {response.status_code}\n{response.json()}")

def check_spelling():
    description = entry_description.get()
    misspelled = spell.unknown(description.split())
    if misspelled:
        messagebox.showwarning("Spell Check", f"Potential typos: {', '.join(misspelled)}")
    else:
        messagebox.showinfo("Spell Check", "No spelling errors found!")

root = tk.Tk()
root.title("GitHub Repository Creator")
icon = PhotoImage(file="logo1.png")
root.iconphoto(False, icon)
root.configure(bg='#2c3e50')

frame = tk.Frame(root, bg='#34495e', bd=10)
frame.pack(padx=50, pady=50)

tk.Label(frame, text="Personal Access Token:", bg='#34495e', fg='white').grid(row=0, column=0, padx=10, pady=10)
entry_token = tk.Entry(frame, width=50, show="*")
entry_token.grid(row=0, column=1, padx=10, pady=10)

tk.Label(frame, text="Repository Name:", bg='#34495e', fg='white').grid(row=1, column=0, padx=10, pady=10)
entry_name = tk.Entry(frame, width=50)
entry_name.grid(row=1, column=1, padx=10, pady=10)

tk.Label(frame, text="Repository Description:", bg='#34495e', fg='white').grid(row=2, column=0, padx=10, pady=10)
entry_description = tk.Entry(frame, width=50)
entry_description.grid(row=2, column=1, padx=10, pady=10)

tk.Label(frame, text="Repository Mode:", bg='#34495e', fg='white').grid(row=3, column=0, padx=10, pady=10)
var_private = tk.BooleanVar()
tk.Radiobutton(frame, text="Public", variable=var_private, value=False, bg='#34495e', fg='white', selectcolor='#2980b9', indicatoron=0).grid(row=3, column=1, padx=10, pady=10, sticky='w')
tk.Radiobutton(frame, text="Private", variable=var_private, value=True, bg='#34495e', fg='white', selectcolor='#c0392b', indicatoron=0).grid(row=3, column=1, padx=10, pady=10, sticky='e')

create_button = tk.Button(frame, text="Create Repository", command=create_repository, bg='#16a085', fg='white', padx=10, pady=5)
create_button.grid(row=4, column=1, padx=10, pady=20, sticky='w')

spell_check_button = tk.Button(frame, text="Check Spelling", command=check_spelling, bg='#e74c3c', fg='white', padx=10, pady=5)
spell_check_button.grid(row=4, column=1, padx=10, pady=20, sticky='e')

root.mainloop()
