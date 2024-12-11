import matplotlib.pyplot as plt
import numpy as np

def draw_bars(arr, colorArray, pause_time=0.5):
    plt.bar(range(len(arr)), arr, color=colorArray)
  
    for i, value in enumerate(arr):
        plt.text(i, value + 0.1, str(value), ha='center', va='bottom', fontsize=10)

    plt.pause(pause_time)  
    plt.clf() 

def bucket_sort_visual(arr):
    max_value = max(arr)
    num_buckets = len(arr) // 5 + 1  
    buckets = [[] for _ in range(num_buckets)]

  
    for value in arr:
        index = value * num_buckets // (max_value + 1) 
        buckets[index].append(value)

    
    for i, bucket in enumerate(buckets):
        bucket.sort()
        colorArray = ['blue'] * len(bucket)
        draw_bars(bucket, colorArray)
        colorArray = ['red'] * len(bucket)
        draw_bars(bucket, colorArray)

   
    index = 0
    for bucket in buckets:
        for value in bucket:
            arr[index] = value
            index += 1
            draw_bars(arr, ['green' if x != 0 else 'blue' for x in arr])
    
    draw_bars(arr, ['green'] * len(arr))
    plt.show()


if __name__ == "__main__":
    user_input = input("Enter numbers separated by space: ")
    arr = list(map(int, user_input.split()))
    
    plt.figure()
    plt.title("Bucket Sort Visualization")
    plt.xlabel("Index")
    plt.ylabel("Value")
    bucket_sort_visual(arr)
