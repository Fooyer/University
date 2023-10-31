import time

# Word to ASCII conversion function (unchanged)
def word_to_ascii_list(word):
    return [ord(char) for char in word]

# Counting sort for words (unchanged)
def counting_sort_for_words(words):
    ascii_values = [word_to_ascii_list(word) for word in words]
    sorted_words = [word for _, word in sorted(zip(ascii_values, words))]
    return sorted_words

# Counting sort (unchanged)
def counting_sort(arr):
    start_time = time.time()
    
    if isinstance(arr[0], str):
        sorted_values = counting_sort_for_words(arr)
    else:
        max_val = max(arr)
        min_val = min(arr)
        count = [0] * (max_val - min_val + 1)
        for num in arr:
            count[num - min_val] += 1
        i = 0
        for j in range(len(count)):
            while count[j] > 0:
                arr[i] = j + min_val
                i += 1
                count[j] -= 1
        sorted_values = arr
        
    end_time = time.time()
    return sorted_values, end_time - start_time

# Quick sort implementation
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def read_and_sort_with_prints(filename):
    with open(filename, 'r') as file:
        values = [line.strip() for line in file]
    
    try:
        values = [int(val) for val in values]
    except ValueError:
        pass
    
    # Counting Sort
    sorted_values_counting, elapsed_time_counting = counting_sort(values.copy())
    print(f"File {filename} sorted using Counting Sort in {elapsed_time_counting:.5f} seconds!")
    
    # QuickSort
    start_time = time.time()
    sorted_values_quick = quick_sort(values.copy())
    elapsed_time_quick = time.time() - start_time
    print(f"File {filename} sorted using QuickSort in {elapsed_time_quick:.5f} seconds!")
    print("-" * 50)
    
    with open(filename, 'w') as file:
        for value in sorted_values_counting:
            file.write(str(value) + '\n')


# List of filenames (unchanged)
filenames = ["1000valores.txt", "10000valores.txt", "100000valores.txt", "1000words.txt", "10000words.txt", "100000words.txt"]

# Note: Since I don't have access to these files, I can't run the function. But this should give you the idea.
# Please run the following lines in your local environment:
for filename in filenames:
     read_and_sort_with_prints(filename)

# Return the modified functions for review
"Functions modified and added successfully!"
