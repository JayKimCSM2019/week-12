#Jay Kim
#CSCI 102 E
#Week 12

def PrintOutput(string):
    print(string)

def Loadfile(file_name):
    file=open(file_name)
    lines=file.readlines()
    file.close()
    for line in lines:
        words=lines.split('.')
    print(words)
def UpdateString(string,letter,index):
    word_list=string.split()
    word_list[index]==letter
    
