## 找到任意数据流的中位数
from pyHeap import MinHeap, MaxHeap

class FindMedian:

    def __init__(self):
        self.lq_half_part = MaxHeap()
        self.bq_half_part = MinHeap()

    def insert(self, num):
        ## put this num 
        if self.lq_half_part.size() == 0:
            self.lq_half_part.insert(num)
        elif (num > self.lq_half_part.get_max()):
            self.bq_half_part.insert(num)
        elif (num <= self.lq_half_part.get_max()):
            self.lq_half_part.insert(num)
        
        ## 
        if self.bq_half_part.size() - self.lq_half_part.size() >= 2:
            self.lq_half_part.insert(self.bq_half_part.delete_min())
        elif (self.lq_half_part.size() - self.bq_half_part.size() >= 2):
            self.bq_half_part.insert(self.lq_half_part.delete_max())
        else:
            pass

    def get_median(self):
        if self.bq_half_part.size() == self.lq_half_part.size():
            return ((self.bq_half_part.get_min() + self.lq_half_part.get_max()) / 2)
        elif (self.bq_half_part.size() > self.lq_half_part.size()):
            return self.bq_half_part.get_min()
        elif (self.lq_half_part.size() > self.bq_half_part.size()):
            return self.lq_half_part.get_max()
        


if __name__ == "__main__":
    finder = FindMedian()

    finder.insert(3)
    finder.insert(4)
    finder.insert(1)
    finder.insert(8)
    finder.insert(4)
    finder.insert(9)
    finder.insert(12)
    finder.insert(6)
    finder.insert(8)
    finder.insert(6)
    print(finder.get_median())
    print(finder.bq_half_part.size())
    print(finder.lq_half_part.size())
    
