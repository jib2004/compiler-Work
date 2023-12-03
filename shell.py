import basic
import tkinter as tk
from tkinter import filedialog
import subprocess

def new_file():
    text_editor.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            text_editor.delete(1.0, tk.END)
            text_editor.insert(tk.END, content)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        content = text_editor.get(1.0, tk.END)
        with open(file_path, 'w') as file:
            file.write(content)

def run_code():

    data = text_editor.get(1.0, tk.END)
    
    result, error = basic.run('<stdin>', data)  # Call the run function from basic.py
    
    text_output.delete(1.0, tk.END)
    if error:
        text_output.insert(tk.END, f"Error: {error}")
    else:
        text_output.insert(tk.END, f"Result: {result}")


root = tk.Tk()
root.title("Code Editor with Runner")

# Text Editor
text_editor = tk.Text(root, wrap="word")
text_editor.pack(expand=True, fill="both")

# Output Box
text_output = tk.Text(root, wrap="word")
text_output.pack(expand=True, fill="both")

# Menu Bar
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)
menu_bar.add_cascade(label="File", menu=file_menu)

run_menu = tk.Menu(menu_bar, tearoff=0)
run_menu.add_command(label="Run", command=run_code)
menu_bar.add_cascade(label="Run", menu=run_menu)

root.config(menu=menu_bar)
root.mainloop()





# while True:
# 	text = input('basic > ')
# 	if text.strip() == "": continue
# 	result, error = basic.run('<stdin>', text)

# 	if error:
# 		print(error.as_string())
# 	elif result:
# 		if len(result.elements) == 1:
# 			print(repr(result.elements[0]))
# 		else:
# 			print(repr(result))