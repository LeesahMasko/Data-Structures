from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.order = DoublyLinkedList()
        self.storage = dict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        #Key is not in cache - return
        if key not in self.storage:
            return None
        else:
        #Key is in the cache
        #move it ot the most recently used
            node = self.storage(key)
            self.order.move_to_end(node)
        #return value
            return node.value(1)


    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
           # If item or key already exists
        if key in self.storage:
            #overwrite the value
            node = self.storage(key)
            node.value = (key, value)
            #where is the value stored
            self.order.move_to_end(node)
            return

            #move to the tail (most recently used)
        # Size is at limit
        if len(self.order) == self.limit:
            #evict the oldest one
            index_of_oldest = self.order.head.value(0)
            del self.storage(index_of_oldest)
            self.order.remove_from_head()
            #add the new one to the end

        # Size is not at limit
        if len(self.order) < self.limit:
        #add it to order
            self.order.add_to_tail((key, value))
        #add it to storage
            self.storage(key) = self.order.tail



