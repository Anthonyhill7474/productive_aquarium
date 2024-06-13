import tkinter as tk
from tkinter import messagebox
from scheduler import start_notifier
import config
from fish import aquarium_app
import notifier

def create_gui():
    global study_period_entry, start_button
    
    notifier.root = tk.Tk()  # Set the root in notifier to the Tkinter main window
    notifier.root.title("Procrastination Notifier")

    tk.Label(notifier.root, text="Enter Study Period (minutes):").pack(pady=10)
    study_period_entry = tk.Entry(notifier.root)
    study_period_entry.pack(pady=10)
    
    start_button = tk.Button(notifier.root, text="Start Notifier", command=set_study_period_and_start)
    start_button.pack(pady=20)

    notifier.root.mainloop()

def set_study_period_and_start():
    try:
        period_str = study_period_entry.get()  # Call the method to get the value
        print(f"Study period entered: {period_str}")  # Debugging output
        config.study_period = int(period_str)
        start_notifier()
    except ValueError as e:
        print(f"Error: {e}")  # Debugging output
        messagebox.showerror("Invalid Input", "Please enter a valid number for the study period.")