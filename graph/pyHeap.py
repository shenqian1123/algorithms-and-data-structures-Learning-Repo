## heap python 
## those code is created by 文心一言
class MinHeap:  
    def __init__(self):  
        self.heap = []  
    
    def isEmpty(self):
        return len(self.heap) == 0
    
    def size(self):
        return len(self.heap)

    def parent(self, i):  
        return (i-1)//2  
  
    def left_child(self, i):  
        return 2*i + 1  
  
    def right_child(self, i):  
        return 2*i + 2  
  
    def get_min(self):  
        if self.heap:  
            return self.heap[0]  
        else:  
            return None  
  
    def insert(self, value):  
        self.heap.append(value)  
        self.heapify_up(len(self.heap)-1)  
  
    def delete_min(self):  
        if len(self.heap) > 1:  
            min_value = self.heap[0]  
            self.heap[0] = self.heap[-1]  
            del self.heap[-1]  
            self.heapify_down(0)  
            return min_value  
        elif len(self.heap) == 1:  
            min_value = self.heap[0]  
            del self.heap[0]  
            return min_value  
        else:  
            return None  
  
    def pop(self):  
        if len(self.heap) > 1:  
            min_value = self.heap[0]  
            self.heap[0] = self.heap[-1]  
            del self.heap[-1]  
            self.heapify_down(0)  
            return min_value  
        elif len(self.heap) == 1:  
            min_value = self.heap[0]  
            del self.heap[0]  
            return min_value  
        else:  
            return None  
  
    def peek(self):  
        if self.heap:  
            return self.heap[0]  
        else:  
            return None  
  
    def heapify_up(self, i):  
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:  
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]  
            i = self.parent(i)  
  
    def heapify_down(self, i):  
        smallest = i  
        l = self.left_child(i)  
        r = self.right_child(i)  
        if l < len(self.heap) and self.heap[l] < self.heap[smallest]:  
            smallest = l  
        if r < len(self.heap) and self.heap[r] < self.heap[smallest]:  
            smallest = r  
        if smallest != i:  
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]  
            self.heapify_down(smallest)


class MaxHeap:


    def __init__(self):  
        self.heap = []  

    def isEmpty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)

    def parent(self, i):  
        return (i-1)//2  
  
    def left_child(self, i):  
        return 2*i + 1  
  
    def right_child(self, i):  
        return 2*i + 2  
  
    def get_max(self):  
        if self.heap:  
            return self.heap[0]  
        else:  
            return None  
  
    def insert(self, value):  
        self.heap.append(value)  
        self.heapify_up(len(self.heap)-1)  
  
    def delete_max(self):  
        if len(self.heap) > 1:  
            max_value = self.heap[0]  
            self.heap[0] = self.heap[-1]  
            del self.heap[-1]  
            self.heapify_down(0)  
            return max_value  
        elif len(self.heap) == 1:  
            max_value = self.heap[0]  
            del self.heap[0]  
            return max_value  
        else:  
            return None  
  
    def heapify_up(self, i):  
        while i > 0 and self.heap[i] > self.heap[self.parent(i)]:  
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]  
            i = self.parent(i)  
  
    def heapify_down(self, i):  
        smallest = i  
        l = self.left_child(i)  
        r = self.right_child(i)  
        if l < len(self.heap) and self.heap[l] > self.heap[smallest]:  
            smallest = l  
        if r < len(self.heap) and self.heap[r] > self.heap[smallest]:  
            smallest = r  
        if smallest != i:  
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]  
            self.heapify_down(smallest)