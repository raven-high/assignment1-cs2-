#count symbols 'A', 'C', 'G', and 'T' in dna string 

def count_base(dna_string):
    nA = dna_string.count ('A')
    nC = dna_string.count ('C')
    nG = dna_string.count ('G')
    nT = dna_string.count ('T')
    print(nA, nC, nG, nT)
   
dna_string = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
count_base(dna_string)