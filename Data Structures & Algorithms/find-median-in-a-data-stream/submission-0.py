class MedianFinder:

    def __init__(self):
        self.heap = []
        

    def addNum(self, num: int) -> None:
        self.heap.append(num)
        self.heap.sort()

    def findMedian(self) -> float:
        n = len(self.heap)
        if n%2 == 1:
            return self.heap[n//2]
        return (self.heap[(n//2)-1]+self.heap[n//2])/2
        
        