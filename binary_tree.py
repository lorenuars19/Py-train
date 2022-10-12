import math
from random import randint
import sys


class BTree:
    def __init__(self):
        self.data = [0, None]
        self.depth = 0
        self.last_idx = 1

    def add(self, value):
        if self.depth == 0:
            self.depth = 1
        if self.last_idx >= len(self.data):
            self.depth += 1
        next_len = 1 + round(math.pow(2, self.depth))
        if self.last_idx < next_len:
            while len(self.data) < next_len - 1:
                self.data.append(None)
        self.data[self.last_idx] = value
        self.last_idx += 1

    def get_parent(self, index):
        return self.data[index // 2]

    def get_parent_idx(self, index):
        return index // 2

    def get_children(self, index):
        child1 = index * 2
        child2 = child1 + 1
        ret = list()
        if child1 < len(self.data) and self.data[child1] != None:
            ret.append(self.data[child1])
        if child2 < len(self.data) and self.data[child2] != None:
            ret.append(self.data[child2])
        return ret

    def get_children_idx(self, index):
        child1 = index * 2
        child2 = child1 + 1
        ret = list()
        if child1 < len(self.data) and self.data[child1] != None:
            ret.append(child1)
        if child2 < len(self.data) and self.data[child2] != None:
            ret.append(child2)
        return ret

    def pretty_print(self):
        number_len = 3
        max_nodes = (round(pow(2, self.depth - 1)))
        max_line_len = number_len * ((max_nodes * 2) - 1)
        print(self.data)
        print("-" * (max_line_len), "TREE")
        if self.depth == 0:
            print("EMPTY TREE")
            return

        for stage in range(1, self.depth + 1):
            start_idx = pow(2, stage - 1)
            if self.depth == 1:
                start_idx = 1
            end_idx = 2
            if self.depth > 1:
                end_idx = pow(2, stage)
            if self.depth == 1:
                end_idx = 2
            stage_nodes = self.data[start_idx:end_idx]

            space_num = round(max_line_len / pow(2, stage - 1)) - number_len

            init_space_num = round(max_line_len / pow(2, stage)) - 1

            # print(f"{max_line_len=} {max_nodes=}")

            print(" " * init_space_num, end='')
            for idx, node in enumerate(stage_nodes):
                if idx > 0:
                    print(" " * space_num, end='')
                if node:
                    print(f"{node:0>{number_len}}", end='')
                if not node:
                    print("-" * number_len, end='')
            if stage < self.depth:
                print("", end="\n")
                print(" " * init_space_num, end='')
                for idx, node in enumerate(stage_nodes):
                    if idx > 0:
                        print(" " * space_num, end='')
                    lines = "/ \\"
                    print(f"{lines:^{number_len}}", end='')
            print("", end="\n")
        print("-" * (max_line_len), "TREE")


class Heap(BTree):

    def push(self, value):
        idx = 1

        children = self.get_children_idx(idx)
        # print(f"{children=}")
        while len(children) > 0:
            # children = self.get_children(idx)
            self._siftdown(idx)

    def pop(self):
        print("POP")
        return None

    def peek(self):
        print("PEEK")
        return None

    def _swap(self, src_idx, dst_idx):
        tmp = self.data[src_idx]
        self.data[src_idx] = self.data[dst_idx]
        self.data[dst_idx] = tmp
        print("_swap", src_idx, dst_idx)

    def _siftdown(self, idx):
        cur = self.data[idx]
        children = self.get_children_idx(idx)

        for i in children:
            if cur < self.data[i]:
                print("cur is smaller than children")
            elif cur > self.data[i]:
                print("cur is larger than children")

        print("_siftdown", idx)

    def _siftup(self, idx):
        print("_siftup", idx)


if __name__ == '__main__':

    tree = BTree()

    NUM = 0
    # print(f"{sys.argv=}")
    if len(sys.argv) == 2:
        NUM = int(sys.argv[1])

    # for i in range(1, NUM + 1):
    #     tree.add(randint(-99, 99))

    for i in range(1, NUM + 1):
        tree.add(i)
    tree.pretty_print()

    h = Heap()
    for i in range(1, NUM + 1):
        h.push(i)
    h.pretty_print()
