def get_length(dna):
    ''' (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    '''
    return len(dna)


def is_longer(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    '''
    
    if len(dna1) > len(dna2):
        return True
    else:
        return False

def count_nucleotides(dna, nucleotide):
    ''' (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    '''

    nucleotides = 0
    for char in dna: 
        if char in nucleotide:
            nucleotides = nucleotides + 1
    return nucleotides


def contains_sequence(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    '''

    if dna1.find(dna2) >= 0:
        return True
    else: 
        return False 


def is_valid_sequence(dna):
    ''' (str) -> bool

    Returs True if DNA sequence is valid (contains only ATCG), returns False otherwise

    >>> is_valid_sequence('ATCG')
    True 
    >>> is_valid_squeince('AadfasrAF')
    False
    '''
    
    OK = True
    valid_sequence = 'ATCG'
    
    for char in dna:
        if char not in valid_sequence:
            return False

    return OK


def insert_sequence(dna1, dna2, index):
    
    ''' (str,str,int)->str

    Inserts dna2 into dna1 sequence starting with index number 

    >>> insert_sequence('ATCGGG', 'AT', 3)
    'ATCATGGG'
    >>> insert_sequence('GAAAAA', 'AT', 1)
    'GATAAAAA'
    '''

    dna3 = dna1[0:index] + dna2 + dna1[index:]
    return dna3

    
def get_complement(nucleotide):
    ''' (str)->str

    >>> get_complement(A)
    'T'
    >>> get_complement(G)
    'C'
    '''

    if nucleotide not in 'ATCG' or len(nucleotide) > 1: 
        return False

    for char in nucleotide: 
        if char in 'A':
            return 'T'
        if char in 'T': 
            return 'A'
        if char in 'C':
            return 'G'
        if char in 'G':
            return 'C'
    return  

def get_complementary_sequence(dna):
    '''(str)->str

    >>> get_complementary_sequence(AT)
    'TA'
    >>> get_complementary_sequence(GC)
    'CG'
    '''

    if not is_valid_sequence(dna): 
        return False

    if dna not in 'ATCG' or len(dna) > 2: 
        return False

    result=''
    
    for char in dna:
        result = result + get_complement(char)

    return result 
      
