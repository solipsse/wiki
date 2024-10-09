# search

```python
# linear
def linearSearch(arr, key):
    for index, element in enumerate(arr):
        if key == element:
            return index
    return -1

# binary
def iterativeBinarySearch(arr, key):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left+right) // 2
        if key == arr[mid]:
            return mid
        elif key > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1

def recursiveBinarySearch(arr, key, left=0, right=None):
    if right == None:
        right = len(arr) - 1

    if left > right:
        return -1
    mid = (left+right) // 2
    if key == arr[mid]:
        return mid
    elif key > arr[mid]:
        return recursiveBinarySearch(arr, key, mid + 1, right)
    else:
        return recursiveBinarySearch(arr, key, left, mid - 1)
```