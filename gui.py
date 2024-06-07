import tkinter as tk
from tkinter import messagebox
from alarm_clock import AlarmClock
import time  # Import the time module

class AlarmClockGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Alarm Clock")
        self.alarm_clock = AlarmClock()
        self.alarm_clock.start()
        self.create_widgets()

    def create_widgets(self):
        self.time_label = tk.Label(self.root, text="Set Alarm (HH:MM):")
        self.time_label.grid(row=0, column=0, padx=10, pady=10)

        self.time_entry = tk.Entry(self.root)
        self.time_entry.grid(row=0, column=1, padx=10, pady=10)

        self.message_label = tk.Label(self.root, text="Message:")
        self.message_label.grid(row=1, column=0, padx=10, pady=10)

        self.message_entry = tk.Entry(self.root)
        self.message_entry.grid(row=1, column=1, padx=10, pady=10)

        self.set_button = tk.Button(self.root, text="Set Alarm", command=self.set_alarm)
        self.set_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.alarms_listbox = tk.Listbox(self.root, width=50)
        self.alarms_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.remove_button = tk.Button(self.root, text="Remove Alarm", command=self.remove_alarm)
        self.remove_button.grid(row=4, column=0, columnspan=2, pady=10)

    def set_alarm(self):
        alarm_time = self.time_entry.get().strip()
        message = self.message_entry.get().strip()
        if self.validate_time(alarm_time):
            self.alarm_clock.add_alarm(alarm_time, message)
            self.alarms_listbox.insert(tk.END, f"{alarm_time} - {message}")
            self.time_entry.delete(0, tk.END)
            self.message_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Invalid Time Format", "Please enter the time in HH:MM format")

    def remove_alarm(self):
        selected_alarm_index = self.alarms_listbox.curselection()
        if selected_alarm_index:
            index = selected_alarm_index[0]
            self.alarms_listbox.delete(index)
            self.alarm_clock.remove_alarm(index)
        else:
            messagebox.showerror("No Selection", "Please select an alarm to remove")

    def validate_time(self, time_str):
        try:
            time.strptime(time_str, "%H:%M")
            return True
        except ValueError:
            return False

if __name__ == "__main__":
    root = tk.Tk()
    gui = AlarmClockGUI(root)
    root.mainloop()

