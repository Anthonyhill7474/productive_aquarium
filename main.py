import tkinter as tk
from scheduler import start_notifier
import config
from fish import AquariumApp

def create_gui():
    global study_period_entry, start_button
    
    root = tk.Tk()
    config.root = root
    root.title("Procrastination Notifier")

    tk.Label(root, text="Enter Study Period (minutes):").pack(pady=10)
    study_period_entry = tk.Entry(root)
    study_period_entry.pack(pady=10)
    
    start_button = tk.Button(root, text="Start Notifier", command=lambda: start_notifier(study_period_entry, start_button))
    start_button.pack(pady=20)

    config.aquarium_app = AquariumApp(root)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
