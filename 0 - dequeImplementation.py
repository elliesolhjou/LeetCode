class Deque:
    def __init__(self):
        # define array
        self.items=[]
        # create size (count of index)
        self.size = 0
    def append_left(self, element):
        # create new array with new size (adding one element every time appending = increasing size) in cpu
        new_items = [None] * (self.size+1)
        # assign first left cell to the element
        new_items[0] = element
        # Copy the existing elements to the new array, starting from index 1
        # shifting rest of previous elements to right
        for i in range(1, self.size+1):
            new_items[i] = self.items[i-1]
        self.items = new_items
        self.size +=1
    def append_right(self, element):
        # growing array -> creating new array with new size
        new_items = [None] * (self.size+1)
        # assign last cell of array on right to element
        new_items[self.size] = element
        # Copy the existing elements to the new array, starting from index 0
        for i in range(self.size+1):
            new_items[i] = self.items[i]
        self.items= new_items
        self.size+=1
    
    # pop return element
    def pop_left(self): 
        # if queue is empty raise an error
        if not self.size == 0:
            raise IndexError("empty queue")
        # grab value of popped element
        element = self.items[0]
        # create new array with new size
        new_items= [None] * (self.size-1)
        # shift elements to right
        for i in range(1, self.size-1):
            new_items[i-1] = self.items[i]
        self.items = new_items
        self.size -=1
        return element

    def pop_right(self):
        # return value
        # if queue is empty
        if self.size == 0:
            raise IndexError("empty stack")
        # grab return value
        element = self.items[self.size-1]
        # create new array
        new_items = [None]* (self.size-1)
        # copy old array elements to new array
        for i in range(self.size-1):
            new_items[i] = self.items[i]
        
        new_items = self.items
        self.size -=1
        return element

    def peek_left(self):
        # return value
        # check size
        if self.size == 0:
            raise IndexError ("empty queue")
        element = self.items[0]
        return element
    
    def peek_right(self):
        if self.size == 0:
            raise IndexError ("empty queue")
        return self.items[self.size-1]

    def get_count(self):
        return self.size
    
    def __str__(self):
        return str(self.items[:self.size])
    