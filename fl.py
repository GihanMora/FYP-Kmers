
fo = open('output.txt','r')
species = open('species.txt','w+')
distances = open('distances.txt','w+')
lines = fo.readlines()

for eachline in range(0,len(lines),3):
    print(lines[eachline])
    species.write(lines[eachline])
for eachline in range(1,len(lines),3):
    print(lines[eachline])
    distances.write(lines[eachline])