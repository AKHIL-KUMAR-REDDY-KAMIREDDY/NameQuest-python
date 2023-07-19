import random
# if you want to add participants names dynamically uncomment the below two lines and comment the list of participants_names
# print("Enter all participants name separated with ,:")
# participants_names=input().split(",")
def game():
    print("\n 1 for start game\t 2 for Edit\t 3 for Exit")
    val=int(input())
    return val
#Adding a participant / Question while playing a game
def add_par_que():
    print("1 for Adding Participant\t 2 for Adding Question")
    edit_val=int(input())
    if(edit_val==1):
        print("Enter Participant name:")
        p_name=input()
        participants_names.append(p_name)
    if(edit_val==2):
        print("Enter Questuion:")
        que=input()
        questions.append(que)
    
#Add the participants names in the belowlist
  
participants_names=["akhil","venkey","ganesh","ravi","chaithu","bhanu","mani"]

#Add the Questions in the below list

questions=["Proposing to Opposite Gender","Slap to Opposite Gender","Hug with Same Gender","Dance","Sing a Song","Immitating","Dialogue","Mono action"]
val=0
while(val!=3):
    if(val==1):
        person=random.choice(participants_names)
        print("\n---------------------------------------------------------------------------------------------------------\n")
        print("\t\t\tParticipant is ----> {}".format(person))
        print("\t\t\tQuestion is -------> {}".format(random.choice(questions)))
        print("\n---------------------------------------------------------------------------------------------------------\n")
        p_d_info=input("Do you want to delete the Person_name[y/n]:")
        if(p_d_info=='y'):
            participants_names.remove(person)
        else:
            pass
    if(val==2):
        add_par_que()
        val=game()
    if(val==3):
        break
    return_ans=input("Do you want to play the game[y/n]:")
    if(return_ans=='y'):
        val=game()
    else:
        break