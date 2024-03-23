import requests
import random
import csv

class DatasetGenerator:
    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {'X-RapidAPI-Key': self.api_key}

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
                word = self.get_random_word()
                if word:
                    print(f"Adding word: {word}")
                    current_line.append(word)
                    if len(current_line) == words_per_line:
                        writer.writerow([' '.join(current_line)])
                        current_line = []

            if current_line:
                writer.writerow([' '.join(current_line)])
        print(f'Generated file {file_name} with {num_words} random words')


if __name__ == '__main__':
    api_key = 'd6b34b3690msh3bfcf3525332918p1f0bc7jsn639b9e87f7c7'
    generator = DatasetGenerator(api_key)
    # Generating a CSV file with 100 random words
    generator.generate_csv('random_words_1.csv', 100)
