
import os

# detect the genome Kmer working directory
#path =

# read the entries
with os.scandir(path) as listOfEntries:
    for entry in listOfEntries:
        # print all entries that are files
        if entry.is_file():
            print(entry.name)

# kmer_Count_file_Homo = open('/home/castle/FYP-KMER/KMERData_Results/Homo_Sapien/output.txt')
# kmer_Count_file_Macaca = open('/home/castle/FYP-KMER/KMERData_Results/Macaca_mulatta/result.txt')
#
# kmer_Homo_ReadLineArray = kmer_Count_file_Homo.readlines()
# kmer_Macaca_ReadLineArray = kmer_Count_file_Macaca.readlines()
#
# homo_Kmer_array = []
# Macaca_Kmer_array =[]
#
# for eachKmerCount in kmer_Homo_ReadLineArray:
#     homo_Kmer_array.append(eachKmerCount.split(" ")[0])
#
# for eachKmerCount in kmer_Macaca_ReadLineArray:
#     Macaca_Kmer_array.append(eachKmerCount.split(" ")[0])
#
# print(Macaca_Kmer_array)
# print(homo_Kmer_array)