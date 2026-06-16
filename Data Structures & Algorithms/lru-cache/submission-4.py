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
            self.removeNode(curr)
            self.addNodeToTheEnd(curr)

            return curr.val 
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            curr = self.store[key]
            curr.val = value
            self.removeNode(curr)
            self.addNodeToTheEnd(curr)

        else:
            if self.size == self.capacity:
                curr = self.start.next
                del self.store[curr.key]
                self.removeNode(curr)
                del curr
                self.size-=1

            curr = Node(value, key)
            self.store[key] = curr
            self.addNodeToTheEnd(curr)
            self.size +=1

    def removeNode(self, node: Node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
    
    def addNodeToTheEnd(self, node: Node):
        prev = self.end.prev
        node.next = self.end
        node.prev = prev
        prev.next = node
        self.end.prev = node