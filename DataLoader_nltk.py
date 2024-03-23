import random
import os
import nltk

nltk.download('words')
from nltk.corpus import words

class DatasetGenerator:
    def __init__(self, word_list):
        self.word_list = word_list

    def generate_csv(self, file_name, max_file_size):
        with open(file_name, 'w') as file:
            current_size = 0
            while current_size < max_file_size:
                # Generate a line of random words
                line = ' '.join(random.choice(self.word_list) for _ in range(10)) + '\n'
                file.write(line)
                current_size = file.tell()
        print(f'Generated file {file_name} with size {current_size} bytes')


if __name__ == "__main__":
    word_list = words.words()

    generator = DatasetGenerator(word_list)
    # Generating a CSV file with a size of approximately 1KB
    generator.generate_csv('random_words.csv', 1024)
