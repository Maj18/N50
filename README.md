# General Information:

This program will calculate N50 for a genome assembly.

# Installation

Simply download the n50.py to your working directory

# Usage
An example for running the program:
```
	 python n50.py -i "MyFirstAssembly_out.unpadded.fasta"
```

Here, the fasta file comes from Mira assembly

If you want to save the output to a file:
```
	 python n50.py -i "MyFirstAssembly_out.unpadded.fasta" > outputfile
```

# 
Please be aware that when comparing N50 values from different assemblies,
the assembly sizes must be the same size in order for N50 to be meaningful.
