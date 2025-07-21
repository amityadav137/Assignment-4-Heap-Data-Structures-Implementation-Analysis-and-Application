import heapq

class Task:
    def __init__(self, task_id, priority, arrival, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival = arrival
        self.deadline = deadline

    def __lt__(self, other):
        return self.priority < other.priority

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, task):
        heapq.heappush(self.heap, task)

    def extract_min(self):
        return heapq.heappop(self.heap) if not self.is_empty() else None

    def decrease_key(self, task_id, new_priority):
        for task in self.heap:
            if task.task_id == task_id:
                self.heap.remove(task)
                heapq.heapify(self.heap)
                task.priority = new_priority
                self.insert(task)
                break

    def is_empty(self):
        return len(self.heap) == 0

if __name__ == "__main__":
    pq = PriorityQueue()
    pq.insert(Task(1, 4, 0, 10))
    pq.insert(Task(2, 2, 1, 5))
    pq.insert(Task(3, 1, 2, 3))

    while not pq.is_empty():
        task = pq.extract_min()
        print(f"Task {task.task_id} with priority {task.priority}")
