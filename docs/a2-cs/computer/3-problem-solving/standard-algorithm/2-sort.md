# sort

```python
# bubble
def bubbleSort(arr):
    for iteration in range(len(arr)):
        Swap = False
        for index in range(0, len(arr)-1 - iteration):
            if arr[index] > arr[index +1]:
                isSwap = True
                arr[index], arr[index+1] = arr[index+1] , arr[index] # swap in python
        print(iteration)
        if not Swap:
            break # no swap -> ordered -> exit the loop and all the remaining iteration
# insertion
def insertionSort(arr):
    for index in range (1, len(arr))
        key = arr[index]
        j = index - 1
        while arr[j]>key and j>=0:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
```