class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def find(self, key):
        cur = self.head

        while cur is not None:
            if cur.key == key:
                return cur.value
            cur = cur.next

        return None

    def insert_at_head(self, key, value):
        n = HashTableEntry(key, value)
        n.next = self.head
        self.head = n

    def delete(self, key):
        cur = self.head

        if cur.key == key:
            self.head = self.head.next
            cur.next = None  # cleaning the pointer for the deleted value
            return cur

        prev = cur
        cur = cur.next

        while cur is not None:
            if cur.key == key:
                prev.next = cur.next
                cur.next = None
                return cur
            else:
                prev = prev.next
                cur = cur.next

        return None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = [None] * capacity
      #   self.capacity = capacity
      #   self.count = 0
        self.num_of_items = 0
        self.head = None

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.capacity)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """

      #   load factor =  # of elements / # of buckets
      # In your terminology: the number of items currently in the table divided by the size of the array.
        # Your code here
        return (self.num_of_items / self.capacity)

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for i in range(len(key)):
            hash = ((hash << 5) + hash) + ord(key[i])
        return hash & 0xFFFFFFFF

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % len(self.capacity)

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        # Your code here
        key_index = self.hash_index(key)
        self.num_of_items += 1

        if self.capacity[key_index] is not None:
            # there is a linked list at the location
            # see if key exists to override
            overwrite = self.capacity[key_index].find(key)
            if overwrite is not None:
                # the key already exists in the linked list
                cur = self.capacity[key_index].head

                while cur is not None:
                    if cur.key == key:
                        cur.value = value
                    cur = cur.next
            else:
                self.capacity[key_index].insert_at_head(key, value)
        else:
            # no linked list there
            ll = LinkedList()
            ll.insert_at_head(key, value)
            self.capacity[key_index] = ll

      #   load = self.get_load_factor()

      #   if load > 0.7:
      #       self.resize(len(self.capacity) * 2)

    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        # Your code here
        key_index = self.hash_index(key)

        if self.capacity[key_index] is not None:

            self.num_of_items -= 1
            deleted_node = self.capacity[key_index].delete(key)

            return deleted_node
        else:
            return None

        load = self.get_load_factor()

        if load < 0.2:
            self.resize(len(self.capacity) / 2)

    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        # Your code here
        key_index = self.hash_index(key)

        if self.capacity[key_index] is not None:
            return self.capacity[key_index].find(key)
        else:
            return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        Implement this.
        """
        # Your code here
        old_table = self.capacity
        self.capacity = [None] * new_capacity
        self.num_of_items = 0

        for x in old_table:
            if x is not None:
                cur = x.head

                while cur is not None:
                    # do something
                    self.put(cur.key, cur.value)
                    cur = cur.next


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
   #  ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
