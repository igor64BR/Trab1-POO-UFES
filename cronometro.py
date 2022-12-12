import math
import time


class Cronometro:
    def __init__(self) -> None:
        self.reference_time = time.time()

    def get_display_time(self):
        """Gets the time spent in game to show on the screen"""
        time_spent = self.get_time_spent()

        seconds = time_spent % 60
        minutes = time_spent // 60

        return f"{minutes}:{seconds:02d}"

    def get_time_spent(self, reference_time_in_seconds: int = None) -> int:
        """Returns total time spent in seconds since the given reference time"""
        if reference_time_in_seconds == None:
            reference_time_in_seconds = self.reference_time

        seconds = math.floor(time.time() - reference_time_in_seconds)

        return seconds

    def start_new_reference_time(self):
        """
            Starts and returns an instant time to know the start or end moment 
            of an action
        """
        return time.time()
