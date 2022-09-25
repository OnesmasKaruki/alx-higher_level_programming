#!/usr/bin/python3
def no_c(my_string):
	noc = []
	[noc.append(c) for c in my_list if c != 'c' and c != 'C']
	noc = ''.join(noc)
	return noc
