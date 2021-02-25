import os
import sys
import pefile

def sections(filename):
	sections = []
	pe = pefile.PE(filename)
	for section in pe.sections:
		sections.append(section.Name.decode('utf-8').split("\x00")[0])
	return sections    

if __name__ == '__main__':
	common = []
	first_uniq = []
	sccnd_uniq = []
	# first file sections 
	if sys.argv[1].endswith(".exe"):
		first_file_sections = {}
		first_file_sections = sections(sys.argv[1])
	# seccond file sections 
	if sys.argv[2].endswith(".exe"):	
		seccnd_file_sections = {}
		seccnd_file_sections = sections(sys.argv[2])

	# common sections
	for key in first_file_sections:	
		if (key in seccnd_file_sections):
			common.append(key)

	print ("\n########\n SEÇÕES COMUNS\n########\n")
	print(common)

	# unique sections for first file
	for key in first_file_sections:	
		if (key not in seccnd_file_sections):
			first_uniq.append(key)

	print ("\n########\n SEÇÕES UNICAS ",sys.argv[1],"\n########\n")
	print(first_uniq)

	# unique sections for seccond file
	for key in seccnd_file_sections:	
		if (key not in first_file_sections):
			sccnd_uniq.append(key)

	print ("\n########\n SEÇÕES UNICAS ",sys.argv[2],"\n########\n")
	print(sccnd_uniq)
	