import datetime
import os

from Data_Pre_Processing.CSV_operations import convert_csv_column_to_list
from Data_Pre_Processing.Kmer_indexing import Tree

nested_dict1 = { 'A': {'C': {'C': {'A':{}}}},
                'G': {'C': {'G': {'T':{}}}}}


nested_dict2 = { 'dictA': {'key_1': 'value_1'},
                'dictB': {'key_2': 'value_2'}}




def add_kmer1(dict, kmer):
        if not kmer[0] in dict.keys():
            dict[kmer[0]]={}

        ptr = dict[kmer[0]]
        itr = 1
        #
        while itr < len(kmer):
        #
            if kmer[itr] not in ptr.keys():
                ptr[kmer[itr]] = {}
            ptr = ptr[kmer[itr]]
            itr+=1




def has_kmer(dict, kmer):
        itr = 0

        if not kmer[0] in dict.keys():
            return False

        ptr = dict[kmer[0]]
        itr = 1

        while itr < len(kmer):

            if kmer[itr] not in ptr.keys():
                return False
            else:
                ptr = ptr[kmer[itr]]
                itr += 1
        return True

print(has_kmer(nested_dict1,'ACCA'))
print(nested_dict1)

def tree_construction1(Specie):
    tree = Tree(Specie.name)
    for each_kmer in Specie.kmer_list:
        tree.add_kmer(each_kmer)
    Specie.kmer_tree = tree


csv_file_list_path = "/home/castle/FYP-KMER/KMERData_Results/KMERoutputs/13mer/CSV/test/"
CSVFileList=os.listdir(csv_file_list_path)
specie_list=[]
time1=datetime.datetime.now()
print(time1)
for each_CSV_file in CSVFileList:
    specie_name = each_CSV_file.split('_GCF')[0].split('_kmer')[0]
    print(specie_name)
    kmer_list=convert_csv_column_to_list(csv_file_list_path+each_CSV_file)
    dict = {}
    time1 = datetime.datetime.now()
    for each_kmer in kmer_list:
        add_kmer1(dict,each_kmer)
    time2 = datetime.datetime.now()
    print("done")
    time2 = datetime.datetime.now()
    print(time2-time1)