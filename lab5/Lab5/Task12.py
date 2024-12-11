def removenegatives(numbers):
    return [num for num in numbers if num >= 0]

def find_max_min(numbers):
    if not numbers:
        return None, None
    return max(numbers), min(numbers)

def findaverage(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def main():
    numbers = [0, -4, 1, -2, 7, 2, -6, 4, 8, 18]

    print("Original list:", numbers)

    numbers = removenegatives(numbers)
    print("After removing negatives:", numbers)

    max_value, min_value = find_max_min(numbers)
    print("Maximum value:", max_value)
    print("Minimum value:", min_value)

    average = findaverage(numbers)
    print("Average value:", average)

if __name__ == "__main__":
    main()
