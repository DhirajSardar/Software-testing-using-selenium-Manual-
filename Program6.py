def binary_search(arr, target):
    """
    Searches for the target element in the sorted array using binary search.
    
    Args:
        arr (list): A sorted list of elements.
        target: The element to be searched.
        
    Returns:
        int: The index of the target element if found, None otherwise.
    """
    low = 0  # Initialize the low index to 0
    high = len(arr) - 1  # Initialize the high index to the last element of the array
    
    while low <= high:  # Continue the search until low is less than or equal to high
        mid = (low + high) // 2  # Calculate the middle index
        guess = arr[mid]  # Get the middle element
        
        if guess == target:  # If the middle element is the target, return the index
            return mid
        elif guess < target:  # If the middle element is less than the target, search the right half
            low = mid + 1
        else:  # If the middle element is greater than the target, search the left half
            high = mid - 1
    
    return None  # If the target is not found, return None
# Test cases
arr = [1, 2, 3, 4, 5]

# Test case 1: Target is found in the middle
print("Test case 1:")
print("Array:", arr)
print("Target:", 3)
print("Result:", binary_search(arr, 3))  # Output: 2

# Test case 2: Target is less than the smallest element
print("\nTest case 2:")
print("Array:", arr)
print("Target:", 0)
print("Result:", binary_search(arr, 0))  # Output: None

# Test case 3: Target is greater than the largest element
print("\nTest case 3:")
print("Array:", arr)
print("Target:", 6)
print("Result:", binary_search(arr, 6))  # Output: None

# Test case 4: Empty list
print("\nTest case 4:")
arr = []
print("Array:", arr)
print("Target:", 3)
print("Result:", binary_search(arr, 3))  # Output: None

# Test case 5: List with one element (target is present)
print("\nTest case 5:")
arr = [3]
print("Array:", arr)
print("Target:", 3)
print("Result:", binary_search(arr, 3))  # Output: 0

# Test case 6: List with one element (target is not present)
print("\nTest case 6:")
arr = [3]
print("Array:", arr)
print("Target:", 4)
print("Result:", binary_search(arr, 4))  # Output: None
