## 项目由启动项目所需资金和利润组成
## 初始资金M0和最大投资项目个数K确定
## 求出投资可以获得的最大受益

## solution
## 所有项目按照启动所需资金进小根堆
## 每次投资时选出项目启动资金小于当前资金Mx的项目进入大根堆
## 大根堆按照利润进行排序
## 从大根堆中pop，即为选中的项目
## 循环
## 直到所选项目数量大于K或者大根堆为空

from pyHeap import MinHeap, MaxHeap

class Project_b:

    def __init__(self, p_list):
        self.b = p_list[0]
        self.p = p_list[1]
    
    def __lt__(self, p_node):
        return self.b < p_node.b
    

class Project_p:

    def __init__(self, p_list):
        self.b = p_list[0]
        self.p = p_list[1]
    
    def __lt__(self, p_node):
        return self.p < p_node.p

class Manager:

    def __init__(self, prj_list, M, K):
        self.M = M
        self.K = K
        self.prj_list = prj_list
        self.prj_minheap = MinHeap()
        self.prj_maxheap = MaxHeap()

    def add_all_prj_into_minheap(self):
        for prj in self.prj_list:
            self.prj_minheap.insert(prj)
        
    def run(self):
        self.add_all_prj_into_minheap()
        for i in range(self.K):
            while ((not self.prj_minheap.isEmpty()) and (self.prj_minheap.get_min().b <= self.M)):
                cur = self.prj_minheap.delete_min()
                if not cur == None:
                    self.prj_maxheap.insert(Project_p([cur.b, cur.p]))
            if self.prj_maxheap.isEmpty():
                return self.M
            else:
                self.M = self.M + self.prj_maxheap.delete_max().p
        return self.M


if __name__ == "__main__":
    prj_list = [Project_b([1, 3]), Project_b([2, 4]), Project_b([2, 1]), Project_b([3, 5])]
    manager = Manager(prj_list, 1, 3)
    print(manager.run())
