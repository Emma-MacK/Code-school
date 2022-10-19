def DNA2RNA(DNA):
    RNA = DNA.replace("T", "U")
    return RNA

RNAseq = DNA2RNA(input("Enter Sequence: "))
print(RNAseq)