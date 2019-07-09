"""Tree based data structures

classes: PriorityQueues

version: 1.0

author: Sunny Capt

email: sunny.capt@tuta.io
"""

import random
from typing import List

import math


def get_graph_matrix(arr: List[str]):
    matrix = []
    for i in range(len(arr)):
        if math.log(i + 1, 2).is_integer():
            matrix.append([])
        matrix[-1].append(arr[i])
    return matrix


class PriorityQueues:
    """Heap data structure that takes the form of a binary tree"""

    class _ObjectWithPriority:
        def __init__(self, obj: object = None, priority=0):
            self.obj = obj
            self.priority = priority

        def change_priority(self, new_priority):
            old_priority, self.priority = self.priority, new_priority
            return old_priority

    def __init__(self):
        self._array: List[PriorityQueues._ObjectWithPriority] = []

    def insert(self, obj, priority):
        self._array.append(self._ObjectWithPriority(obj, priority))
        self._sift_up(len(self._array))

    def remove(self, it: "Full binary tree node index (first is 1)"):
        self.change_priority(it, -1 * float('inf'))
        self.extract_min()

    def get_min(self):
        return self._array[0].obj

    def extract_min(self):
        obj = self._array[0].obj
        self._array[0] = self._array.pop()
        self._sift_down(1)
        return obj

    def change_priority(self, it: "tree node index (first is 1)", new_priority):
        old_priority = self._array[it - 1].change_priority(new_priority)
        diff = new_priority - old_priority
        if diff > 0:
            self._sift_down(it)
        elif diff < 0:
            self._sift_up(it)

    def _sift_up(self, it: "Full binary tree node index (first is 1)"):
        child = it - 1
        parent = child // 2
        while self._array[parent].priority > self._array[child].priority:
            self._array[parent], self._array[child] = self._array[child], self._array[parent]
            child = parent
            parent = child // 2

    def _sift_down(self, it: "Full binary tree node index (first is 1)"):
        parent = it - 1
        child_i = 2 * parent + 1
        child_j = child_i + 1
        check = lambda i: i < len(self._array) and self._array[parent].priority > self._array[i].priority
        while True:
            if check(child_i):
                index = child_i
            if check(child_j):
                index = child_j if self._array[child_j].priority <= index else index
            if not (check(child_i) or check(child_j)):
                break
            self._array[parent], self._array[index] = self._array[index], self._array[parent]
            parent = index
            child_i = 2 * parent + 1
            child_j = child_i + 1


if __name__ == "__main__":
    queue = PriorityQueues()
    for _ in range(100):
        c = random.randint(76, 120)
        queue.insert(chr(c), c - 66)
    matrix = get_graph_matrix([elem.obj for elem in queue._array])
    result = []
    w = 2
    ind = 0
    for line in matrix[::-1]:
        result.append(ind * "~" + (w * "~").join(line) + ind * "~")
        ind, w = w - 1, w * 2
    print("\n".join(result[::-1]))
