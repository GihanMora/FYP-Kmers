class Node:
    def __init__(self, letter):
        self.letter = letter
        self.next_nodes = {}

    def set_next(self, node):
        self.next_nodes[node.letter] = node


class Tree:
    def __init__(self):
        self.root = {}

    def add_kmer(self, kmer):
        if not kmer[0] in self.root:
            self.root[kmer[0]] = Node(kmer[0])

        ptr = self.root[kmer[0]]
        itr = 1

        while itr < len(kmer):
            if kmer[itr] not in ptr.next_nodes:
                ptr.next_nodes[kmer[itr]] = Node(kmer[itr])
                ptr = ptr.next_nodes[kmer[itr]]
                itr += 1

    def has_kmer(self, kmer):
        itr = 0

        if not kmer[0] in self.root:
            return False

        ptr = self.root[kmer[0]]
        itr = 1

        while itr < len(kmer):
            if kmer[itr] not in ptr.next_nodes:
                return False
            else:
                ptr = ptr.next_nodes[kmer[itr]]
                itr += 1
        return True


t = Tree()
t.add_kmer('ACGT')
t.add_kmer('GCGT')

print(t.has_kmer('ACGT'))
print(t.has_kmer('ATGT'))