import alignment

seq1 = 'asdef'
seq2 = 'akdefne'

water = alignment.water(seq1, seq2)
needle = alignment.needle(seq1, seq2)
print 'THE BEST RESULT IS ', (float(water) + float(needle)) / float(2)