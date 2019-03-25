import csv
import os
import pandas as pd
outputFilePath="D://FYP/5mer/"
outputCSVPath="D://FYP/5merCSV/"

outputFileList=os.listdir(outputFilePath)
outputCSVFileList=os.listdir(outputCSVPath)


# Output to CSV Conversion

def text_to_csv():
    for outputFile in outputFileList:
        with open(outputFilePath+outputFile, 'r') as in_file:
            print(outputFile + "Started Conversion...")
            stripped = (line.strip() for line in in_file)
            lines = (line.split(" ") for line in stripped if line)
            with open(outputCSVPath+outputFile+'.csv', 'w') as out_file:
                writer = csv.writer(out_file)
                writer.writerow(('Kmer', 'Count'))
                writer.writerows(lines)
        print("outputFile" + "Started Conversion...")


def convert_csv_column_to_list(filename):
    data = pd.read_csv(filename)
    dataframe = pd.DataFrame(data)
    return list(dataframe['Kmer'])


#testing
# filename = 'D:/FYP/5merCSV/Ailuropoda_melanoleuca_GCF_000004335.2_AilMel_1.0_genomic_kmer_output.csv'
# print(convert_csv_column_to_list(filename))