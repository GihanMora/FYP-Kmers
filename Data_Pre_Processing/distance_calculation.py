from Data_Pre_Processing.specie_creation import specie_list
from Data_Pre_Processing.Kmer_indexing import Specie_comparision



for i,specie1 in enumerate(specie_list):
    for specie2 in specie_list[i:]:
        print(specie1.name,specie2.name,Specie_comparision(specie1,specie2))
        # print(set(specie1.kmer_list)-set(specie2.kmer_list))
