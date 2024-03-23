import requests
import csv
from memory_manager import MemoryManager

class DatasetGenerator:
    def __init__(self, api_key, memory_manager):
        self.api_key = api_key
        self.headers = {'X-RapidAPI-Key': self.api_key}
        self.memory_manager = memory_manager

    def get_random_word(self):
        url = "https://wordsapiv1.p.rapidapi.com/words/"
        response = requests.get(url + "?random=true", headers=self.headers)
        if response.status_code == 200:
            return response.json()['word']
        else:
            return None

    def generate_csv(self, file_name, num_words, words_per_line=10):
        with open(file_name, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            current_line = []
            for _ in range(num_words):
                # Checking memory usage and stopping data generation if memory usage exceeds
                if self.memory_manager.memory_exceeded():
                    print("Memory usage exceeded limit. Stopping data generation.")
                    break
                word = self.get_random_word()
                if word:
                    current_line.append(word)
                    if len(current_line) == words_per_line:
                        writer.writerow([' '.join(current_line)])
                        current_line = []

            if current_line:
                writer.writerow([' '.join(current_line)])
        print(f'Generated file {file_name} with random words')
