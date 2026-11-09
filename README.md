# MSCS532 Assignment 4: Heap Data Structures

Heapsort compared with Merge Sort and randomized Quicksort, and a priority queue built on a binary max-heap.
The full report is in [Reports/REPORT.md](Reports/REPORT.md).

## Files

- `heap_sort.py` – Heapsort: builds a max-heap, then moves the largest number to the end with `swap()` and `siftDown()`
- `priority_q.py` – `Task` class and a max-heap `PriorityQueue` with `insert()`, `extract_max()`, `increase_key()` and `is_empty()`, plus a small scheduler demo
- `main.py` – runs a sort on a data file and saves time and memory to `results.csv`
- `merge_sort.py`, `quick_sort_random.py` – the sorting algorithms used for the comparison
- `recorder.py`, `file_parser.py` – timing, memory and file reading helpers
- `data/` – random, sorted and reverse-sorted inputs (1,000 / 10,000 / 50,000 numbers)
- `results.csv` – benchmark results

`merge_sort.py`, `quick_sort_random.py`, `recorder.py`, `file_parser.py` and the `data/` files are adapted from my Assignments 2 and 3.

## How to run

Requires Python 3.

Sorting (choose `h`, `m` or `q`, then enter a file such as `data/sorted_large.txt`):

```bash
python3 main.py
```

To run all 27 tests at once:

```bash
for alg in h m q; do
  for kind in random sorted reverse; do
    for size in small mid large; do
      printf "$alg\ndata/${kind}_${size}.txt\n" | python3 main.py > /dev/null
    done
  done
done
```

Priority queue and scheduler demo:

```bash
python3 priority_q.py
```

## Summary of findings

- Heapsort is O(n log n) in every case and took about the same time on random, sorted and reverse-sorted input (99–116 ms at 50,000 numbers).
- Even with the same O(n log n), Quicksort (51–61 ms) and Merge Sort (54–73 ms) were both clearly faster than Heapsort, because Heapsort jumps around the list and does more swaps.
- In the priority queue, `insert()` and `extract_max()` take O(log n), `increase_key()` takes O(n) because it searches for the task first, and `is_empty()` takes O(1).
