# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    # '''
    # A hash table that with `capacity` buckets
    # that accepts string keys
    # '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        # '''
        # Hash an arbitrary key and return an integer.
        # You may replace the Python hash with DJB2 as a stretch goal.
        # '''
        return hash(key)


    def _hash_djb2(self, key):
        # '''
        # Hash an arbitrary key using DJB2 hash
        # OPTIONAL STRETCH: Research and implement DJB2
        # '''
        pass


    def _hash_mod(self, key):
        # '''
        # Take an arbitrary key and return a valid integer index
        # within the storage capacity of the hash table.
        # '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        # '''
        # Store the value with the given key.
        # Hash collisions should be handled with Linked List Chaining.
        # '''
        # should include overwritting if key already exist

        node = LinkedPair(key, value)
        hashInd = self._hash_mod(key)
        if self.storage[hashInd] is None:
            self.storage[hashInd] = node
            #print(self.storage[hashInd].value)
            return self.storage[hashInd].value
        else:
            # set currentNode to pointer for bash
            currentNode = self.storage[hashInd]
            while currentNode:
                # rewrite value if key exist 
                if currentNode.key == key:
                    currentNode.value = value
                    #print(currentNode.value)
                    return currentNode.value
                # insert to the end if at the end of list
                elif currentNode.next == None:
                    currentNode.next = node
                    #print(currentNode.next.value)
                    return currentNode.next.value
                # keep looping if there is a node next to current node
                else:
                    currentNode = currentNode.next


    def remove(self, key):
        # '''
        # Remove the value stored with the given key.
        # Print a warning if the key is not found.
        # Fill this in.
        # '''

        # set current to pointer to bash
        current = self.storage[self._hash_mod(key)]

        if current is None:
            print("key not found")
            return
            
        # if removed item is the first item pointed to, remove value 
        if current.key == key:
            current.value = None
            return

        else:
            current = current.next
            
            while current:
                if current.key == key:
                    current.value = None
                    return
                else:
                    current = current.next
                    
        
        print("key not found")
        return
                

    def retrieve(self, key):

        #set current to initial pointer of bash
        current = self.storage[self._hash_mod(key)]
        
        while current:
            if current.key == key:
                return current.value
            else:
                current = current.next
        
        return None



    def resize(self):
        # '''
        # Doubles the capacity of the hash table and
        # rehash all key/value pairs.
        # '''

        tempHash = HashTable(self.capacity * 2)

        # each hashInd is a bash
        for i in range(len(self.storage)):
            # set current to initial pointer in bash
            current = self.storage[i]
            while current:
                tempHash.insert(current.key, current.value)                
                print(f"resizing: {tempHash.retrieve(current.key)}, {tempHash._hash_mod(current.key)}")
                current = current.next
        
        self.capacity = self.capacity * 2
        self.storage = tempHash.storage

if __name__ == "__main__":
    ht = HashTable(2)
    
    print("")

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")
    # ht.insert("line_1", "Tiny hash table is now big hash table")
    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")

