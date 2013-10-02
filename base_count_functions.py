def base_count(sequence, base):
    # returns the number of times base X occurs in the sequence
    s=sequence.lower()
    b=base.lower()
    return s.count(b)
    
    
def gc_content(sequence):
    numbases = len(sequence)
    g=base_count(sequence,'g')
    c=base_count(sequence,'c')
    gc = g + c
    gc_count = gc / float(numbases) * 100
    return gc_count + '%'
    # returns the GC content of the sequence
