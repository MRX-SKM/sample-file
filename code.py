def merge_sort(arr):
    """Recursive function to perform Merge Sort on an array."""
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle of the array
        left_half = arr[:mid]  # Left half
        right_half = arr[mid:]  # Right half

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy any remaining elements from left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copy any remaining elements from right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def print_array(arr):
    """Utility function to print an array."""
    print("Sorted array:", arr)

# Example usage
numbers = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", numbers)
merge_sort(numbers)
print_array(numbers)
