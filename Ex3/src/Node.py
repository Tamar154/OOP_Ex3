class Node:
    def __init__(self, pos: tuple, id: int):
        self.pos = pos  # tuple
        self.id = id

    def get_key(self) -> int:
        return self.id

    def get_location(self) -> tuple:
        return self.pos

    def set_location(self, p: tuple):
        self.pos = p

    def __str__(self) -> str:
        return f"{self.id} , {self.pos}"

    def __repr__(self) -> str:
        return f"{self.id} , {self.pos}"
