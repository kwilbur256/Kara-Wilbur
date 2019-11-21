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

def ScoreFinder(lst_one, lst_two, string):
    if string in lst_one:
        position = lst_one.index(string)
        print("OUTPUT", string, "got a score of", lst_two[position])
    else:
        print("OUTPUT player not found")

def Union(lst_one, lst_two):
    x = len(lst_one)
    for i in range(x):
        if lst_one[i] in lst_two:
            lst_one = lst_one.pop(i)

        new_lst = lst_one.extend(lst_two)
        return new_lst
