import sys

filename = sys.argv[1]

newDeletecounter = 0
lineNumber = 1
variable_names = {}

fHandle = open(filename, 'r')
fileLines = fHandle.readlines()

# fileLines has all the lines in the file
# line is each line in the file
# words has each line broken into words
for line in fileLines:
    words = line.split()
    index = 0
    for word in words:
        if word == "new":
            variable_names[words[index - 2]] = lineNumber
            newDeletecounter += 1
        
        if word == "delete" or word == "delete[]":
            if words[index + 1].replace(";", "") in variable_names:
                variable_names.pop(words[index + 1].replace(";", ""))
                newDeletecounter -= 1                    
        index += 1
    lineNumber += 1

if newDeletecounter > 0:
    print("\n\n\nMismatching dynamic allocation in file: " + str(newDeletecounter) + "!")
    print("Variables not allocated: ")
    for entry in variable_names:
        print(str(entry) + ":" + str(variable_names[entry]))
else:
    print("\n\n\nDynamic Allocation correct!\n")
    print("________$$$$")
    print("_______$$__$")
    print("_______$___$$")
    print("_______$___$$")
    print("_______$$___$$")
    print("________$____$$")
    print("________$$____$$$")
    print("_________$$_____$$")
    print("_________$$______$$")
    print("__________$_______$$")
    print("____$$$$$$$________$$")
    print("__$$$_______________$$$$$$")
    print("_$$____$$$$____________$$$")
    print("_$___$$$__$$$____________$$")
    print("_$$________$$$____________$")
    print("__$$____$$$$$$____________$")
    print("__$$$$$$$____$$___________$")
    print("__$$_______$$$$___________$")
    print("___$$$$$$$$$__$$_________$$")
    print("____$________$$$$_____$$$$")
    print("____$$____$$$$$$____$$$$$$")
    print("_____$$$$$$____$$__$$")
    print("_______$_____$$$_$$$")
    print("________$$$$$$$$$$$")

fHandle.close()