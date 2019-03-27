import datetime
import os
import gc
import pickle

from Data_Pre_Processing.Kmer_indexing import Specie,tree_construction
from Data_Pre_Processing.CSV_operations import convert_csv_column_to_list
from Data_Pre_Processing.Kmer_indexing import Specie_comparision

print("Specie Creation started...")
#csv_file_list_path = "/home/castle/FYP-KMER/KMERData_Results/KMERoutputs/13mer/CSV/"
csv_file_list_path = "/home/castle/FYP-KMER/KMERData_Results/KMERoutputs/13mer/CSV/test/"
CSVFileList=os.listdir(csv_file_list_path)
specie_list=[]
time1=datetime.datetime.now()
print(time1)
for each_CSV_file in CSVFileList:
    specie_name = each_CSV_file.split('_GCF')[0].split('_kmer')[0]
    print(specie_name)
    kmer_list=convert_csv_column_to_list(csv_file_list_path+each_CSV_file)
    print(len(kmer_list))


    new_specie = Specie(specie_name,kmer_list)
    tree_construction(new_specie)


    specieTemp = pickle.dumps(new_specie)
    print(specieTemp)


    specie_list.append(new_specie)
    elapsed_time = datetime.datetime.now()-time1
    print("1 done..."+str(elapsed_time))
    # print("comparison")
    # time2 = datetime.datetime.now()
    #
    # c_kmers=Specie_comparision(specie_list[0], specie_list[0])
    # elapsed_time1 = datetime.datetime.now() - time2
    # print("1 done..." +str(c_kmers)+" ,, "+ str(elapsed_time1))
    # gc.collect()


