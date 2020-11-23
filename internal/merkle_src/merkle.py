import internal.shared_function_src.shared_function as shared_function


class MerkleNode(object):
    def __init__(self, left, right, data):
        if left is None and right is None:
            self.data = shared_function.hash_string(f"{data}")
        else:
            self.data = shared_function.hash_string(f"{left.data}{right.data}")
        self.left = left
        self.right = right


class MerkleTree(object):
    def __init__(self, data_list):
        nodes = []
        if len(data_list) % 2 != 0:
            data_list.append(data_list[-1])
        for data in data_list:
            nodes.append(MerkleNode(None, None, data))
        for _ in range(len(data_list)//2):
            new_level = []
            for j in range(0, len(nodes), 2):
                node = MerkleNode(nodes[j], nodes[j+1], None)
                new_level.append(node)
            nodes = new_level
        self._root = nodes[0]

    @property
    def root(self):
        return self._root

    @property
    def root_hash(self):
        return self._root.data

