#Jay Kim
#CSCI 102 E
#Week 12

def PrintOutput(string):
    print("OUTPUT",string)

def Loadfile(file_name):
    file=open(file_name)
    lines=file.readlines()
    file.close()
    for line in lines:
        words=[].split(lines,'.')
    print("OUTPUT",words)
    
def UpdateString(string,letter,index):
    word_list=list(string)
    word_list[index]=letter
    new_string="".join(word_list)
    print("OUTPUT",new_string)

def FindWordCount(entered_list,entered_string):
    counter=0
    for i in entered_list:
        if i==entered_string:
            counter+=1
    print("OUTPUT",counter)

def ScoreBoard(players,scores,name):
    new_list=[]
    for i in players:
        new_list.append(i.lower())
        if i.lower()==name.lower():
            index=i.find(players)
            print("OUTPUT",name, "got a score of", scores[index])
        if name.lower() not in new_list:
            print("OUTPUT","player not found")
    
def Union(list_1,list_2):
    print("OUTPUT",list_1+list_2)

def Intersection(list_1,list_2):
    final_list=[]
    for i in list_1:
        if i in list_2:
            final_list.append(i)
    print("OUTPUT",final_list)

def Notin(list_1,list_2):
    final_list=[]
    for i in list_1:
        if i not in list_2:
            final_list.append(i)
    print("OUTPUT",final_list)
