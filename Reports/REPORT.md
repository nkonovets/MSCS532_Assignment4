# Assignment 4: Heap Data Structures: Implementation, Analysis, and Applications

## Part 1: Heapsort

### Implementation

For this assignment, I implemented a file structure to make implementation, testing, and comparison easier, and transferred recorder.py, merge_sort.py, quick_sort_random.py, and main.py from the previous assignment. To implement heap sort, I created heap_sort.py, which reads data from the data folder, similar to my previous assignment submissions. heap_sort.py is made so that every smaller number is sifted down until it becomes a child of the last available parent. This way, the largest number becomes the root (index 0). After the initial run, the function swaps the root with the last number in the heap, so the largest number moves to the end of the list, where it stays, and then calls siftDown() on the new root to fix the heap again. Every time, the heap becomes one number smaller, and this repeats until the whole list is sorted.

### Analysis

Building the heap takes O(n) time. Even though siftDown() is called on about half of the numbers in the list, most of them are close to the bottom of the heap and can only move down one or two levels, and only a few numbers at the top can move all the way down.

After the initial heap is built, the function extracts n - 1 numbers and calls siftDown() on the new root number. Because the height of the heap is calculated as log n, every extraction costs O(log n) and therefore, all extractions together on the set of n numbers take O(n log n), which also means that, unlike random-pivot quicksort, where its worst, best, and average case are almost always different, which depends on where the pivot was taken, heap sort’s worst, best, and average cases are the same. Thus, the order of input(e.g., sorted, random, reverse sorted) does not really matter for heap sort, because every time the root is swapped with the last number, a small number ends up at the top, and it almost always has to go all the way back down.

As for space, heapsort sorts the list in place, so it only needs O(1) extra space for a couple of variables. Also, I wrote siftDown() with a while loop instead of recursion, so it does not use extra stack space.

### Comparison

I ran heap sort, merge sort, and my random-pivot quicksort from the last assignment on random, sorted, and reverse-sorted lists with 1,000, 10,000, and 50,000 numbers, and recorded the time and memory with recorder.py, the same way as in my previous assignments.

Even though both heap sort and quicksort are O(n log n), heap sort was much slower in every case. At 50,000 numbers, heap sort took around 99–116 ms, while quicksort took 51–61 ms and merge sort took 54–73 ms, so quicksort and merge sort were close to each other, and both were clearly faster than heap sort. This is because heap sort keeps jumping between a parent and its children, who are far apart in the list, and makes many swaps. On the other hand, heap sort took nearly the same time across all input types, which aligns with my analysis that the order of the input does not matter for heap sort.

Heap sort showed 781 KB of memory, but this comes from my heap_sort_in_place() function, which copies the list so recorder.py can work with it, not from heap sort itself.

| Input          |      n | Heap Sort Memory (KB) | Heap Sort Time (ms) | Merge Sort Memory (KB) | Merge Sort Time (ms) | Quick Sort Random Memory (KB) | Quick Sort Random Time (ms) |
| -------------- | -----: | --------------------: | ------------------: | ---------------------: | -------------------: | ----------------------------: | --------------------------: |
| Random         |  1,000 |                  15.6 |                1.33 |                    7.8 |                 1.72 |                          42.9 |                        0.71 |
|                | 10,000 |                 156.2 |               18.98 |                   78.1 |                12.37 |                         392.4 |                        9.68 |
|                | 50,000 |                 781.2 |              116.26 |                  390.6 |                73.25 |                       2,147.7 |                       51.25 |
| Sorted         |  1,000 |                  15.6 |                1.42 |                    7.8 |                 0.89 |                          37.1 |                        0.74 |
|                | 10,000 |                 156.2 |               22.74 |                   78.1 |                10.29 |                         576.0 |                        8.13 |
|                | 50,000 |                 781.2 |              116.28 |                  390.6 |                57.77 |                       1,752.6 |                       53.11 |
| Reverse-sorted |  1,000 |                  15.6 |                1.22 |                    7.8 |                 0.84 |                          52.1 |                        0.80 |
|                | 10,000 |                 156.2 |               18.19 |                   78.1 |                10.06 |                         409.1 |                        8.03 |
|                | 50,000 |                 781.2 |               99.07 |                  390.6 |                54.13 |                       2,244.8 |                       61.19 |

## Part 2: Priority Queue

### Design

I have implemented my priority queue using a list to store a binary heap, as in heap_sort.py. I have also imported certain functions from heap_sort.py into the priority queue to use them directly from the heap sort file. I created a Task class that stores the task ID, priority, arrival time, and deadline, and I decided to use a max-heap, so the task with the highest priority is always at the root and is run first by the scheduler. To keep the code simple, I reused swap() and siftDown() from my heap_sort.py. To make this work, I added three comparison functions to the Task class so that tasks are compared by priority in the same way as numbers.

### Operations

I implemented various operations such as insert(), increase_key(), extract_max() and is_empty. The first one is is_empty, which checks the list's length. Next, insert() adds the new task at the end of the list, and since the height of the heap is log n, insert() takes O(log n). When it adds a new task at the end, the new task is moved up the heap until it meets the parent with the higher priority, which then takes the place of this parent’s children. extract_max() works by swapping the root with the last task, removing it, and calling siftDown() on the new root, which also takes O(log n). Lastly, increase_key() has to find the task by its ID with a loop, which takes O(n), and then move it up in O(log n), so the overall operation takes O(n).

### Scheduler results

In my test, I added four tasks with priorities 3, 5, 1, and 4, and then increased task 3's priority from 1 to 6. The scheduler ran task 3 first, then tasks 2, 4, and 1, which shows that the heap kept the highest-priority task at the top even after its priority changed.
