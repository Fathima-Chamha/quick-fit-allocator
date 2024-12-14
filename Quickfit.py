class QuickFitAllocator:
    def __init__(self, block_sizes):
        # Initialize free lists for each block size
        self.free_lists = {size: [] for size in block_sizes}

    def initialize_memory(self, size_blocks):
        """
        Pre-populates the free lists with blocks.
        size_blocks: dict where key is block size, value is the number of blocks.
        """
        for size, count in size_blocks.items():
            if size in self.free_lists:
                self.free_lists[size] = [f"Block-{size}-{i+1}" for i in range(count)]
            else:
                print(f"Block size {size} is not recognized.")

    def allocate(self, size):
        """Allocates a block of the requested size."""
        if size in self.free_lists and self.free_lists[size]:
            return self.free_lists[size].pop(0)
        else:
            print(f"No free block available for size {size}.")
            return None

    def deallocate(self, size, block):
        """Deallocates a block and adds it back to the free list."""
        if size in self.free_lists:
            self.free_lists[size].append(block)
        else:
            print(f"Invalid block size {size}.")

    def display_free_lists(self):
        """Displays the current state of the free lists."""
        print("\nCurrent Free Lists:")
        for size, blocks in self.free_lists.items():
            print(f"  Size {size}: {blocks if blocks else 'No blocks available'}")

# Define block sizes and initialize the Quick Fit Allocator
block_sizes = [8, 16, 32]
allocator = QuickFitAllocator(block_sizes)

# Pre-populate memory with blocks for each size
allocator.initialize_memory({8: 3, 16: 2, 32: 1})

while True:
    print("\nQuick Fit Memory Allocation")
    print("1. Allocate memory")
    print("2. Deallocate memory")
    print("3. Display free lists")
    print("4. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        try:
            size = int(input("Enter block size to allocate (8, 16, 32): "))
            block = allocator.allocate(size)
            if block:
                print(f"Allocated {block}")
        except ValueError:
            print("Invalid size. Please enter a valid number.")
    elif choice == "2":
        try:
            size = int(input("Enter block size to deallocate (8, 16, 32): "))
            block = input("Enter block name to deallocate (e.g., Block-8-1): ").strip()
            allocator.deallocate(size, block)
            print(f"Deallocated {block}")
        except ValueError:
            print("Invalid size. Please enter a valid number.")
    elif choice == "3":
        allocator.display_free_lists()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
