## 给定一个数组，该数组的和为金条的总长度
## 数组中每个数字表示该金条需要被分成的大小
## 切割金条的代价是金条的长度
## 使用某种贪心策略找出完成切割所花费的最小代价
import heapq

class FindLessMoney:

    def __init__(self, length_list):
        self.len_list = length_list
        self.len_heap = None

    def put_len_item_into_heap(self):
        heapq.heapify(self.len_list)

    def run(self):
        ## 所有长度放到小根堆中去
        self.put_len_item_into_heap()
        result = 0
        while len(self.len_list) > 1:
            cur = heapq.heappop(self.len_list) + heapq.heappop(self.len_list)
            result = result + cur
            heapq.heappush(self.len_list, cur)
        print("Min Money is {}".format(result))


if __name__ == "__main__":
    finder = FindLessMoney([10, 20, 30])
    finder.run()