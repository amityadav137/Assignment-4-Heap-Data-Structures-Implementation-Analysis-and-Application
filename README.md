# Assignment 4: Heap Data Structures — Implementation, Analysis, and Applications

This repository contains the implementation of the Heapsort algorithm and a Priority Queue using a binary heap. The assignment demonstrates how heap data structures can be used for efficient sorting and task scheduling.

## Contents

- `heapsort.py`: Implementation of the Heapsort algorithm.
- `priority_queue.py`: Implementation of a Priority Queue using a binary heap with task scheduling.
- `analysis_comparison.py`: Script comparing Heapsort with Quicksort and Merge Sort on different data distributions.
- `report.md`: Detailed explanation of design choices, implementation, time and space complexity analysis, and experimental results.

## How to Run

Ensure you have Python 3.x installed.

1. **Clone the repository:**

   ```bash
   git clone https://github.com/amityadav137/Assignment-4-Heap-Data-Structures-Implementation-Analysis-and-Application.git
   cd Assignment-4-Heap-Data-Structures-Implementation-Analysis-and-Application
   ```

2. **Run Heapsort Example:**

   ```bash
   python heapsort.py
   ```

3. **Run Priority Queue Simulation:**

   ```bash
   python priority_queue.py
   ```

4. **Run Comparison of Sorting Algorithms:**

   ```bash
   python analysis_comparison.py
   ```

## Summary of Findings

- **Heapsort** offers consistent time complexity of O(n log n) in all cases, making it stable for worst-case performance.
- **Priority Queue** efficiently handles dynamic scheduling scenarios using heap operations with logarithmic time complexity.
- **Comparative analysis** shows that while Quicksort is often faster in practice on average, Heapsort is more predictable in time complexity.
