import time

lst = []
for i in range(1, 101):
    start_time = time.time()
    lst.append(i)
    print(f"Appended {i}: Time Taken = {time.time() - start_time:.10f} seconds")
