#!/bin/bash

# Import Properties File
. ./startup.properties
 
for file in ${GENOME_DIRECTORY}/left/*.fna; do

     # keep the .fna file name
     fileName="$(basename -- $file)"

     # extension removal
     specieName="${fileName%.*}"

     #construct .h5 file name according to specie
     outputH5Name=${specieName}"_output"

     #construct kmer txt file name according to specie
     outputKmerSpecieName=${specieName}"_kmer_output"

     echo ${fileName}"_Kmer counting started.."

     #mkdir ${OUTPUT_DIRECTORY}/H5outputs
     #mkdir ${OUTPUT_DIRECTORY}/KMERoutputs

     # DSK tool .h5 intermediate file construction
     ./dsk -nb-cores 4 -max-memory 12000 -file ${GENOME_DIRECTORY}/left/${fileName} -kmer-size 5 -out ${OUTPUT_DIRECTORY}/H5outputs/5mer/${outputH5Name}

     # DSK tool kmer txt file construction
     ./dsk2ascii -file ${OUTPUT_DIRECTORY}/H5outputs/5mer/${outputH5Name} -out ${OUTPUT_DIRECTORY}/KMERoutputs/5mer/${outputKmerSpecieName}

     echo ${fileName}"_Kmer counting Finished.."	
done
     
	







