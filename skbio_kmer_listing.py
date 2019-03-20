from skbio import Sequence
import skbio
from datetime import datetime
import os
import numpy as np


genomeFile = open('/home/castle/Downloads/GenomeDataTable1/aaa.fna')


genomeread = genomeFile.read()
print(len(genomeread))


genomeSeq = Sequence(genomeread)
t = datetime.now()

genomeKmers = set(map(str, genomeSeq.iter_kmers(4, overlap=True)))

print("Kmer counting Elapse Time with SKBIO : " + (datetime.now() -t))

