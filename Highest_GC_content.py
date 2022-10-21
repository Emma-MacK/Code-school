
# from a fasta file, read in sequences, calculate GC%
# return ID of sequence with highest GC content
import sys
# read in modules


# take the file to be read, and read it
input_file =  sys.argv[1]
file = open(input_file, "r").read()
# print(file.read()) 

# separate the file into objects where a > is present
# the fist element is a blank space, so remove
# the length of the fasta is calculated
# All elements of the fasta file returned

fasta_length = len(file)
list_fasta = file.split(">")[1:fasta_length]
# print(list_fasta)

# create a loop, run over elements a split into ID and sequence

for sequence in list_fasta:
    ID = sequence.split()[0]
    # print(ID)
    bases = sequence.split()[1]
    # print(bases)
    # count total number of bases
    length_bases = len(bases)
    # print(length_bases)
    # count the number of Cs and Gs 
    number_CG = bases.count("C") + bases.count("G")
    # print(number_CG)
    GC_per = number_CG/length_bases
    print(GC_per)
    
# count G and G bases in sequences, store based on ID

# Maybe have for loop, going over given sequences
# first sequence stored into objects
# if next object has higher GC, replace original ID and GC
# once through all sequences, return highest sequence.