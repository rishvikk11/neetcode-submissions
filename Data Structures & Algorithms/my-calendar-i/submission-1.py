# binary search tree recursive solution to see if there's overlaps
class Node:
    def __init__(self, start, end, left, right):
        self.start = start
        self.end = end
        self.left = None
        self.right = None

class MyCalendar:
    
    def __init__(self):
        self.root = None

    # inserting a node into the binary search tree
    def insert(self, node, start, end):
        start_time, end_time = node.start, node.end
        if end <= start_time:
            if not node.left:
                new_node = Node(start, end, None, None)
                node.left = new_node
                return True
            return self.insert(node.left, start, end)

        elif start >= end_time:
            if not node.right:
                new_node = Node(start, end, None, None)
                node.right = new_node
                return True
            return self.insert(node.right, start, end)
        
        else:
            return False
    
    def book(self, startTime: int, endTime: int) -> bool:
        if not self.root:
            self.root = Node(startTime, endTime, None, None)
            return True
            
        return self.insert(self.root, startTime, endTime)
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)