# Sort
## Selection Sort
Concept: Find minimum variable of the array and put it in front, repeat the process without the numbers already sorted n - 1 times. \
Time Complexity: O(n<sup>2</sup>) \
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
## Insertion Sort
## Merge Sort
## Quick Sort