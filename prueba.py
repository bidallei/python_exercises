memReg = './members02.txt'
exReg = './inactive02.txt'

#TODO:Open the currentMem file as in r+ mode
open_memReg = open(memReg, 'r+')

#TODO: Open the exMem file in a+ mode
open_exMem = open(exReg, 'a+')

#TODO: Read each member in the currentMem (1 member per row) file into a list.
with open_memReg as file:
    lista_memReg = []
    for line in file:
        lista_memReg.append(file.readline())
#Hint: Recall that the first line in the file is the header.

#TODO: iterate through the members and create a new list of the innactive members
lista_yes_memReg = []
for i in lista_memReg:
    if "yes" in i:
        lista_yes_memReg.append(i)
    else:
        continue

print(lista_yes_memReg)

#Go to the beginning of the currentMem file
#TODO: Iterate through the members list. 
#If a member is inactive, add them to exMem, otherwise write them into currentMem
