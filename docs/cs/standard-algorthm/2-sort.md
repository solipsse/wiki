# Sort
## Selection Sort
Concept: Find minimum variable of the array and put it in front, repeat the process without the numbers already sorted n - 1 times. \
Time Complexity: o(n<sup>2</sup>), O(n<sup>2</sup>) \
Stability: Stable \
C implementation
```
void Sort(int arr[],int n){
    //loop n - 1 times
    for(int i = 0; i < n - 1; ++i){
        int min_index = i;

        //find minimum element from i onwards
        for(int j = i + 1; j < n; ++j){
            if(arr[j] < arr[min_index]){
                min_index = j;
            }
        }

        // Swap minimum variable to the ith position
        if (min_idx != i) {
            int temp = arr[i];
            arr[i] = arr[min_idx];
            arr[min_idx] = temp;
        }
    }
}
```
## Bubble Sort
Concept: Pass through the array comparing pairs of adjacent elements, and swapping them if they are  out of order, done n- 1 times or until there are no swaps (whichever comes first). \
Time Complexity: o(n), O(n<sup>2</sup>) \
Stability: Stable \
C Implementation
```
void swap(int* xp, int* yp){
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}
void Sort(int arr[],int n){
    bool swapped;
    for(int i = 0;i < n - 1; ++i){
        swapped = false;
        for (j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(&arr[j], &arr[j + 1]);
                swapped = true;
            }
        }
        if(!swapped)
            break;
    }
}
```
## Insertion Sort
Concept: Start with the second element of the array, compare it with all previous(sorted) elements and insert to put it in its correct position. Repeat lenght - 1 times iterating through each element every time \
Time Complexity: o(n), O(n<sup>2</sup>) \
Stability: Stable  \
C Implementation
```
void Sort(int arr[], int n)
{
    for (int i = 1; i < n; ++i) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            --j;
        }
        arr[j + 1] = key;
    }
}
```
## Merge Sort
## Quick Sort