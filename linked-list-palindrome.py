# Task: check if Linked List is a Palindrome


class Node(object):
    """Node in a linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    """Linked List using head and tail."""

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        """Append node with data to end of list."""

        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            # Did list start as empty?
            self.tail.next = new_node

        self.tail = new_node

    def print_list(self):
        """Print all items in the list."""

        current = self.head

        while current is not None:
            print current.data
            current = current.next

    def find(self, data):
        """Does this data exist in our list?"""

        current = self.head

        while current is not None:
            if current.data == data:
                return True

            current = current.next

        return False

    def remove(self, value):
        """Remove node with given value"""

        # If removing head, make 2nd item (if any) the new .head
        if self.head is not None and self.head.data == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return

        # Removing something other than head
        current = self.head

        while current.next is not None:

            if current.next.data == value:
                current.next = current.next.next
                if current.next is None:
                    # If removing last item, update .tail
                    self.tail = current
                return

            else:     # haven't found yet, keep traversing
                current = current.next


def is_palindrome():
    """Determine if linked list is a palindrome."""

    # need to know if linked list is odd/even using slow/fast runners
    # if fast.next is none, means list is EVEN + slow is on MIDDLE item
    # if fast is none, means list is ODD + slow is on MIDDLE item

    # as we traverse, need to keep a list of node's DATA
    # Even: once slow is on middle (and list filled), use stack by popping off
    # last item on list after each check
    # Odd: same as even except pop off last item in list before the check

    # First, create a Linked List with 4 nodes
    node1 = Node("T")
    node2 = Node("O")
    node3 = Node("O")
    node4 = Node("T")

    lst = LinkedList()

    # Create runners
    slow_runner = self.head
    fast_runner = self.head.next

    # Create empty list to attach data during traversal
    lst_data = []

    while

