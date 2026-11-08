from heap_sort import swap, siftDOwn


class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):     # one task with its information
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __lt__(self, other):            # tasks are compared by their priority, so siftDown from heapsort works on them
        return self.priority < other.priority

    def __gt__(self, other):
        return self.priority > other.priority

    def __ge__(self, other):
        return self.priority >= other.priority


class PriorityQueue:
    def __init__(self):                 # empty heap stored in a list
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def sift_up(self, i):               # move the task up 
        while i > 0 and self.heap[i] > self.heap[(i - 1) // 2]:
            swap(self.heap, i, (i - 1) // 2)
            i = (i - 1) // 2

    def insert(self, task):             # add the task at the end 
        self.heap.append(task)
        self.sift_up(len(self.heap) - 1)

    def extract_max(self):              # remove and return the task with the hihgest priority
        swap(self.heap, 0, len(self.heap) - 1)
        top_task = self.heap.pop()
        siftDOwn(self.heap, 0, len(self.heap))
        return top_task

    def increase_key(self, task_id, new_priority):     # find the task and raise its priority 
        for i in range(len(self.heap)):
            if self.heap[i].task_id == task_id:
                self.heap[i].priority = new_priority
                self.sift_up(i)
                return


if __name__ == "__main__":

    queue = PriorityQueue()

    for task in [Task(1, 3, 0, 10), Task(2, 5, 1, 8), Task(3, 1, 2, 15), Task(4, 4, 3, 12)]:   # loop to add the tasks
        queue.insert(task)

    queue.increase_key(3, 6)            # task 3 becomes the most important one

    while not queue.is_empty():         # loop that runs the tasks in order of priority
        task = queue.extract_max()
        print("running task", task.task_id, "with priority", task.priority)