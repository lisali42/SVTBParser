import re

file = open ('chipmunks.sv', mode = 'r')

stepone=file.read()

moduleheader = stepone.split(';')

# Getting the module name
spaceSplit = stepone.split(' ')
bracketSplitModName = spaceSplit[1].split('(')
modName = bracketSplitModName[0]

file.close()

bracketsRegexObj = re.search(r'\(([^)]+)', moduleheader[0])             #Regex search, inside brackets, ^) excludes ')'

IOlist = bracketsRegexObj.group(0).split('(')                    #Get rid of the '('

# input parse

inputRegexObj = re.compile(r'(?<=input )\w+')                    #Finds all input values
inputRegexObjBus = re.compile(r'(?<=input )\[\w+\D\w+\] \w+')

inputList = re.findall(inputRegexObj, IOlist[1])                  #inputList is a array that contains all inputs
inputListbus = re.findall(inputRegexObjBus, IOlist[1])

file = open('output.txt', mode='w')

file.write('module tb_')
file.write(modName)
file.write('();')
file.write('\n')

if inputList:
    for x in range(len(inputList)):
        file.write('wire ')
        file.write(inputList[x])
        file.write(';')
        file.write('\n')
if inputListbus:
    for x in range(len(inputListbus)):
        file.write('wire ')
        file.write(inputListbus[x])
        file.write(';')
        file.write('\n')

file.close()