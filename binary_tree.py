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

    def get_children(self, index):
        child1 = index * 2
        child2 = child1 + 1
        ret = list()
        if child1 < len(self.data):
            ret.append(self.data[child1])
        if child2 < len(self.data):
            ret.append(self.data[child2])
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


if __name__ == '__main__':

    tree = BTree()

    NUM = 0
    # print(f"{sys.argv=}")
    if len(sys.argv) == 2:

        NUM = int(sys.argv[1])

    for i in range(1, NUM + 1):
        tree.add(randint(-99, 99))

    print(f"<MAIN>{tree=} {tree.data=}<>\n")

    tree.pretty_print()
