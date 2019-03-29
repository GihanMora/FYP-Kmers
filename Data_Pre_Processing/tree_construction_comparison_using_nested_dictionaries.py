import datetime
import os
from Data_Pre_Processing.CSV_operations import convert_csv_column_to_list
from Data_Pre_Processing.Kmer_indexing import Tree

# test1= { 'G': {'C': {'C': {},'A':{}}},'A': {'C': {'C': {},'T': {}}}}
# test2= { 'A': {'C': {'G': {}}}}


def add_kmer1(dict, kmer):
        if not kmer[0] in dict.keys():
            dict[kmer[0]]={}

        ptr = dict[kmer[0]]
        itr = 1
        while itr < len(kmer):
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



def tree_construction1(Specie):
    tree = Tree(Specie.name)
    for each_kmer in Specie.kmer_list:
        tree.add_kmer(each_kmer)
    Specie.kmer_tree = tree

def get_child_count(d):
    cnt = 0
    for e in d:
        if d[e] !={}:
            cnt += get_child_count(d[e])
        else:
            cnt += 1
    return cnt
class Summer:
    def __init__(self):
        self.summing = 0


def nested_tree_comparison(dict1,dict2,summ):

    for k in dict1.keys():
        if (k not in dict2.keys()):
            if(dict1[k]=={}):
                summ.summing+=1
            else:
                summ.summing += get_child_count(dict1[k])
        else:

            nested_tree_comparison(dict1[k], dict2[k],summ)

csv_file_list_path = "/home/castle/FYP-KMER/KMERData_Results/KMERoutputs/13mer/CSV/test/"
CSVFileList=os.listdir(csv_file_list_path)
specie_list=[]
time1=datetime.datetime.now()
print("started at : "+str(time1))
all_dicts=[]
k_lists = []
for each_CSV_file in CSVFileList:
    print
    specie_name = each_CSV_file.split('_GCF')[0].split('_kmer')[0]
    print(specie_name)
    kmer_list=convert_csv_column_to_list(csv_file_list_path+each_CSV_file)
    k_lists.append(kmer_list)
    dict = {}
    time1 = datetime.datetime.now()
    for each_kmer in kmer_list:
        add_kmer1(dict,each_kmer)
    print("done")
    time2 = datetime.datetime.now()
    print("tree construction finished : "+str(time2-time1))
    all_dicts.append(dict)


    #comparison by iterating all kmers
    # count = 0
    # for each_kmer in kmer_list:
    #     if(has_kmer(dict, each_kmer)):
    #         count=count+1
    # print(count)

time22 = datetime.datetime.now()
print(all_dicts[1].keys())

#new tree comparison method
summ = Summer()
nested_tree_comparison(all_dicts[0], all_dicts[1],summ)
time3 = datetime.datetime.now()
print(summ.summing)
print(time3 - time22)

#tree comparison using set intersection method
time4 = datetime.datetime.now()
print(len(set(k_lists[0])-set(k_lists[1])))
print(datetime.datetime.now() - time4)