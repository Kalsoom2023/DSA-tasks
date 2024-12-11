# Real-Life Problem: Organizing Books by Height
# Imagine you are organizing a shelf of books in a library, but instead of randomly placing them, you want to arrange them by height, from shortest to tallest. The number of books is quite large, so you want to find an efficient way to do this.

# Solution: Quick Sort
# Quick Sort can be used to solve this problem. Here’s how it works, applied to the task of sorting books by height:

# Choose a pivot book: Start by randomly picking one book on the shelf. This book’s height will be your pivot. You’ll use this book to compare the height of all the other books.

# Partitioning the books:

# Left pile: Place all books shorter than the pivot on the left side of the pivot.
# Right pile: Place all books taller than the pivot on the right side.
# Now, the pivot book is in its correct position. All books on the left are shorter, and all books on the right are taller.

# Recursively apply the process: Now, repeat the same process for both the left and right piles of books. For each pile, choose a new pivot, partition the books, and repeat until all the books are sorted.
def quick_sort(arr):
   
    if len(arr) <= 1:
        return arr
    

    pivot = arr[len(arr) // 2]  
    
   
    left = [x for x in arr if x < pivot]   
    middle = [x for x in arr if x == pivot] 
    right = [x for x in arr if x > pivot]   
    
    return quick_sort(left) + middle + quick_sort(right)


books_by_height = [5, 2, 9, 1, 5, 6, 7, 3]
sorted_books = quick_sort(books_by_height)
print(sorted_books)
