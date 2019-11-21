#Kara Wilbur
#CSCI 102 - Section C
#Week 12 LabA

def PrintOutput(output):
    print("OUTPUT", output)

def LoadFile(file):
    text = open(file, "r")
    contents = text.read()
    text.close()
    print("OUTPUT", contents)
    
def UpdateString(str_one, str_two, index):
    str_one = str_one[:index] + str_two + str_one[index + 1:]
    print("OUTPUT", str_one)

def FindWordCoUnt(lst , string):
    number = lst.count(string)
    return number

