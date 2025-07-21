# Assignment 4: Heap Data Structures — Implementation, Analysis, and Applications

## 1. Heapsort Implementation

The Heapsort algorithm was implemented using a max-heap constructed from an array. The algorithm follows these key steps:
- Build a max-heap from the input array.
- Repeatedly extract the maximum element from the heap and move it to the end of the array.
- Restore the heap property after each extraction using `heapify`.

### Python Code
See `heapsort.py` for full implementation and test examples.

## 2. Heapsort Time and Space Complexity

| Case        | Time Complexity | Reason                                                                 |
|-------------|------------------|------------------------------------------------------------------------|
| Best Case   | O(n log n)       | Building the heap is O(n), and extracting max is O(log n) per element. |
| Average Case| O(n log n)       | The operations are consistent regardless of input ordering.            |
| Worst Case  | O(n log n)       | Even with worst distribution, time remains logarithmic per extraction. |

- **Space Complexity**: O(1) additional space (in-place sort).

## 3. Comparison with Other Algorithms

We compared Heapsort with Quicksort and Merge Sort using the script `analysis_comparison.py`.

### Datasets:
- Sorted
- Reverse Sorted
- Random (uniform distribution)

### Observations:
- **Quicksort** is typically faster on random and sorted inputs.
- **Heapsort** shows consistent performance across all cases.
- **Merge Sort** also has O(n log n) time but uses more memory due to additional arrays.

## 4. Priority Queue Implementation

We implemented a Priority Queue using a binary heap stored in a Python list. Tasks are modeled with a `Task` class including:
- Task ID
- Priority
- Arrival Time
- Deadline

We used a **min-heap** so that the lowest priority value is served first (e.g., shortest deadline first).

### Key Methods:
- `insert(task)`: Adds a task and restores heap property. **Time Complexity**: O(log n)
- `extract_min()`: Removes and returns the task with highest priority (min value). **Time Complexity**: O(log n)
- `decrease_key(task, new_priority)`: Updates the priority and repositions the task. **Time Complexity**: O(log n)
- `is_empty()`: Checks if the heap is empty. **Time Complexity**: O(1)

### Python File: `priority_queue.py`

## 5. Scheduling Application

In a simulation, tasks with various priorities and deadlines were scheduled using the Priority Queue. This shows real-world applications like:
- CPU scheduling
- Print job handling
- Emergency response systems

## 6. Design Justifications

- **Binary heap using array**: Efficient indexing and easy to implement with `heapq`-like logic.
- **Min-heap for scheduling**: More suitable for priority-based task management where lower values have higher urgency.

## 7. Conclusion

This assignment demonstrated:
- In-depth understanding of heap-based sorting and scheduling.
- Implementation of Heapsort with theoretical and empirical analysis.
- Practical priority queue logic for real-world scenarios.
