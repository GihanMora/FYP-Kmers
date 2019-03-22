import csv
import os

outputFilePath="/home/castle/FYP-KMER/KMERData_Results/KMERoutputs/"
outputCSVPath="/home/castle/FYP-KMER/KMERData_Results/CSV/"

outputFileList=os.listdir(outputFilePath)
outputCSVFileList=os.listdir(outputCSVPath)

# Output to CSV Conversion
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

# CSV File Reading
# for outputCSVFile in outputCSVFileList:
#     with open(outputCSVPath+outputCSVFile+'.csv', 'r') as csvFile:
#         reader = csv.reader(csvFile)
#         for row in reader:
#             print(row)
#     csvFile.close()