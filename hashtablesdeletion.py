SIZE = 5  # Define the size of the hash table

class DataItem:
    def __init__(self, key):
        self.key = key

def hashCode(key):
    # Implement your hash function here
    # Return a hash value based on the key
    return key % SIZE

def insert(key):
    global hashArray  # Access the global hashArray variable
    # Calculate the hash index for the key
    hashIndex = hashCode(key)

    # Handle collisions (linear probing)
    while hashArray[hashIndex] is not None:
        # Move to the next cell
        hashIndex = (hashIndex + 1) % SIZE

    # Insert the new DataItem at the calculated index
    hashArray[hashIndex] = DataItem(key) # type: ignore

    # Print the inserted item's key and hash index
    print(f"Inserted key {key} at index {hashIndex}")

def delete(key):
    global hashArray  # Access the global hashArray variable
    # Find the item in the hash table
    hashIndex = hashCode(key)
    while hashArray[hashIndex] is not None:
        if hashArray[hashIndex].key == key:
            # Mark the item as deleted (optional: free memory)
            hashArray[hashIndex] = None
            return
        # Move to the next cell
        hashIndex = (hashIndex + 1) % SIZE

    # If the key is not found, print a message
    print(f"Item with key {key} not found.")

# Initialize the hash table as a list of None values
hashArray = [None] * SIZE
print("Hash Table Contents before deletion:")
# Call the insert function with different keys to populate the hash table
insert(1)  # Insert an item with key 1
insert(2)  # Insert an item with key 2
insert(3)  # Insert an item with key 3
insert(4)  # Insert an item with key 4
ele1 = 2
ele2 = 4
print("The keys to be deleted: ", ele1, " and ", ele2)
delete(2)  # Delete an item with key 2
delete(4)  # Delete an item with key 4
