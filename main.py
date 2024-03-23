import threading
from Generator import DatasetGenerator
from memory_manager import MemoryManager

def generate_data(thread_id, generator):
    # Generating CSV of 100 words
    file_name = f'random_words_{thread_id}.csv'
    generator.generate_csv(file_name, 100)
    print(f"Thread {thread_id} finished generating data.")

def main():
    # Create and start multiple threads
    # Number of threads used 5 with 1GB of memory for each
    threads = []
    num_threads = 5
    memory_limit_per_thread = 1024 * 1024 * 1024

    for i in range(num_threads):
        api_key = f'd6b34b3690msh3bfcf3525332918p1f0bc7jsn639b9e87f7c7'
        memory_manager = MemoryManager(memory_limit_per_thread) # Creating separate memory manager for each thread
        generator = DatasetGenerator(api_key, memory_manager)
        thread = threading.Thread(target=generate_data, args=(i, generator))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("All threads finished.")

if __name__ == '__main__':
    main()
