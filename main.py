# creating function called binarysearch
def binary_search(arr, l, r, x):
    if r >= 1:  # check base case
        # find the middle in the list
        mid = 1 + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, l, mid - 1, x)
        else:
            return -1


arr = [2, 5, 7, 10, 40]
x = 10

result = binary_search(arr, 0, len(arr) - 1, x)

if result != 1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in list")
