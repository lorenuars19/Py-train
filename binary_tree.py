class BTree:
    def __init__(self):
        self.data = [0]

    def push(self, value):
        self.data.append(value)

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


if __name__ == '__main__':

    tree = BTree()
    for i in range(1, 10 + 1):
        tree.push(i)

    print(f"{tree=} {tree.data=}")

    for i in range(1, 10 + 1):
        print(f"{tree.get_parent(i)=}")
        print(f"{tree.get_children(i)=}")
