"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

from queue import Queue
from stack import Stack

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    # check if it's empty
    # if it's empty put node at the root
    # else if new < node.vale - leftnode.insert value
    # if >=  - rightnode.insert value
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    # if node is none
    # return false
    # if node.value == findvalue
    # return true
    # else if find < node.valueif node.left
    # find on left node
    def contains(self, target):
        if self.value == target:
            return True
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    # will always be the most right node
    # if there is a right node get max on right
    # else return node.value
    # def get_max(self):
    #     if self.right is None:
    #         return self.right.get_max()
    #     else:
    #         return self.value
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left is not None:
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node=None):
        if self.left is not None:
            self.left.in_order_print()
        print(self.value)
        if self.right is not None:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)
        while queue.__len__() > 0:
            current_node = queue.dequeue()
            print(current_node.value)
            if current_node.left:
                queue.enqueue(current_node.left)
            if current_node.right:
                queue.enqueue(current_node.right)


        # if node is None:
        #     return
        # queue = Queue()
        # queue.enqueue(node)
        # while len(queue) > 0:
        #     print(queue)
        #     node = queue.enqueue(0)
        #     if self.left is not None:
        #         queue.enqueue(self.left)
        #     if self.right is not None:
        #         queue.enqueue(self.right)
    # print(node)
        # while Queue().__len__ != 0:
        #     current = Queue().dequeue()
        #     # print(current.value)
        #     print(current)
        #     if not current:
        #         return
        #     if current.left < current:
        #         Queue().enqueue(current.left)
        #     if current.right >= current:
        #         Queue().enqueue(current.right)
            # if current.left is not None:
            #     Queue().enqueue(current.left)
            # if current.right is not None:
            #     Queue().enqueue(current.right)
        # while len(Queue())> 0:
        #     current = Queue().dequeue()
        #     if current is None:
        #         return
        #     if current.left:
        #         Queue().enqueue(current.left)
        #     if current.right is not None:
        #         Queue().enqueue(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node=None):
        stack=Stack()
        stack.push(node)
        while stack.__len__() > 0:
            current = stack.pop()
            print(current.value)
            if current.left is not None:
                stack.push(current.left)
            if current.right is not None:
                stack.push(current.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
