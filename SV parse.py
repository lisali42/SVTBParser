import re

file = open ('chipmunks.sv', mode = 'r')

stepone=file.read()

steptwo=stepone.split(';')

file.close()

stepthree = re.search(r'\(([^)]+)', steptwo[0])

stepfour = stepthree.group(0).split('(')

stepfive = stepfour.split(',')

file = open('output.txt', mode='w')

file.write(stepfour[1])

file.close()