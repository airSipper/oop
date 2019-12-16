#!/usr/bin/python3

"""
* bev												      
* One uppercase character
* Two numbers
* Two lowercase characters
* One symbol
* The year Tommy Boy came out in theaters = 1995
"""

import itertools
import string
from itertools import product


upper = list(string.ascii_uppercase) 
lower = list(string.ascii_lowercase)
digits = list(string.digits)
symbols = list(string.punctuation)

# all digit combos
digit_combos = [''.join(i) for i in itertools.product(digits, repeat = 2)]

# all lowercase combinations
lower_combos = [''.join(i) for i in itertools.product(lower, repeat = 2)]

a = 'bev'
b = 'A'
c = '00'
d = 'aa'
e = '!'
f = '1995'

def out(a, b, c, d, e, f):
	print("".join([a,b,c,d,e,f]))

for i in range(len(upper)):
	b = upper[i]
	out(a, b, c, d, e, f)

	for j in range(len(digit_combos)):
		c = digit_combos[j]
		out(a, b, c, d, e, f)
		
		for k in range(len(lower_combos)):
			d = lower_combos[k]
			out(a, b, c, d, e, f)

			for l in range(len(symbols)):
				e = symbols[l]
				out(a, b, c, d, e, f)

