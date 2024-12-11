import matplotlib.pyplot as plt

def draw_bars(arr, colorArray, pause_time=0.5):
    plt.bar(range(len(arr)), arr, color=colorArray)

  
    for i, value in enumerate(arr):
        plt.text(i, value + 0.1, str(value), ha='center', va='bottom', fontsize=10)

    plt.pause(pause_time)  
    plt.clf() 

def counting_sort_visual(arr):
  
    max_value = max(arr)
   
    count = [0] * (max_value + 1)
    output = [0] * len(arr)
   
    for num in arr:
        count[num] += 1

    colorArray = ['blue'] * len(count)
    for i in range(len(count)):
        colorArray[i] = 'red'  
        draw_bars(count, colorArray)
        colorArray[i] = 'blue'  


    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(count)):
        colorArray[i] = 'yellow'  
        draw_bars(count, colorArray)
        colorArray[i] = 'blue' 

    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

       
        draw_bars(output, ['green' if x != 0 else 'blue' for x in output])

   
    for i in range(len(arr)):
        arr[i] = output[i]

    
    draw_bars(arr, ['green'] * len(arr))
    plt.show()

if __name__ == "__main__":
      user_input = input("Enter numbers separated by space: ")

  
      arr = list(map(int, user_input.split()))

  
      plt.figure()
      plt.title("Insertion Sort Visualization")
      plt.xlabel("Index")
      plt.ylabel("Value")
      counting_sort_visual(arr)