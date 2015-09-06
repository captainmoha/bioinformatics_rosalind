# Given: A DNA string s of length at most 1000 nt.

# Return: Four integers (separated by spaces) counting the respective
# number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

s = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
bases = {'A': 0, 'C': 0, 'G': 0, 'T': 0}


def DNA_Nucleotides(s):

    for nucleotide in s:
        bases[nucleotide] += 1

    return (str(bases['A']) + ' ' + str(bases['C']) + ' ' + str(bases['G']) + ' ' + str(bases['T']))

dna_file = str(open('dna.txt', 'r').read().strip())

print DNA_Nucleotides(dna_file)

# print DNA_Nucleotides(s)
