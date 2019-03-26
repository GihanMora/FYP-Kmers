import os

from Data_Pre_Processing.Kmer_indexing import Specie,tree_construction
from Data_Pre_Processing.CSV_operations import convert_csv_column_to_list

print("Specie Creation started...")
csv_file_list_path = "/home/castle/FYP-KMER/KMERData_Results/KMERoutputs/13mer/CSV/"
CSVFileList=os.listdir(csv_file_list_path)
specie_list=[]
for each_CSV_file in CSVFileList:
    specie_name = each_CSV_file.split('_GCF')[0].split('_kmer')[0]
    print(specie_name)

    kmer_list=convert_csv_column_to_list(csv_file_list_path+each_CSV_file)
    print(len(kmer_list))
    new_specie = Specie(specie_name, kmer_list)
    # tree_construction(new_specie)
    specie_list.append(new_specie)
    print("1 done...")
print(len(set(specie_list[0].kmer_list)-set(specie_list[1].kmer_list)))