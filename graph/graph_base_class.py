## import
import heapq

# base class of graph
class BaseGraph:
    def __init__(self):
        self.dict_nodes = {}
        self.list_edges = []

    def add_node(self, index, node):
        self.dict_nodes[index] = node
    
    def add_edges(self, edges):
        self.list_edges.append(edges)


    # class print and str method 
    def __str__(self):
        str_nodes = "Nodes in Graph:\n"
        #str_edges = ""
        for key, value in self.dict_nodes.items():
            str_nodes += str(value) + "*******************************\n"
        return str_nodes + "\n"

class BaseNode:

    def __init__(self, index):
        self.index = index
        self.in_num = 0
        self.out_num = 0
        self.next = []
        self.edges = []

    # class print and str method 
    def __str__(self):
        str_edges = ""
        str_next_nodes = "next-"
        for edge in self.edges:
            str_edges += str(edge)
        # for the index can represent the node, thus can use index 
        # there is no same index in a graph
        # is use next node, then str(node) -> for node in str(node) ->xxx, this will induce loop with no break
        for node in self.next:
            str_next_nodes += str(node.index)
        
        return "node-index:{}\t\tin_num:{}\t\tout_num:{}\n".format(self.index, self.in_num, self.out_num) + str_edges + str_next_nodes + "\n"

class BaseEdge:

    def __init__(self, weight, from_node, to_node):
        self.weight = weight
        self.from_node = from_node
        self.to_node = to_node

    # class print and str method 
    def __str__(self):
        return "edge-weight:{}\t\tdirection:{}->{}\n".format(self.weight, self.from_node.index, self.to_node.index)
    
    ## override the lt method for comparing 
    def __lt__(self, edge):
        return self.weight < edge.weight

## dict node:node set
class NodeSetDict:
    def __init__(self, nodes):
        self.node_set_dict=self.nodes2node_set_dict(nodes)
    
    def nodes2node_set_dict(self, nodes):
        node_set_dict = {}
        for indes, node in nodes.items():
            node_set_dict[node] = set([node])
        return node_set_dict
    
    def is_same_set(self, node1, node2):
        if ((self.node_set_dict[node1] & self.node_set_dict[node2]) == self.node_set_dict[node1]):
        # if ((self.node_set_dict[node1] == self.node_set_dict[node2])):
            return True
        else:
            return False

    def union(self, node1, node2):

        self.node_set_dict[node1].add(node2)
        self.node_set_dict[node2] = self.node_set_dict[node1]

    def union_ver1(self, node1, node2):
        self.node_set_dict[node1] = self.node_set_dict[node1] | self.node_set_dict[node2]
        self.node_set_dict[node2] = self.node_set_dict[node1]

##  convert a 2D list to base graph
## [[2, 1, 3], [4, 3, 4], [6, 4, 1]]
def convert_2D_list_to_base_graph_oriented(list_2d):
    result_graph = BaseGraph()
    for item in list_2d:
        item_weight = item[0]
        item_from = item[1]
        item_to = item[2]
        if (result_graph.dict_nodes.get(item_from) == None):
            result_graph.add_node(item_from, BaseNode(item_from))
        if (result_graph.dict_nodes.get(item_to) == None):
            result_graph.add_node(item_to, BaseNode(item_to))
        item_edge = BaseEdge(item_weight, result_graph.dict_nodes[item_from], result_graph.dict_nodes[item_to])
        result_graph.dict_nodes[item_from].next.append(result_graph.dict_nodes[item_to])
        result_graph.dict_nodes[item_from].out_num += 1
        result_graph.dict_nodes[item_to].in_num += 1
        result_graph.dict_nodes[item_from].edges.append(item_edge)
        result_graph.add_edges(item_edge)
    
    return result_graph

def convert_2D_list_to_base_graph(list_2d):
    result_graph = BaseGraph()
    for item in list_2d:
        item_weight = item[0]
        item_from = item[1]
        item_to = item[2]
        if (result_graph.dict_nodes.get(item_from) == None):
            result_graph.add_node(item_from, BaseNode(item_from))
        if (result_graph.dict_nodes.get(item_to) == None):
            result_graph.add_node(item_to, BaseNode(item_to))
        item_edge_1 = BaseEdge(item_weight, result_graph.dict_nodes[item_from], result_graph.dict_nodes[item_to])
        item_edge_2 = BaseEdge(item_weight, result_graph.dict_nodes[item_to], result_graph.dict_nodes[item_from])
        result_graph.dict_nodes[item_from].next.append(result_graph.dict_nodes[item_to])
        result_graph.dict_nodes[item_from].out_num += 1
        result_graph.dict_nodes[item_to].in_num += 1
        result_graph.dict_nodes[item_from].edges.append(item_edge_1)
        result_graph.dict_nodes[item_to].edges.append(item_edge_2)        
        result_graph.add_edges(item_edge_1)
        result_graph.add_edges(item_edge_2)       
    
    return result_graph


## graph BFS algorithm
## define a set to make sure that evary element is ergodic once
def graph_BFS(node):
    node_list = []
    node_set = set()
    node_list.insert(0, node)
    node_set.add(node)
    while node_list:
        cur_node = node_list.pop()
        ## process
        print(cur_node)
        ## process
        for n_node in cur_node.next:
            if (n_node not in node_set):
                node_set.add(n_node)
                node_list.insert(0, n_node)

