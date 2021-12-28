import random


class Node:
    def __init__(self, pos: tuple, id: int):
        if pos is None:
            pos = (random.uniform(35.000, 35.30), random.uniform(32.000, 32.30))
        self.pos = pos  # tuple
        self.id = id
        self.in_edges = []
        self.out_edges = []

    def __int__(self, id: int):
        self.id = id

    def add_in(self, key: int):
        self.in_edges.append(key)

    def add_out(self, key: int):
        self.out_edges.append(key)

    def get_x(self):
        if self.pos is not None:
            return self.pos[0]
        return None

    def get_y(self):
        if self.pos is not None:
            return self.pos[1]
        return None

    def get_key(self) -> int:
        return self.id

    def get_location(self) -> tuple:
        return self.pos

    def set_location(self, p: tuple):
        self.pos = p

    #  {0: 0: |edges_out| 1 |edges in| 1, 1: 1: |edges_out| 3 |edges in| 1, 2: 2: |edges_out| 1 |edges in| 1, 3: 3: |edges_out| 0 |edges in| 2}
    def __str__(self) -> str:
        _in = ""
        _out = ""
        for i in self.in_edges:
            _in += ", " + i
        for i in self.out_edges:
            _out += ", " + i
        return f"{self.id}: |edges_out| {_out} |edges_in| {_in}"

    def __repr__(self) -> str:
        return f"{self.id}: |edges_out| {self.out_edges} |edges_in| {self.in_edges}"
