import threading
import main

def run_main():
    main.main()

if __name__ == "__main__":
    count_input = input("How many ^^  :")
    count = int(count_input) if count_input else 10
    threads = []

    for _ in range(count):
        thread = threading.Thread(target=run_main)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()