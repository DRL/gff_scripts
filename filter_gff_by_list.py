#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def read_strings_to_set(infile):
	set_of_strings = set()
	with open(infile) as fh:
		for line in fh:
			set_of_strings.add(line.rstrip("\n"))
	return set_of_strings

def process_infile(infile, set_of_strings):
	with open(infile) as fh:
		for line in fh:
			if not line.startswith('#'):
				temp = line.split("\t")
				if len(temp) == 9:
					if temp[0] in set_of_strings:
						print line
				else:
					pass 

if __name__ == "__main__":
	strings = sys.argv[1]
	infile = sys.argv[2]

	set_of_strings = read_strings_to_set(infile)
	process_infile(infile, set_of_strings)
