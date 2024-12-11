import time

def main():
    numbers = []
    times = []

    for i in range(1, 101):
        start_time = time.time()  # Start time
        numbers.append(i)  # Append integer to the list
        end_time = time.time()  # End time
        
        elapsed_time = end_time - start_time
        times.append(elapsed_time)
        print(f"Appended {i}: Time taken = {elapsed_time:.10f} seconds")

    print("\nSummary of append times:")
    for index, elapsed_time in enumerate(times, start=1):
        print(f"Appending {index}: {elapsed_time:.10f} seconds")

if __name__ == "__main__":
    main()