## graph DFS algorthm
def graph_DFS(node):
    nodes_stack = []
    nodes_set = set()
    print(node)
    nodes_stack.append(node)
    nodes_set.add(node)
    while nodes_stack:
        cur_node = nodes_stack.pop()
        for n_node in cur_node.next:
            if n_node not in nodes_set:
                nodes_stack.append(cur_node)
                nodes_set.add(n_node)
                print(n_node)
                nodes_stack.append(n_node)
                break


## Topology sort
## 依次找入度为零的node，将该node加入到result，并擦除该node和该node带给其他node的入度影响
def topology_sort(graph):
    node_inNum = {}
    zero_inNum_node_queue = []

    for index, node in graph.dict_nodes.items():
        node_inNum[node] = node.in_num
        if node_inNum[node] == 0:
            zero_inNum_node_queue.insert(0, node)

    while zero_inNum_node_queue:
        cur_node = zero_inNum_node_queue.pop()
        print(cur_node)
        for n_node in cur_node.next:
            node_inNum[n_node] = node_inNum[n_node] - 1
            if node_inNum[n_node] == 0:
                zero_inNum_node_queue.insert(0, n_node)
            

## 最小生成树，要求无向图，保证连通性的前提下，所有边的权重之和最小
## kruskal算法
def kruakalMST(graph):

    ## 根据图生成node:set map
    set_map = NodeSetDict(graph.dict_nodes)
    ## 生成小根堆，实现从小到大遍历
    edges = [edge for edge in graph.list_edges]
    heapq.heapify(edges)
    ## 遍历小根堆中的每个edge
    result = []
    while len(edges) != 0:
        cur_edge = heapq.heappop(edges)
        from_node = cur_edge.from_node
        to_node = cur_edge.to_node
        if (set_map.is_same_set(from_node, to_node) == False):
            set_map.union(from_node, to_node)
            result.append(cur_edge)

    return result

## 最小生成数
## prim算法
def primMST(graph):

    node_processed = set()
    result = []
    heap_queue = []
    heapq.heapify(heap_queue)
    for index, cur_node in graph.dict_nodes.items():
        if (cur_node not in node_processed):
            node_processed.add(cur_node)
            for cur_edge in cur_node.edges:
                heapq.heappush(heap_queue, cur_edge)
            while len(heap_queue) != 0:
                min_edge = heapq.heappop(heap_queue)
                if (min_edge.to_node not in node_processed):
                    node_processed.add(min_edge.to_node)
                    for edge in min_edge.to_node.edges:
                        heapq.heappush(heap_queue, edge)
                    result.append(min_edge)

    return result


## dijkstra 算法
## 给点一个起点，输出该起点到所有node的最小距离
def dijkstra(node):
    ## create a dict: node-destence
    result = {}
    node_stack_poped = set()

    ## add start node into result
    result[node] = 0
    node = get_min_distence_unselected_node(result, node_stack_poped)

    while node != None:
        for edge in node.edges:
            if (edge.to_node != node):
                if (edge.to_node not in result.keys()):
                    result[edge.to_node] = edge.weight + result[edge.from_node]
                    print(edge.to_node.index, result[edge.to_node])
                else:
                    result[edge.to_node] = min(edge.weight + result[edge.from_node], result[edge.to_node])
                    print(edge.to_node.index, result[edge.to_node])
        node_stack_poped.add(node)
        node = get_min_distence_unselected_node(result, node_stack_poped)
    return result

## 得到当前node_processed中没有锁定的项中距离最小的节点
## node_processed表示项
## node_stack_poped表示已经锁定/处理完毕的项
def get_min_distence_unselected_node(result, node_stack_poped):
    min_distence = float("inf")
    min_node = None
    for node, distence in result.items():
        if node not in node_stack_poped:
            if min_distence > distence:
                min_distence = distence
                min_node = node

    return min_node
            






if __name__ == "__main__":
    dijk_data = [[9, 'a', 'd'], [15, 'a', 'c'], [3, 'a', 'b'], [16, 'd', 'e'], [14, 'c', 'e'], [200, 'b', 'e'], [7, 'd', 'c'], [2, 'c', 'b']]
    data_1 = [[2, 'a', 'c'], [4, 'c', 'd'], [7, 'a', 'b'], [100, 'a', 'd'], [1000, 'b', 'd'], [10, 'b', 'e'], [34, 'ff', 'dd']]
    test_name = "dijk"
    graph = convert_2D_list_to_base_graph([[9, 'a', 'd'], [15, 'a', 'c'], [3, 'a', 'b'], [16, 'd', 'e'], [14, 'c', 'e'], [200, 'b', 'e'], [7, 'd', 'c'], [2, 'c', 'b']])
    print(graph)
    if test_name == "bfs":
        graph_BFS(graph.dict_nodes[1])
    if test_name == "dfs":
        graph_DFS(graph.dict_nodes[1])
    if test_name == "toposort":
        topology_sort(graph)
    if test_name == "mst":
        [print(edge) for edge in kruakalMST(graph)]
        [print(edge) for edge in primMST(graph)]
    if test_name == "dijk":
        for key, value in dijkstra(graph.dict_nodes['a']).items():
            print("---------\n", key.index, value)




    