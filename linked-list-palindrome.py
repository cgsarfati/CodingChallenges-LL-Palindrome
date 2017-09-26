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

    def is_palindrome(head):
        """Determine if linked list is a palindrome. Return True if so."""

        # PSEUDOCODE:
        # need to know if linked list is odd/even using runners
        # if fast.next is none, means list is EVEN + slow is on MIDDLE item
        # if fast is none, means list is ODD + slow is on MIDDLE item

        # as we traverse, need to keep a list of node's DATA
        # Even: once slow is on middle (and list filled), use stack by popping off
        # last item on list after each check
        # Odd: same as even except pop off last item in list before the check

        # create runners
        slow = head
        fast = head

        # keep track of letters in first half of the LL
        stack = []

        # traverse LL until slow in middle
        while fast is not None and fast.next is not None:
            stack.append(slow.data)
            slow = slow.next
            fast = fast.next.next

        # account for odd number of items in LL
        if fast is not None:
            slow = slow.next

        # compare each letter in 2nd half of list to letters in 1st half
        while slow is not None:
            if slow.data != stack.pop():
                return False
            slow = slow.next

        return True
