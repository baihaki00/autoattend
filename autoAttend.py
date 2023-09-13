from tkinter import *
import subprocess
import customtkinter
from tkinter import messagebox
import sys
import os

def get_file_path(filename):
    if getattr(sys, 'frozen', False):
        # The application is frozen (bundled in an executable)
        return os.path.join(sys._MEIPASS, filename)
    else:
        # The application is not frozen
        # Change this line to match where you keep your data files:
        return os.path.join(os.path.dirname(__file__), filename)

# Usage
check_in_path = get_file_path('check_in.py')
check_out_path = get_file_path('check_out.py')
break_start_path = get_file_path('break_start.py')
break_end_path = get_file_path('break_end.py')
loom_start_path = get_file_path('loom_start.py')

# Now use these paths in your code to access the files





# Variable to store the subprocess
current_process = None

def run_subprocess(script_name, label_text):
    global current_process
    try:
        # Check if a previous subprocess is running, and terminate it if necessary
        if current_process and current_process.poll() is None:
            current_process.terminate()
        
        # Run the specified Python script as a subprocess
        current_process = subprocess.Popen(["python", script_name], creationflags=subprocess.CREATE_NO_WINDOW)
        
        # Update the label text
        progress_label.configure(text=label_text)
        
        # Start checking the subprocess status periodically
        check_subprocess_status()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def check_subprocess_status():
    global current_process
    if current_process:
        return_code = current_process.poll()
        if return_code is None:
            # Subprocess is still running
            # Schedule this function to run again after 1000 milliseconds (1 second)
            root.after(1000, check_subprocess_status)
        else:
            # Subprocess has completed
            progress_label.configure(text="Done")

customtkinter.set_appearance_mode("dark")

# Create the main application window
root = customtkinter.CTk()
root.title("AUTOATTEND")
root.geometry("300x500")  # Set the window size to 300x500 pixels
root.resizable(False, False)


coded_by_label = customtkinter.CTkLabel(
    master=root,
    width=20,
    text="// CODED. BAIHAKI",
    font = ("Palatino", 20, "bold")
    
)
coded_by_label.place(relx=0.5, rely=0.1, anchor=CENTER)

desc_label = customtkinter.CTkLabel(
    master=root,
    text="Expecto Petronum! ",
    font = ("Palatino", 12, "italic")
)
desc_label.place(relx=0.5, rely=0.15, anchor=CENTER)

button_check_in = customtkinter.CTkButton(
    master=root,
    width=120,
    height=32,
    border_width=0,
    corner_radius=8,
    text="CHECK IN",
    #command=lambda: run_subprocess("check_in.py", "Checking In...")
    command=lambda: run_subprocess(check_in_path, "Checking In...")
)
button_check_in.place(relx=0.5, rely=0.3, anchor=CENTER)

button_check_out = customtkinter.CTkButton(
    master=root,
    width=120,
    height=32,
    border_width=0,
    corner_radius=8,
    text="CHECK OUT",
    #command=lambda: run_subprocess("check_in.py", "Checking In...")
    command=lambda: run_subprocess(check_out_path, "Checking Out...")
)
button_check_out.place(relx=0.5, rely=0.4, anchor=CENTER)

button_break_start = customtkinter.CTkButton(
    master=root,
    width=120,
    height=32,
    border_width=0,
    corner_radius=8,
    text="BREAK START",
    #command=lambda: run_subprocess("check_in.py", "Checking In...")
    command=lambda: run_subprocess(break_start_path, "Break Time!")
)
button_break_start.place(relx=0.5, rely=0.5, anchor=CENTER)

button_break_end = customtkinter.CTkButton(
    master=root,
    width=120,
    height=32,
    border_width=0,
    corner_radius=8,
    text="BREAK END",
    #command=lambda: run_subprocess("break_end.py", "Break End ;(")
    command=lambda: run_subprocess(break_end_path, "Break End ;(")
)
button_break_end.place(relx=0.5, rely=0.6, anchor=CENTER)

button_start_loom = customtkinter.CTkButton(
    master=root,
    width=120,
    height=32,
    border_width=0,
    corner_radius=8,
    text="START AUTOLOOM",
    #command=lambda: run_subprocess("break_end.py", "Break End ;(")
    command=lambda: run_subprocess(loom_start_path, "Loom Starting...")
)
button_start_loom.place(relx=0.3, rely=0.7, anchor=CENTER)

button_stop_loom = customtkinter.CTkButton(
    master=root,
    width=120,
    height=32,
    border_width=0,
    corner_radius=8,
    text="START AUTOLOOM",
    #command=lambda: run_subprocess("break_end.py", "Break End ;(")
    command=lambda: run_subprocess(loom_start_path.terminate(), "Loom Stopping...")
)
button_stop_loom.place(relx=0.3, rely=0.7, anchor=CENTER)



# You can add more buttons for other functions in a similar manner

progress_label = customtkinter.CTkLabel(
    master=root,
    text="",
    font=("Helvetica", 14)
)
progress_label.place(relx=0.5, rely=0.9, anchor=CENTER)

# Run the Tkinter main loop
root.mainloop()
