import psutil
import os

class MemoryManager:
    def __init__(self, max_memory_usage):
        self.max_memory_usage = max_memory_usage

    def memory_exceeded(self):
        # Resident Set Size( rss ) will give the portion of the processes memory held in RAM
        current_memory_usage = psutil.Process(os.getpid()).memory_info().rss
        return current_memory_usage > self.max_memory_usage
