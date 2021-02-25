import os
import sys
import pefile

def sections(filename):
	file = sys.argv[1] + "/" + filename	
	sections = []
	pe = pefile.PE(file)
	for section in pe.sections:
		sections.append(section)
	return sections    

def executablesSections(sections):
    executables = []
    for section in sections:
        if checkIfIsExecutable(section):
            executables.append(section.Name.decode('utf-8').split("\x00")[0])
    return executables

def checkIfIsExecutable(section):
    characteristics = getattr(section, 'Characteristics')
    if characteristics & 0x00000020 > 0 or characteristics & 0x20000000 > 0:
        return True
    return False

if __name__ == '__main__':
	filesDict = {}

	for filename in os.listdir(sys.argv[1]):
		if filename.endswith(".exe"):
			filesDict[filename] = {}
			filesDict[filename] = sections(filename)

	print ("########\n SEÇÕES EXECUTAVEIS \n########\n")
	for key in filesDict:
	    execSections = executablesSections(filesDict[key])
	    print(key," Sections: ",execSections)
			
	