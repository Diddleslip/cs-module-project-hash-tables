class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        total = 0

        for key in self.storage:
            if key is not None:
                total += 1

        return (total / self.capacity)
            

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        hash = 14695981039346656037 ## offset_basis
        kb = key.encode()

        for k in kb:
            hash = hash ^ k
            hash = hash * 1099511628211 # FNV_Prime
            hash &= 0xffffffffffffffff # Converts the number to a 64-bit number if not already
        return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """        

        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Gives us index for storage
        i = self.hash_index(key)

        return self.insert_at_head(key, value, i)
            
    def insert_at_head(self, key, value, i):
        node = HashTableEntry(key, value) # Make the new node

        # If slot is empty, assign node as self.head
        if self.storage[i] is None:
            self.storage[i] = node
        # If slot already has stuff in it, lets swap current head with new node
        else:
            node.next = self.storage[i]
            self.storage[i] = node
            

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        i = self.hash_index(key)

        current = self.storage[i]

        if current.key == key:
            # current is first item so just redirect what is self.storage[i]
            self.storage[i] = self.storage[i].next
            return self.storage[i]

        prev = current
        current = current.next
        while current is not None:
            # If match found, then redirect prev.next to cur.next, current node will get deleted automatically
            if current.key is key:
                prev.next = current.next
                return current.value
            else:
                prev = prev.next
                current = current.next
                
        print("KEY NOT FOUND!")

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # With index, we have access to the NODE
        i = self.hash_index(key)
        ### self.storage[i].key/value to access the things inside the nodes.
        return self.find(key, i)
        # return self.storage[i]

    def find(self, key, i):
        current = self.storage[i]

        # While loop to get through all of the chain-links in that index
        while current is not None:
            if current.key == key:
                # We found it, we can return it
                return current.value

            current = current.next

        # This means we didn't find it after we broke the loop
        return None 

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here

        # Change capacity of self.capacity
        self.capacity = new_capacity
        # Copy of self.storage
        oldStorage = self.storage
        # Resetting self.storage to new capacity
        self.storage = [None] * self.capacity

        
        for i in oldStorage:
            self.put(i.key, i.value)

            current = i.next
            # If there's a chain link on a bucket, then we need to go down the chain
            while current is not None:
                self.put(current.key, current.value)

                current = current.next


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
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
