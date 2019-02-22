from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np


def parent(i):
    return i // 2

def left(i):
    return 2 * i

def right(i):
    return 2 * i + 1


class MaxHeap(object):
    """Max Heap implementation of Priority Queue.

    Max-heap property: A[parent(i)] >= A[i], i = left, right.

    Application: Heapsort Algorithm.
    """
    def __init__(self):
        self.A = [0]
        self.heap_size = 0

    def show(self):
        print(self.A)

    def get_max(self):
        return self.A[1]

    def heapify(self, i):
        """Max heapify operation.

        Complexity: O(log(n)).
        """
        l = left(i)
        r = right(i)
        if l <= self.heap_size and self.A[l] > self.A[i]:
            max_i = l
        else:
            max_i = i
        if r <= self.heap_size and self.A[r] > self.A[max_i]:
            max_i = r
        if max_i != i:
            # Swap node i and node max_i.
            self.A[i], self.A[max_i] = self.A[max_i], self.A[i]
            self.heapify(max_i)

    def build(self, arr):
        """Build max heap from unordered array.

        Start from the level-1 nodes from leaves back to level-log(n) node.
        Specifically, node (n/2), node (n/2 - 1), ..., node 1, where
        n is the number of nodes including the root one.

        Complexity: O(n*log(n)) via simple analysis. Actually O(n).
        """
        self.A.extend(arr)
        self.heap_size = len(arr)
        for i in reversed(range(1, (self.heap_size + 1) // 2 + 1)):
            self.heapify(i)

    def extract_max(self):
        if self.heap_size < 1:
            raise ValueError('Heap underflow.')
        maximum = self.A[1]
        last = self.A.pop()
        self.heap_size -= 1
        if self.heap_size < 1:
            # The last element is maximum.
            pass
        else:
            self.A[1] = last
        self.heapify(1)
        return maximum

    def increase_key(self, i, key):
        if self.A[i] > key:
            raise ValueError('New key is smaller than current key.')
        self.A[i] = key
        while i > 1 and self.A[parent(i)] < self.A[i]:
            # Swap node i and node parent(i).
            self.A[i], self.A[parent(i)] = self.A[parent(i)], self.A[i]
            i = parent(i)

    def insert(self, new_key):
        self.heap_size += 1
        self.A.append(-np.inf)
        self.increase_key(self.heap_size, new_key)


def main():
    print('Max Heap by inserting 1, 3, 5, 7:')
    max_pq = MaxHeap()
    max_pq.insert(1)
    max_pq.insert(3)
    max_pq.insert(5)
    max_pq.insert(7)
    max_pq.show()

    print('Build max heap from unordered list [1, 3, 5, 7]:')
    max_pq = MaxHeap()
    max_pq.build([1, 3, 5, 7])
    max_pq.show()   

    print('Increase key 1 at position 4 to 6.')
    max_pq.increase_key(4, 6)
    max_pq.show()

    print('Get max:')
    print(max_pq.get_max())

    print('Extract max:')
    _max = max_pq.extract_max()
    print(_max)
    print('The remaining:')
    max_pq.show()


if __name__ == '__main__':
    main()