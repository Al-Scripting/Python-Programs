class Queue:
    def __init__(self):
        # Initialize the queue with an empty list
        self.items = []

    def is_empty(self):
        # Return True if the queue is empty, else return False
        return len(self.items) == 0

    def enqueue(self, item):
        # Add the item to the end of the list (i.e., enqueue it)
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            # If the queue is empty, raise an exception
            raise Exception("\nQueue is empty\n")
        # Remove the first item from the list (i.e., dequeue it) and return it
        return self.items.pop(0)

    def size(self):
        # Return the number of items in the list (i.e., the size of the queue)
        return len(self.items)

    def printQueue(self):
        count = 1
        print("Queue:")
        for item in self.items:
            print(f"{count}. {item}")
            count += 1
        print("")

# Main program to test the Queue implementation
queue = Queue()

while True:
    # Display the menu options
    print("Select an option:")
    print("1. Enqueue an item")
    print("2. Dequeue an item")
    print("3. Check if the queue is empty")
    print("4. Get the size of the queue")
    print("5. Print queue")
    print("6. Quit")

    # Get the user's choice
    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        # Enqueue an item by getting it from the user and adding it to the queue
        item = input("Enter the item to enqueue: ")
        queue.enqueue(item)
        print(f"\n{item} was enqueued.\n")
    elif choice == 2:
        # Dequeue an item and display it
        try:
            item = queue.dequeue()
            print(f"\n{item} was dequeued.\n")
        except Exception as e:
            print(e)
    elif choice == 3:
        # Check if the queue is empty and display the result
        if queue.is_empty():
            print("\nThe queue is empty.\n")
        else:
            print("\nThe queue is not empty.\n")
    elif choice == 4:
        # Get the size of the queue and display it
        size = queue.size()
        print(f"\nThe size of the queue is {size}.\n")

    elif choice == 5:
        if queue.is_empty():
            print("\nThe queue is empty.\n")
        else:
            queue.printQueue()


    elif choice == 6:
        # Quit the program
        print("\nEND PROGRAM")
        break

    else:
        print("\nInvalid choice. Please try again.\n")
