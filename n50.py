import argparse
import sys
import re
import numpy as np

if len(sys.argv) != 3:
	sys.exit("ERROR: please run the program as follows: \
		python n50.py -i 'MyFirstAssembly_out.unpadded.fasta'")


parser = argparse.ArgumentParser(description = 'This program will calculate N50 for a genome assembly,\
	please be aware that when comparing N50 values from different assemblies, \
	the assembly sizes must be the same size in order for N50 to be meaningful.')
parser.add_argument(
	'-i',
	dest = "infile",
	metavar = 'INFILE',
	type = argparse.FileType('r'),
	default = True)
args = parser.parse_args()
infile = args.infile


contigL = []
L=0
for line in infile:
	line = line.rstrip()
	if line.startswith(">"):
		contigL.append(L)
		L=0
	else:
		L = L + len(line)
contigL.sort()
GenomeL_half = np.sum(contigL)/2
sum = 0
print("We now add upp the contig length starting from the shortest one")
print("...")
N50 = []
for i in contigL:
	sum = sum + i
	if sum >= GenomeL_half:
		N50.append(i)
		print (f"Now the contig length sum becomes longer than 50% of the genome length ({GenomeL_half}): ")
		print("Contig length", i)
		print("Contig length sum so far: ", sum)
print("\n", "N50: ", N50[0])


