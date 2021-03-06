from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


class Node(object):
    """Node class as building block for linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListOrdered(object):
    """Ordered singly linked list class.

    Operations include the following:
      - is_empty()
      - size()
      - show()
      - add(data)
      - delete_with_data(data)
      - pop(pos)
      - search(item)
      - index(item)
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        """Check list is empty or not.

        Time complexity: O(1).
        Space complexity: O(1).
        """
        return self.head is None

    def size(self):
        """Obtain list size.

        Time complexity: O(n).
        Space complexity: O(1).
        """
        current = self.head
        counter = 0
        while current:
            counter += 1
            current = current.next   
        return counter

    def show(self):
        """Print the list.

        Time complexity: O(n).
        Space complexity: O(n).
        """
        a_list = []
        current = self.head
        while current:
            a_list.append(current.data)
            current = current.next
        print(a_list)

    def add(self, data):
        """Add data to list.

        Time complexity: O(n).
        Space complexity: O(1).
        """
        if not self.head:
            self.head = Node(data)
            return None
        if self.head.data > data:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return None

        current = self.head
        previous = None
        is_stop = False
        
        while not is_stop and current.next:
            if current.next.data > data:
                is_stop = True

            previous = current
            current = current.next

        new_node = Node(data)
        if not previous:
            current.next = new_node
        else:
            if not is_stop:
                current.next = new_node
            else:
                new_node.next = current
                previous.next = new_node              

    def delete_with_data(self, data):
        """Delete data from list, if existed.

        Time complexity: O(n).
        Space complexity: O(1).
        """
        if not self.head:
            return None
        if self.head.data == data:
            self.head = self.head.next
            return None

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return None
            else:
                current = current.next


    def pop(self, pos=None):
        """Pop list item at specified position.

        If pos is None, then pop the last item.

        Time complexity: O(pos).
        Space complexity: O(1).
        """
        if not self.head:
            return None
        if not pos:
            pos = self.size() - 1

        current = self.head
        previous = None
        counter = 0

        while counter < pos and current.next:
            previous = current
            current = current.next
            counter += 1

        if not previous:
            self.head = current.next
        else:
            previous.next = current.next

        return current.data

    def search(self, data):
        """Search data in list.

        Time complexity: O(n).
        Space complexity: O(1).
        """
        if not self.head:
            return False

        current = self.head
        is_found = False
        is_stop = False

        while not is_found and not is_stop and current.next:
            if current.data == data:
                is_found = True
            else:
                if current.data > data:
                    is_stop = True
                else: 
                    current = current.next
        
        return is_found

    def index(self, data):
        """Obtain data's index in list.

        Time complexity: O(n).
        Space complexity: O(1).
        """
        if not self.head:
            return None

        current = self.head
        is_found = False
        is_stop = False
        counter = 0

        while not is_found and not is_stop and current.next:
            if current.data == data:
                is_found = True
            else:
                if current.data > data:
                    is_stop = True
                else:
                    current = current.next
                    counter += 1
        
        if not is_found:
            counter = None

        return counter


def main():
    a_list = LinkedListOrdered()
    a_list.add(31)
    a_list.add(77)
    a_list.add(17)
    a_list.add(93)
    a_list.add(26)
    a_list.add(54)
    print('Is empty: {}'.format(a_list.is_empty()))
    print('Size: {}'.format(a_list.size()))

    print('Delete non-existed 100')
    a_list.delete_with_data(100)
    a_list.show()
    print('Delete 77')
    a_list.delete_with_data(77)
    a_list.show()

    print('Pop pos 3:')
    a_list.pop(3)
    a_list.show()

    print('Search non-existed 100: {}'.format(a_list.search(100)))
    print('Search 31: {}'.format(a_list.search(31)))

    print('Index non-existed 100: {}'.format(a_list.index(100)))
    print('Index 31: {}'.format(a_list.index(31)))


if __name__ == '__main__':
    main()
