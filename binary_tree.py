import math
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
        print(
            f"{self.data=}\n  {self.depth=} {self.last_idx=} {next_len=} {len(self.data)=}<>\n")

        self.data[self.last_idx] = value
        self.last_idx += 1
        print(f"{self.data=} {self.last_idx=} {self.depth=}")

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
        number_len = 5
        max_nodes = 0

        print("-" * 20, "TREE", "-" * 20)

        for stage in range(self.depth + 1):
            start_idx = pow(2, stage)
            if self.depth == 1:
                start_idx = 0
            end_idx = 0
            if self.depth > 1:
                end_idx = pow(2, stage + 1) - 1
            if self.depth == 1:
                end_idx = 2
            stage_nodes = self.data[start_idx:end_idx + 1]

            space_num = abs(max_nodes - number_len)
            max_nodes = round(math.pow(2, (self.depth - stage)))
            init_space_num = max_nodes
            # print(f"{max_nodes=} {init_space_num=} {space_num=}")
            if stage < self.depth - 1:
                print(" " * init_space_num, end='')
            for idx, node in enumerate(stage_nodes):
                if idx > 0:
                    print(" " * space_num, end='')
                if node:
                    print(f"{node:^{number_len}}", end='')
                elif not node:
                    empty = "None"
                    # print("-" * number_len, end='')
                    print(f"{empty:0.{number_len}}", end='')
            if stage < self.depth - 1:
                print("", end="\n")
                print(" " * init_space_num, end='')
                for idx, node in enumerate(stage_nodes):
                    if idx > 0:
                        print(" " * space_num, end='')
                    lines = "/ \\"
                    print(f"{lines:^{number_len}}", end='')

            print("", end="\n")


if __name__ == '__main__':

    tree = BTree()

    NUM = 0
    # print(f"{sys.argv=}")
    if len(sys.argv) == 2:

        NUM = int(sys.argv[1])

    for i in range(1,
                   NUM + 1):
        tree.add(i)

    print(f"<MAIN>{tree=} {tree.data=}<>\n")

    tree.pretty_print()
