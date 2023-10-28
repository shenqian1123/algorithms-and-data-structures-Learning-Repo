## 前缀树
## 查询字符串出现了几次
## 查询以"xx"开头的字符串出现了几次

class TriNode:

    def __init__(self):
        self.pass_num = 0
        self.end_num = 0
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

    def __str__(self):
        node_queue = []
        node_queue.insert(0, self.root)
        node_str = ""
        while node_queue:
            node = node_queue.pop()
            node_str += "N({}, {})".format(node.pass_num, node.end_num)
            for index, n_node in enumerate(node.next):
                if n_node != []:
                    index_chr = index + 97
                    node_str += "-L[{}]".format(chr(index_chr))
                    node_queue.insert(0, n_node)
        return node_str
    



if __name__ == "__main__":
    tree = TriTree(TriNode())
    tree.insert("hello")
    tree.insert("good")
    print(tree)
            

