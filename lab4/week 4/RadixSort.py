import matplotlib.pyplot as plt

def draw_bars(arr, colorArray, pause_time=0.5):
    plt.bar(range(len(arr)), arr, color=colorArray)
  
    for i, value in enumerate(arr):
        plt.text(i, value + 0.1, str(value), ha='center', va='bottom', fontsize=10)

    plt.pause(pause_time)  
    plt.clf() 

def radix_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        draw_bars(output, ['green' if x != 0 else 'blue' for x in output])

    for i in range(n):
        arr[i] = output[i]

def radix_sort_visual(arr):
    max_value = max(arr)
    
    exp = 1
    while max_value // exp > 0:
        radix_sort(arr, exp)
        exp *= 10
    
    draw_bars(arr, ['green'] * len(arr))
    plt.show()


if __name__ == "__main__":
    user_input = input("Enter numbers separated by space: ")
    arr = list(map(int, user_input.split()))
    
    plt.figure()
    plt.title("Radix Sort Visualization")
    plt.xlabel("Index")
    plt.ylabel("Value")
    radix_sort_visual(arr)
