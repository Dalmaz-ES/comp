"""
def some_function(dna_sequence):
    if not isinstance(dna_sequence, str):
        return "Invalid DNA sequence"
    
    complements = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    comp_seq = ''.join(complements.get(char, '') for char in dna_sequence)
    
    return comp_seq
"""


def some_function(dna_sequence):
    if not isinstance(dna_sequence, str) or not set(dna_sequence).issubset('ATCG'):
        return "Invalid DNA sequence"
    
    complements = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    comp_seq = ''.join(complements[char] for char in dna_sequence)
    
    return comp_seq