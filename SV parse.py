import re


def findexpandprint(regexobj, objlist, svtype):
    filteredlist=re.findall(regexobj, objlist)
    if filteredlist:
        for x in range(len(filteredlist)):
            file.write(svtype)
            file.write(filteredlist[x])
            file.write(';')
            file.write('\n')
    return filteredlist


def printdut(modname, IOarray):
    file.write(modname)
    file.write(' dut(')
    for i in range(len(IOarray)):
        for j in range(len(IOarray[i])):
            file.write('.')
            file.write(IOarray[i][j])
            file.write('(')
            file.write(IOarray[i][j])
            file.write(')')
            if i == len(IOarray)-1 and j == len(IOarray[i])-1:
                file.write(');')
            else:
                file.write(',')
    return


file = open('chipmunks.sv', mode='r')

stepOne = file.read()

moduleHeader = stepOne.split(';')

# Getting the module name
spaceSplit = stepOne.split(' ')
bracketSplitModName = spaceSplit[1].split('(')
modName = bracketSplitModName[0]

file.close()

bracketsRegexObj = re.search(r'\(([^)]+)', moduleHeader[0])             # Regex search, inside brackets, ^) excludes ')'

IOlist = bracketsRegexObj.group(0).split('(')                    # Get rid of the '('

# Regex for input and outputs

inputRegexObj = re.compile(r'(?<=input )\w+')                    # Finds all input values
inputRegexObjBus = re.compile(r'(?<=input )\[\w+\D\w+\] \w+')

outputRegexObj = re.compile(r'(?<=output )\w+')                    # Finds all output values
outputRegexObjBus = re.compile(r'(?<=output )\[\w+\D\w+\] \w+')

inoutRegexObj = re.compile(r'(?<=inout )\w+')                    # Finds all output values
inoutRegexObjBus = re.compile(r'(?<=inout )\[\w+\D\w+\] \w+')

allBusesRegexObj = re.compile(r'(?<=] )\w+')
allBuses = re.findall(allBusesRegexObj, IOlist[1])
# End of Regex search

# Writing in file
file = open('output.txt', mode='w')

file.write('module tb_')
file.write(modName)
file.write('();')
file.write('\n\n')

fileInputs = findexpandprint(inputRegexObj, IOlist[1], 'logic ')
findexpandprint(inputRegexObjBus, IOlist[1], 'logic ')
fileOutputs = findexpandprint(outputRegexObj, IOlist[1], 'wire ')
findexpandprint(outputRegexObjBus, IOlist[1], 'wire ')
fileInOuts = findexpandprint(inoutRegexObj, IOlist[1], 'wire ')
findexpandprint(inoutRegexObjBus, IOlist[1], 'wire ')

IOarray = [fileInputs, fileOutputs, fileInOuts, allBuses]
# x = len(IOarray)
file.write('\n\n')

printdut(modName, IOarray)

file.write('\n')
file.write('endmodule')
file.close()
