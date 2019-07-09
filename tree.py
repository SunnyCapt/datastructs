"""Tree based data structures

classes: PriorityQueues

version: 1.0

author: Sunny Capt

email: sunny.capt@tuta.io
"""

from typing import List


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
        pass

    def _sift_down(self, it: "Full binary tree node index (first is 1)"):
        pass
