#!/usr/bin/env python

import sys, string
import alignment

# Command-line arguments
'''f1 = open(sys.argv[1], 'r')
seq1 = f1.readline()
seq1 = string.strip(seq1)

f2 = open(sys.argv[2], 'r')
seq2 = f2.readline()
seq2 = string.strip(seq2)
'''
seq1 = 'kemal'
seq2 = 'asdef'
alignment.needle(seq1, seq2)
