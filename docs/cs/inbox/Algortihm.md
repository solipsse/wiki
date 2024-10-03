# Algorithm
## Search
!!! tip
    - linear
    - binary (ordered array only)
        - more performant for large array
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
## Sort

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
!!! note
    performance factor:

    1. initial order
    2. number of item (both of them has complexity: O(n))
# ADT
## Stack
```python exec="1" source="tabbed-left"

```
## Queue

## Linked List

```python exec='1' source='tabbed-left'
# Setup
freeStart = 0
dataStart = -1
```

```python exec='1' source='tabbed-left'
NULL = -1

class Node:
    def __init__(self):
        self.data = None
        self.ptr = None

class LinkedList:
    global NULL
    def __init__(self):
        self.startptr = NULL
        self.freeptr = 0
        self.list = [Node() for _ in range(8)] # can't use * 8 here because it will create 1 instance of node and duplicate them
        for i in range(7):
            self.list[i].ptr = i + 1
        self.list[7].ptr = NULL

    def insert(self, key):
        if self.freeptr == NULL:
            return -1
        nodeptr = self.freeptr
        self.list[nodeptr].data = key
        self.freeptr = self.list[self.freeptr].ptr

        prevptr = NULL
        thisptr = self.startptr
        while thisptr != NULL and key > self.list[thisptr].data:
            prevptr = thisptr
            thisptr = self.list[thisptr].ptr

        if prevptr == NULL:
            self.list[nodeptr].ptr = self.startptr
            self.startptr = nodeptr
            return 0

        self.list[nodeptr].ptr = thisptr
        self.list[prevptr].ptr = nodeptr
        return 0

    def find(self, key):
        thisptr = self.startptr
        while thisptr != NULL and self.list[thisptr].data != key:
            thisptr = self.list[thisptr].ptr
        return thisptr

    def delete(self, key):
        prevptr = NULL
        thisptr = self.startptr
        while thisptr != NULL and self.list[thisptr].data != key:
            prevptr = thisptr
            thisptr = self.list[thisptr].ptr

        if thisptr == NULL:
            return -1

        if thisptr == self.startptr:
            self.startptr  = self.list[self.startptr].ptr
        else:
            self.list[prevptr].ptr = self.list[thisptr].ptr

        self.list[thisptr].ptr = self.freeptr
        self.freeptr = thisptr



```
### Graph

!!! note
    - adjacency matrix: 2D arr, row -> col
        - $+$ easy to work with, adding edge is simple
        - $-$ graph with many nodes with little connection between all node will waste memory space
    - adjacency list: dictionary or set

!!! tip "list >> matrix"
