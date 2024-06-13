import random
import logging
import platform
import subprocess
import schedule
from tkinter import messagebox
import config

# Set up logging,
logging.basicConfig(filename='activity.log', filemode='w', level=logging.DEBUG, format='%(asctime)s - %(message)s')

def show_notification():
    logging.debug("show_notification called")

    messages = [
        "Are you procrastinating?",
        "Time to focus!",
        "Get back to work!",
        "Remember your goals!",
        "Stay productive!"
    ]
    message = random.choice(messages)
    if platform.system() == 'Darwin':  # macOS
        macos_notification(message)
    else:
        try:
            from plyer import notification
            notification.notify(
                title='Procrastination Checker',
                message=message,
                timeout=10  # Duration in seconds for the notification to stay on screen
            )
        except ImportError:
            logging.error("Plyer is not available for notifications")

    # Log the notification
    logging.info(f"Notification shown: {message}")
    
    # Schedule the focus check on the main thread
    config.root.after(0, check_focus)

    # Update the elapsed time
    interval = config.job.interval
    config.elapsed_time += interval

    # Schedule the next notification
    schedule_notifications()

def check_focus():
    response = messagebox.askyesno("Focus Check", "Are you focusing?")

    if response:
        logging.info("User is focusing.")
        config.aquarium_app.add_fish()
        config.aquarium_app.grow_all_fish()
    else:
        logging.info("User is procrastinating.")

def macos_notification(message):
    script = f'display notification "{message}" with title "Procrastination Checker"'
    subprocess.run(["osascript", "-e", script])

def schedule_notifications():
    logging.debug("schedule_notifications called")

    remaining_time = config.study_period - config.elapsed_time
    if remaining_time < 5:
        logging.debug("Remaining time is less than 1 minute, stopping scheduling")
        return

    interval = random.randint(1, min(2, remaining_time))
    logging.debug(f"Scheduling next notification in {interval} minutes")
    logging.debug(f"elapsed time is {config.elapsed_time}")

    if config.job is not None:
        schedule.cancel_job(config.job)

    config.job = schedule.every(interval).minutes.do(show_notification)
    config.job.interval = interval
