import json
import sys
from typing import List

from src.DiGraph import DiGraph
from src.Edge import Edge
from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: DiGraph):
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name, "r") as fp:
                di = json.load(fp)
                for i in di["Edges"]:
                    e = Edge(**i)
                    self.graph.add_edge(e.get_src(), e.get_dest(), e.get_weight())
                for i in di["Nodes"]:
                    pos = tuple(map(float, i["pos"].split(',')))
                    self.graph.add_node(i["id"], pos)
                return True
        except IOError as e:
            print(e)
            return False

    def save_to_json(self, file_name: str) -> bool:
        try:
            with open(file_name, "w") as outfile:
                Nodes = []
                Edges = []
                for i in self.graph.edges:
                    for j in self.graph.edges.get(i).values():
                        temp = {"src": j.get_src(), "w": j.get_weight(), "dest": j.get_dest()}
                        Edges.append(temp)
                for i in self.graph.nodes:
                    pos_tuple = self.graph.nodes.get(i).get_location()
                    pos = ','.join(tuple(map(str, pos_tuple)))
                    Nodes.append(
                        {"pos": pos, "id": self.graph.nodes.get(i).get_key()})
                dictionary = {"Edges": Edges, "Nodes": Nodes}
                outfile.write(json.dumps(dictionary, indent=1))
            return True
        except IOError as e:
            print(e)
            return False

        pass

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        ans = []
        n = self.graph.v_size()
        dis = [[0 for x in range(n)] for y in range(n)]
        nex = [[0 for x in range(n)] for y in range(n)]
        mat = [[0 for x in range(n)] for y in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    mat[i][j] = 0
                else:
                    mat[i][j] = sys.float_info.max
        for i in self.graph.edges:
            for j in self.graph.edges.get(i):
                mat[i][j] = self.graph.edges.get(i).get(j).get_weight()

        for i in range(n):
            for j in range(n):
                dis[i][j] = mat[i][j]
                if mat[i][i] == sys.float_info.max:
                    mat[i][j] = -1
                else:
                    nex[i][j] = j

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dis[i][k] + dis[k][j] < dis[i][j]:
                        dis[i][j] = dis[i][k] + dis[k][j]
                        nex[i][j] = nex[i][k]

        dist = dis[id1][id2]
        if nex[id1][id2] == -1:
            return -1, None

        ans.append(id1)
        while id1 != id2:
            id1 = nex[id1][id2]
            ans.append(id1)

        if dist == sys.float_info.max:
            ans = None
        return dist, ans

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        n = self.graph.v_size()
        mat = [[0 for x in range(n)] for y in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    mat[i][j] = 0
                else:
                    mat[i][j] = sys.float_info.max
        for i in self.graph.edges:
            for j in self.graph.edges.get(i):
                mat[i][j] = self.graph.edges.get(i).get(j).get_weight()
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if mat[i][k] + mat[k][j] < mat[i][j]:
                        mat[i][j] = mat[i][k] + mat[k][j]

        counter = 0
        j = 0
        i = 0
        list_size = len(node_lst)
        MIN = sys.float_info.min
        visited = [node_lst[0]]
        route = [0 for x in range(n)]
        while i < list_size and j < list_size:
            if counter >= list_size - 1:
                break
            # if node_lst[j] < len(visited):
            # if j != i and visited.__contains__(node_lst[j]) is False:
            if j != i and not (node_lst[j] in visited):
                if mat[i][j] < MIN:
                    MIN = mat[i][j]
                    route[counter] = j + 1
            j += 1
            if j == list_size:
                MIN = sys.float_info.max
                visited.append(node_lst[route[counter] - 1])
                j = 0
                i = route[counter] - 1
                counter += 1
        for k in range(list_size):
            if i != k and mat[i][k] < MIN:
                MIN = mat[i][k]
                route[counter] = k + 1

        return visited

    def centerPoint(self) -> (int, float):
        n = self.graph.v_size()
        D = [[0 for x in range(n)] for y in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    D[i][j] = 0
                else:
                    D[i][j] = sys.float_info.max
        for i in self.graph.edges:
            for j in self.graph.edges.get(i):
                D[i][j] = self.graph.edges.get(i).get(j).get_weight()

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if D[i][k] + D[k][j] < D[i][j]:
                        D[i][j] = D[i][k] + D[k][j]

        temp = [0 for x in range(n)]
        for i in range(n):
            temp[i] = 0
            for j in range(n):
                if temp[i] < D[i][j]:
                    temp[i] = D[i][j]

        MAX = sys.float_info.max
        for i in range(n):
            if MAX > temp[i]:
                MAX = temp[i]
        for i in range(n):
            if temp[i] == MAX:
                return i
        return None

    def plot_graph(self) -> None:
        pass


if __name__ == '__main__':
    g = DiGraph()
    g_algo = GraphAlgo(g)
    # g_algo.load_from_json("C:\\Users\\TamarD\\PycharmProjects\\Ex3\\data\\A0.json")
    # g_algo.save_to_json("save.json")

    g_algo.get_graph().add_node(0, (0, 0, 0))
    g_algo.get_graph().add_node(1)
    g_algo.get_graph().add_node(2)
    g_algo.get_graph().add_edge(0, 1, 1)
    g_algo.get_graph().add_edge(1, 2, 4)
    print(g_algo.TSP([0, 1, 2]))
    # # (1, [0, 1])
    # print(g_algo.shortest_path(0, 2))
    # # (5, [0, 1, 2])
    # # print(a.shortest_path(0, 2))
