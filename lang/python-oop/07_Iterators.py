class CountTo:
    def __init__(self, max):
        self.max =  max
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.max:
            value = self.current
            self.current += 1
            return value 
        else:
            raise StopIteration


class ListIterator:
    def __init__(self, array):
        self.array =  array
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.array):
            value = self.array[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration




if __name__ == "__main__":
    counter = CountTo(5)
    for i in counter:
        print(i)
    
    myList = ListIterator([12,13,14,15,16])
    for val in myList:
        print(val)
        