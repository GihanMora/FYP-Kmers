from Data_Pre_Processing.specie_creation import specie_list
from Data_Pre_Processing.Kmer_indexing import Specie_comparision



for i,specie1 in enumerate(specie_list):
    for specie2 in specie_list[i:]:
        print(specie1.name,specie2.name,specie1.kmer_tree.root,specie2.kmer_tree.root)
        # print(set(specie1.kmer_list)-set(specie2.kmer_list))
