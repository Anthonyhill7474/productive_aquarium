import schedule
import time
import threading
import tkinter as tk
from tkinter import messagebox
import config
from notifier import schedule_notifications

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(2)

def start_notifier(study_period_entry, start_button):
    try:
        config.study_period = int(study_period_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the study period.")
        return
    
    config.elapsed_time = 0
    schedule_notifications()
    start_button.config(state=tk.DISABLED)
    threading.Thread(target=run_scheduler).start()