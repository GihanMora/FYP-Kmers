from skbio import Sequence
import skbio
from datetime import datetime
import os
import numpy as np





class Specie:
    def __init__(self, name, kmer_list):
        self.name = name
        self.kmer_list = kmer_list
        self.kmer_tree = None

class Node:
    def __init__(self, letter):
        self.letter = letter
        self.next_nodes = {}

    def set_next(self, node):
        self.next_nodes[node.letter] = node

    def __repr__(self):
        return "letter - "+self.letter+" next nodes -"+str(self.next_nodes)


class Tree:
    def __init__(self,name):
        self.root = {}
        self.name = name

    def add_kmer(self, kmer):
        if not kmer[0] in self.root:
            self.root[kmer[0]] = Node(kmer[0])

        ptr = self.root[kmer[0]]
        itr = 1

        while itr < len(kmer):

            if kmer[itr] not in ptr.next_nodes:
                ptr.next_nodes[kmer[itr]] = Node(kmer[itr])
            ptr = ptr.next_nodes[kmer[itr]] #put out of the loop
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


def tree_construction(Specie):
    tree = Tree(Specie.name)
    for each_kmer in Specie.kmer_list:
        tree.add_kmer(each_kmer)
    Specie.kmer_tree = tree

def Specie_comparision(Specie1,Specie2):
    kmer_hits =0
    for each_kmer in Specie1.kmer_list:
        if(Specie2.kmer_tree.has_kmer(each_kmer)):
            kmer_hits+=1
    return kmer_hits









#testing

# t= datetime.now()
# print(len(seq1_kmers.intersection(seq2_kmers)))
# print(datetime.now()-t)
# # print(seq1_kmers)
# # print(seq2_kmers)
# t= datetime.now()
# t1 = Tree()
# t2 = Tree()
#
# for i in seq1_kmers:
#     t1.add_kmer(i)
#
#
# for i in seq2_kmers:
#     t2.add_kmer(i)






# count=0
# for i in seq1_kmers:
#     if (t2.has_kmer(i)):
#         count+=1
#
#
#
#
# print(count,len(seq1_kmers))
# print(datetime.now()-t)
# # print(t.has_kmer('ACGT'))
# # print(t.has_kmer('ATGT'))
#
# print(t1.root)
# print(t2.root)