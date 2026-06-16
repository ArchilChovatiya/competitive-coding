class Node:
    def __init__(self, val: Optional[int] = None, key: Optional[int] = None, prev: Optional[Node]= None, next: Optional[Node]= None) -> None:
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.store = {}
        self.start = Node()
        self.end = Node()
        self.start.next = self.end
        self.end.prev = self.start
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.store:
            curr = self.store[key]
            prev = curr.prev
            next = curr.next
            prev.next, next.prev = next, prev

            prev = self.end.prev
            curr.next = self.end
            curr.prev = prev
            prev.next = curr
            self.end.prev = curr

            return curr.val 
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            curr = self.store[key]
            prev , next = curr.prev , curr.next
            prev.next, next.prev = next, prev

            prev = self.end.prev
            curr.next = self.end
            curr.prev = prev
            prev.next = curr
            self.end.prev = curr
            curr.val = value
        else:
            if self.size == self.capacity:
                curr = self.start.next
                self.start.next = curr.next
                curr.next.prev = self.start
                del self.store[curr.key]
                self.size-=1

            curr = Node(value, key)
            self.store[key] = curr
                
            prev = self.end.prev
            self.end.prev = curr
            curr.next = self.end
            curr.prev = prev
            prev.next = curr
                
            self.size +=1
