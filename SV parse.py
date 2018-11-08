import re

file = open ('chipmunks.sv', mode = 'r')

stepone=file.read()

steptwo=stepone.split(';')

file.close()

stepthree = re.search(r'\(([^)]+)', steptwo[0])             #Regex search, inside brackets, ^) excludes ')'

stepfour = stepthree.group(0).split('(')                    #Get rid of the '('

stepfive = re.compile('input (.*)', flags=re.DOTALL)

stepsix = re.search(stepfive,stepfour[1])

#stepfive = stepfour[1].split(',')

file = open('output.txt', mode='w')

if stepfive:
    file.write(stepsix.group(0))

#for i in stepfive:
#    file.write(stepfive[1])

file.close()