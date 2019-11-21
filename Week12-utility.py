#Kara Wilbur
#CSCI 102 - Section C
#Week 12 LabA

def PrintOutput(output):
    print("OUTPUT", output)git

def LoadFile(file):
    text = open(file, "r")
    contents = text.read()
    text.close()
    print("OUTPUT", contents)
