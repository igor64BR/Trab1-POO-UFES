import math
import time


class Cronometro:
    def __init__(self) -> None:
        self.tempo_referencia = time.time()

    def get_display_time(self):
        time_spent = self.get_time_spent()

        seconds = time_spent % 60
        minutes = time_spent // 60

        return f"{minutes}:{seconds:02d}"

    def get_time_spent(self, reference_time_in_seconds: int = None) -> int:
        """Returns total time spent in seconds"""
        if reference_time_in_seconds == None:
            reference_time_in_seconds = self.tempo_referencia

        seconds = math.floor(time.time() - reference_time_in_seconds)

        return seconds

    def start_new_reference_time(self):
        return time.time()
