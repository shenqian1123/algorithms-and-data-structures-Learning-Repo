## 前缀树
## 查询字符串出现了几次
## 查询以"xx"开头的字符串出现了几次

class TriNode:

    def __init__(self):
        self.pass_num = 0
        self.end_num = 0
        ## next 可以使用key-value类型的数据结构
        self.next_dict = {}
        self.next = [[] for _ in range(26)]


class TriTree:

    def __init__(self, root):
        self.root = root
        self.cur = root
    
    def insert(self, word):
        self.cur = self.root
        if word:
            for item in word:
                index = ord(item) - 97
                if (self.cur.next[index] == []):
                    self.cur.next[index] = TriNode()
                self.cur.pass_num += 1
                self.cur = self.cur.next[index]
            self.cur.end_num += 1
            self.cur.pass_num += 1

    def insert_dict(self, word):
        self.cur = self.root
        if word:
            for item in word:
                if self.cur.next[item] is None:
                    self.cur.next[item] = TriNode()
                self.cur.pass_num += 1
                self.cur = self.cur.next[item]
            self.cur.end_num += 1
            self.cur.pass_num += 1

    ## search 方法
    ## 查询一个单词出现的次数
    def search(self, word):
        self.cur = self.root
        for item in word:
            index = ord(item) - 97
            if (self.cur.next[index] == []):
                return 0
            self.cur = self.cur.next[index]
        return self.cur.end_num
    
    ## prefixNumber 
    ## 查询加入的字符串中有几个是以pre为前缀的
    def prefix_number(self, prefix):
        self.cur = self.root

        if prefix:
            for item in prefix:
                index = ord(item) - 97
                if (self.cur.next[index] == []):
                    return 0
                self.cur = self.cur.next[index]
        else:
            return 0
        return self.cur.pass_num
    
    ## delete 方法
    ## 从前缀树中删除一个word
    def delete(self, word):
        if self.search(word) != 0:
            self.cur = self.root
            self.cur.pass_num -= 1
            for item in word:
                index = ord(item) - 97
                ## 当删完单词的最后一个字母时恰好该节点的pass_num=0
                ## 需要从上一级节点删除这个节点
                if (self.cur.next[index].pass_num - 1 == 0):
                    self.cur.next[index] = []
                    return 1
                self.cur = self.cur.next[index]
                self.cur.pass_num -= 1
            self.cur.end_num -= 1
            return 1
        else:
            return 0
                



    ## 前缀树可视化
    ## 宽度优先遍历
    def __str__(self):
        node_queue = []
        node_queue.insert(0, self.root)
        node_str = ""
        while node_queue:
            node = node_queue.pop()
            node_str += "【节点】({}, {})".format(node.pass_num, node.end_num)
            for index, n_node in enumerate(node.next):
                if n_node != []:
                    index_chr = index + 97
                    node_str += "-边[{}]".format(chr(index_chr))
                    node_queue.insert(0, n_node)
        return node_str
    



if __name__ == "__main__":
    tree = TriTree(TriNode())
    tree.insert("hello")
    tree.insert("good")
    tree.insert("good")
    print("delete", tree.delete("good"))
    print("delete", tree.delete("hello"))
    tree.insert("good")
    tree.insert("good")
    print("search:", tree.search("good"))
    print("search", tree.search("hel"))
    tree.prefix_number("h")
    print(tree)
            

