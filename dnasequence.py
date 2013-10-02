import string

class NucleotideSequence:
    '''A general nucleotide class. The class is inherited by DNASequence
    and RNASequence classes. Not for general use. Use DNASequence and
    RNASequence instead'''
    complements = {'G': 'C',
                   'C': 'G',
                   'A': 'T',
                   'T': 'A'}
    valid = set(complements)

    def __init__(self, sequence):
    self.sequence = sequence
    self.base_counts = {}
    if set(sequence).difference(self.valid) != set():
        raise InvalidBaseException("Invalid base; bases: " + ''.join(set(sequence).difference(self.valid)))
        
    
    def base_count(self, base):
        '''Given a base, returns the number of
        times the base occurs in this sequence.
        
        Returns an integer.
        '''
        if base in self.base_counts:
            return self.base_counts[base]
        else:
            count = self.sequence.count(base)
            self.base_counts[base] = count
            return count
    
    def gc_content(self):
        g = self.base_count('G')
        c = self.base_count('C')
        return float(g+c)/len(self.sequence)
        
    def reverse_complement(self):
        rev_c = ""
        for base in self.sequence:
            rev_c = self.complements[base] + rev_c
            
        return rev_c
        
        
class DNASequence(NucleotideSequence):
    '''Uses the bases GATC.'''
    pass
    
class RNASequence(NucleotideSequence):
    '''Uses the bases GAUC.'''
    complements = {'G': 'C',
                   'C': 'G',
                   'A': 'U',
                   'U': 'A'}
    valid = set(complements)
                   
    def __init__(self, sequence):
        NucleotideSequence.__init__(self, sequence)
        assert not 'T' in sequence

