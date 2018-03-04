from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

class MinBinaryHeap(object):
    """Binary Min Heap class with (key, val)."""
    def __init__(self):
        self.heap_ls = [(0, 0)]
        self.current_size = 0

    def show(self):
        print(self.heap_ls)

    def _percolate_up(self, i):
        while i // 2 > 0:
            if self.heap_ls[i][0] < self.heap_ls[i // 2][0]:
                tmp = self.heap_ls[i // 2]
                self.heap_ls[i // 2] = self.heap_ls[i]
                self.heap_ls[i] = tmp
            i = i // 2

    def insert(self, new_node):
        self.heap_ls.append(new_node)
        self.current_size += 1
        self._percolate_up(self.current_size)

    def _get_min_child(self, i):
        if (i * 2 + 1) > self.current_size:
            return i * 2
        else:
            if self.heap_ls[i * 2][0] < self.heap_ls[i * 2 + 1][0]:
                return i * 2
            else:
                return i * 2 + 1

    def _percolate_down(self, i):
        while (i * 2) <= self.current_size:
            min_child = self._get_min_child(i)
            if self.heap_ls[i][0] > self.heap_ls[min_child][0]:
                tmp = self.heap_ls[i]
                self.heap_ls[i] = self.heap_ls[min_child]
                self.heap_ls[min_child] = tmp
            else:
                pass
            i = min_child

    def find_min(self):
        return self.heap_ls[1]
    
    def delete_min(self):
        val_del = self.heap_ls[1]
        self.heap_ls[1] = self.heap_ls[self.current_size]
        self.current_size -= 1
        self.heap_ls.pop()
        self._percolate_down(1)
        return val_del

    def is_empty(self):
        return self.current_size == 0

    def size(self):
        return self.current_size

    def __len__(self):
        return self.current_size

    def __contains__(self, vertex):
        for vertex_tp in self.heap_ls:
            if vertex == vertex_tp[1]:
                return True
        return False

    def build_heap(self, a_list):
        # alist: a list of tuples.
        self.current_size = len(a_list)
        self.heap_ls = [(0, 0)] + a_list[:]
        i = len(a_list) // 2
        while i > 0:
            self._percolate_down(i)
            i -= 1

    def decrease_key(self, val, new_key):
        done_bool = False
        i = 1
        new_pos = 0
        while not done_bool and i <= self.current_size:
            if self.heap_ls[i][1] == val:
                done_bool = True
                new_pos = i
            else:
                i += 1
        if new_pos > 0:
            self.heap_ls[new_pos] = (new_key, val)
            self._percolate_up(new_pos)


def main():
    print('Binary heap tuple with (1, a) (3, c)', 
          '(4, b), (5, e), (2, d):')
    bh_min = MinBinaryHeap()
    bh_min.insert((1, 'a'))
    bh_min.insert((3, 'c'))
    bh_min.insert((4, 'b'))
    bh_min.insert((5, 'e'))
    bh_min.insert((2, 'd'))
    bh_min.show()

    print('Find min: {}'.format(bh_min.find_min()))
    print('Is empty? {}'.format(bh_min.is_empty()))
    print('Size? {}'.format(bh_min.size()))

    print('Delete min: {}'.format(bh_min.delete_min()))
    bh_min.show()

    print('Build heap with (1, a), (3, c), (2, b):')
    bh_min = MinBinaryHeap()
    bh_min.build_heap([(1, 'a'), (3, 'c'), (2, 'b')])
    bh_min.show()

    print('len by size(): {}'.format(bh_min.size()))
    print('len by len(): {}'.format(len(bh_min)))
    print('c in bh_min: {}'.format('c' in bh_min))
    print('d in bh_min: {}'.format('d' in bh_min))


if __name__ == '__main__':
    main()
