


def complement_dna(dna_sequence):
    complement = ""
    
    for nucleotide in dna_sequence.upper():
        if nucleotide == 'A':
            complement += 'T'
        elif nucleotide == 'T':
            complement += 'A'
        elif nucleotide == 'C':
            complement += 'G'
        elif nucleotide == 'G':
            complement += 'C'
        else:
            return "Error: Invalid DNA sequence."
    
    return complement

#user input
dna_input = input("Enter a DNA sequence: ").strip()
result = complement_dna(dna_input)
print(result)