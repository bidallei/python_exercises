  
'''
The two arguments for this function are the files:
    - currentMem: File containing list of current members
    - exMem: File containing list of old members
    
    This function should remove all rows from currentMem containing 'no' 
    in the 'Active' column and appends them to exMem.
    '''
def cleanFiles(currentMem, exMem):
    #TODO: Open the currentMem file as in r+ mode
    open_currentMem = open(currentMem, 'r+')

    #TODO: Open the exMem file in a+ mode
    open_exMem = open(exMem, 'a+')

    #TODO: Read each member in the currentMem (1 member per row) file into a list.
    with open_currentMem as file:
        print(file.read())
    
    #Hint: Recall that the first line in the file is the header.

    #TODO: iterate through the members and create a new list of the innactive members

    #Go to the beginning of the currentMem file
    #TODO: Iterate through the members list. 
    # If a member is inactive, add them to exMem, otherwise write them into currentMem

        
    
    pass # Remove this line when done implementation

# The code below is to help you view the files.
# Do not modify this code for this exercise.
memReg = './members.txt'
exReg = './inactive.txt'
cleanFiles(memReg,exReg)


headers = "Membership No  Date Joined  Active  \n"
with open(memReg,'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())
    
with open(exReg,'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())
                