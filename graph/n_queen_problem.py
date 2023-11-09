## n皇后问题
## 在n*n的棋盘上放置n个皇后，需要保证
## 1.n个皇后不同列
## 2.n个皇后不同行
## 3.n个皇后不同斜线(45°线)
import time


class NQSolver:

    def __init__(self, n, select):
        self.select = select
        self.n = n
        self.queen_pos = n*[0]
        self.limit = (1 << self.n) - 1

    def run(self):
        ## 处理输入的边界条件
        if (self.n < 1):
            return 0
        ## 处理n>=1
        ## 主函数，需要入参有
        ## 1.之前皇后填的位置，用一维数组维护
        ## 2.当前正在处理的行，也就是会在当前行进行放置皇后的尝试
        if self.select == 1:
            return self.processor1(0)
        elif self.select == 2:
            return self.processor2(0, 0, 0)
        else:
            print("wrong select arg !!!")
    
    def processor1(self, i):
        ## base case
        ## 当处理到i==n的时候，表明所有的皇后都已经填到棋盘中
        ## 即找到了一种皇后的排列方法
        if (i == self.n):
            return 1
        res = 0
        for j in range(self.n):
            if self.is_valid(j, i):
                self.queen_pos[i] = j
                res += self.processor1(i+1)
        return res
    
    def is_valid(self, cur_col, cur_row):
        ## 1.不同行天然满足
        ## 2.不同列
        ## 3.不同斜线
        for k in range(cur_row):
            if (self.queen_pos[k] == cur_col) or ((abs(self.queen_pos[k] - cur_col)) == (abs(k - cur_row))):
                return False
        return True

    ## 第二种解法，使用位运算，可以减小常数时间，入参
    ## 当前行的列限制
    ## 当前行的左对角线限制
    ## 当前行的右对角线限制
    def processor2(self, col_limit, left_limit, right_limit):
        ## base case
        ## 当col_limit全为1，表示所有的列被填了皇后
        if (col_limit == self.limit):
            return 1
        res = 0
        ## 找到可行的位置
        posibly_pos = self.limit & (~(col_limit | left_limit | right_limit))
        while (posibly_pos != 0):
            most_right_pos = posibly_pos & (~posibly_pos + 1)
            posibly_pos = posibly_pos - most_right_pos
            res += self.processor2(col_limit | most_right_pos, (left_limit | most_right_pos) << 1, (right_limit | most_right_pos) >> 1)
        return res
        



if __name__ == "__main__":
    t1 = time.perf_counter()
    finder1 = NQSolver(14, 1)
    print(finder1.run())
    print(f"coast:{time.perf_counter() - t1:.8f}s")

    
    t2 = time.perf_counter()
    finder2 = NQSolver(14, 2)
    print(finder2.run())
    print(f"coast:{time.perf_counter() - t2:.8f}s")
    
