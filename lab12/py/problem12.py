nums = [-10, 20, -30, 40, 50]

# Remove negative numbers
nums = [x for x in nums if x >= 0]
print("Without negatives:", nums)

# Find max and min
print("Max:", max(nums), "Min:", min(nums))

# Average
print("Average:", sum(nums) / len(nums))
