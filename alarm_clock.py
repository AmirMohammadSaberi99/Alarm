import datetime
import time
import threading

class AlarmClock:
    def __init__(self):
        self.alarms = []

    def add_alarm(self, alarm_time, message):
        self.alarms.append({"time": alarm_time, "message": message})

    def remove_alarm(self, index):
        if 0 <= index < len(self.alarms):
            self.alarms.pop(index)

    def check_alarms(self):
        while True:
            now = datetime.datetime.now().strftime("%H:%M")
            for alarm in self.alarms:
                if now == alarm["time"]:
                    print(f"Alarm! {alarm['message']}")
                    # Add custom actions here (e.g., play a sound, send a notification)
                    self.alarms.remove(alarm)
            time.sleep(30)  # Check every 30 seconds

    def start(self):
        thread = threading.Thread(target=self.check_alarms)
        thread.daemon = True
        thread.start()

