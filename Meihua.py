def byNum(num1,num2):
  
  #calculation
  outer = num1%8
  inner = num2%8
  if(num1+num2)<=6:
    change = num1+num2
  else:
    change = (num1+num2)%6

  #Main diagram(Present)
  Main = eightDiagrams[outer-1]+eightDiagrams[inner-1]
  
  #Changed diagram(Result)
  Changed = eightDiagrams[outer-1]+eightDiagrams[inner-1]
  
  if Changed[6-change] == 1:
    Changed[6-change] = 0
  elif Changed[6-change] == 0:
    Changed[6-change] = 1

  return Main,Changed

#judge Diagrams
def judgeDiagrams(Main,Changed):
  nowTi = 0 #上卦为体为0；下卦为体则是1
  
  for i in range(3):
    if Main[i]!=Changed[i]:
      nowTi = 1
  return nowTi

def listToString(List):
  output = ""
  for i in range(len(List)):
    output+=str(List[i])
  return output


def fiveProperty(Main,Changed,TiYong):
  if TiYong == 0:
    Main_Ti = Main[0:3]
    Main_Yong = Main[3:]
    Changed_Ti = Changed[0:3]
    Changed_Yong = Changed[3:]
  else:
    Main_Ti = Main[3:]
    Main_Yong = Main[0:3]
    Changed_Ti = Changed[3:]
    Changed_Yong = Changed[0:3]
  
    
  Main_Ti = listToString(Main_Ti)
  Main_Yong = listToString(Main_Yong)
  Changed_Ti = listToString(Changed_Ti)
  Changed_Yong = listToString(Changed_Yong)
  

  MainFP_Ti = WuXing[Main_Ti]
  MainFP_Yong = WuXing[Main_Yong]
  ChangedFP_Ti = WuXing[Changed_Ti]
  ChangedFP_Yong = WuXing[Changed_Yong]

  return MainFP_Ti,MainFP_Yong,ChangedFP_Ti,ChangedFP_Yong
  
def produce_overcome(MainFP_Ti,MainFP_Yong,ChangedFP_Ti,ChangedFP_Yong):
  #main situation
  if(overcome[MainFP_Ti]==MainFP_Yong):#体克用
    mainResult = "TOY"
  elif(overcome[MainFP_Yong]==MainFP_Ti):#用克体
    mainResult = "YOT"
  elif(produce[MainFP_Ti]==MainFP_Yong):#体生用
    mainResult = "TPY"
  elif(produce[MainFP_Yong]==MainFP_Ti):#用生体
    mainResult = "YPT"
  elif(MainFP_Ti == MainFP_Yong):
    mainResult = "TYBH"

  #changed situation
  if(overcome[ChangedFP_Ti]==ChangedFP_Yong):#体克用
    changedResult = "TOY"
  elif(overcome[ChangedFP_Yong]==ChangedFP_Ti):#用克体
    changedResult = "YOT"
  elif(produce[ChangedFP_Ti]==ChangedFP_Yong):#体生用
    changedResult = "TPY"
  elif(produce[ChangedFP_Yong]==ChangedFP_Ti):#用生体
    changedResult = "YPT"
  elif(ChangedFP_Ti == ChangedFP_Yong):
    changedResult = "TYBH"
  return mainResult,changedResult


def normalThings(mainResult,changedResult): #占人事
  #Now situation

  #Future situation
  if(changedResult == "TOY"):
    result = "Good, positive or yes"
  elif(changedResult == "YOT"):
    result = "Not good, negative or no"
  elif(changedResult == "TPY"):
    result = "Doing this may have some potential problems to cost you"
  elif(changedResult == "YPT"):
    result = "Something good could happen and it could be good for you"
  elif(changedResult == "TYBH"):
    result = "Good, it ought to be done"

  return result


def family(mainResult,changedResult):
  if(changedResult == "TOY"):
    result = "Happy and harmonious family"
  elif(changedResult == "YOT"):
    result = "Family is not harmonious, may be more quarrels or poverty"
  elif(changedResult == "TPY"):
    result = "Family will annoy you, consume energy, or have the possibility of theft"
  elif(changedResult == "YPT"):
    result = "The benefits are many, or there are good things to receive"
  elif(changedResult == "TYBH"):
    result = "Good, safe and sound"
  
  return result


def house(mainResult,changedResult):
  if(changedResult == "TOY"):
    result = "Good"
  elif(changedResult == "YOT"):
    result = "Bad"
  elif(changedResult == "TPY"):
    result = "The family or household may be on a downward trend"
  elif(changedResult == "YPT"):
    result = "The family or household may be on an upward trend"
  elif(changedResult == "TYBH"):
    result = "Good, safe and sound"
  
  return result


def love(mainResult,changedResult):
  if(changedResult == "TOY"):
    result = "You will be together, but it may be late"
  elif(changedResult == "YOT"):
    result = "You will not be together, even together will consume a lot of your time and energy and material"
  elif(changedResult == "TPY"):
    result = "This relationship is difficult to be successful and you may lose something because of it"
  elif(changedResult == "YPT"):
    result = "This relationship can be successful and you can learn or get something from it"
  elif(changedResult == "TYBH"):
    result = "Good, the relationship can come true"
  
  return result

def birth(mainResult,changedResult): #关于男女可以单独询问
  if(changedResult == "TOY"):
    result = "Not good for kid"
  elif(changedResult == "YOT"):
    result = "Not good for Mom"
  elif(changedResult == "TPY"):
    result = "Good for kid"
  elif(changedResult == "YPT"):
    result = "Good for Mom"
  elif(changedResult == "TYBH"):
    result = "Both are safe and sound"
  
  return result

def diet(mainResult,changedResult):
  if(changedResult == "TOY"):
    result = "There are some obstacles on food, maybe don't have time or can't find restaurant"
  elif(changedResult == "YOT"):
    result = "No food or haven't eaten yet"
  elif(changedResult == "TPY"):
    result = "Foods are yucky"
  elif(changedResult == "YPT"):
    result = "Have a hearty meal"
  elif(changedResult == "TYBH"):
    result = "Both are safe and sound"
  
  return result

def plan(mainResult,changedResult):
  if(changedResult == "TOY"):
    result = "The plan can be achieved, but the realization time will be slow"
  elif(changedResult == "YOT"):
    result = "The plan cannot be achieved, even achieved it will harm you"
  elif(changedResult == "TPY"):
    result = "Most plans don't work out"
  elif(changedResult == "YPT"):
    result = "Have a hearty meal"
  elif(changedResult == "TYBH"):
    result = "The plan will goes well"
  
  return result

def career(mainResult,changedResult):
  if(changedResult == "TOY"):
    result = "Interviews or jobs are available, but take a longer time"
  elif(changedResult == "YOT"):
    result = "The jobs or interviews will be failed"
  elif(changedResult == "TPY"):
    result = "This job doesn't not suitable for you, it's bad for you"
  elif(changedResult == "YPT"):
    result = "It's easy to get the job or the fame"
  elif(changedResult == "TYBH"):
    result = "Everything goes well"
  
  return result

def wealth(mainResult,changedResult):
  if(changedResult == "TOY"):
    result = "You will have the treasure or make a good deal"
  elif(changedResult == "YOT"):
    result = "No money, or the trade will fail"
  elif(changedResult == "TPY"):
    result = "Wealth will be lost, or the transaction will not be easy to succeed"
  elif(changedResult == "YPT"):
    result = "Something good will increase your wealth and the deal will be successful immediately"
  elif(changedResult == "TYBH"):
    result = "Everything goes well"
  
  return result

def lostPeople(mainResult,changedResult): #or pets
  if(changedResult == "TOY"):
    result = "They may come back late"
  elif(changedResult == "YOT"):
    result = "They can't come back or be hard to come back"
  elif(changedResult == "TPY"):
    result = "They are not coming back"
  elif(changedResult == "YPT"):
    result = "They will back soon"
  elif(changedResult == "TYBH"):
    result = "If they are lost, just for a while or several days"
  
  return result

def appointment(mainResult,changedResult):
  if(changedResult == "TOY"):
    result = "You can go on that appointment"
  elif(changedResult == "YOT"):
    result = "You should not go to that appointment"
  elif(changedResult == "TPY"):
    result = "It's hard to have such appointment with someone or useless"
  elif(changedResult == "YPT"):
    result = "You should get in touch with them, it's good for you"
  elif(changedResult == "TYBH"):
    result = "There will be a happy and nice appointment"
  
  return result

def lostStuff(mainResult,changedResult):#contact with me and I will analyze the direction to you
  if(changedResult == "TOY"):
    result = "Things can be found, but late"
  elif(changedResult == "YOT"):
    result = "You can't find it"
  elif(changedResult == "TPY"):
    result = "It's hard to find"
  elif(changedResult == "YPT"):
    result = "It's easy to find"
  elif(changedResult == "TYBH"):
    result = "Can't lose things"
  
  return result

def disease(mainResult,changedResult):#contact with me and I will analyze more details to you
  if(changedResult == "TOY"):
    result = "The disease is more easily stabilized"
  elif(changedResult == "YOT"):
    result = "It's hard to get well"
  elif(changedResult == "TPY"):
    result = "The disease is delayed and difficult to get well"
  elif(changedResult == "YPT"):
    result = "The disease will be cured soon"
  elif(changedResult == "TYBH"):
    result = "The disease will be stabilized."
  
  return result


def lawsuit(mainResult,changedResult):
  if(changedResult == "TOY"):
    result = "You can win the lawsuit"
  elif(changedResult == "YOT"):
    result = "You will lose"
  elif(changedResult == "TPY"):
    result = "Lawsuits are not justified or lost because of lawsuits"
  elif(changedResult == "YPT"):
    result = "The lawsuit can be justified and may also gain somethings because of the lawsuit"
  elif(changedResult == "TYBH"):
    result = "Good outcome of the lawsuit, there may be a peaceful end"
  
  return result


eightDiagrams = [[1,1,1],[0,1,1],[1,0,1],[0,0,1],[1,1,0],[0,1,0],[1,0,0],[0,0,0]]
WuXing = {"111":"jin","011":"jin","101":"huo","001":"mu","110":"mu","010":"shui","100":"tu","000":"tu"}
overcome = {"jin":"mu","mu":"tu","shui":"huo","huo":"jin","tu":"shui"}
produce = {"jin":"shui","mu":"huo","shui":"mu","huo":"tu","tu":"jin"}


#main
print("Welcome to Plum Blossom I Prediction(part of I-Ching)")
print("If you have any question or just met any problem, you can use this program to help you")
print("All the results here are for reference only, cuz a more accurate prediction needs more information")
print("If you want to have a more accurate prediction, find me on INS. (id: t_nvgu)\n")
print("Here is the way to use the program > ")
print("1. Think about your problem or issue")
print("2. Find two numbers from anywhere.")
print("   E.g. you just looked at your watch and it's 5:23, you can just pick two of them, without any hesitation")
print("   For me, I would like to take 2 and 3, so just input 2 and 3 later in the program.")
print("   Or, you can get the number from anywhere but it's subconscious.")
print("   Like when you are thinking about the problem, and suddenly a person say hi, how are you to you")
print("   Then, you can pick the number of letter of the first two words, 2 and 3")
print("   And like that, it can be the phone number, it can be the date of birth, but it all needs to be the first thing that comes to mind.")
print("(This is the most important part of prediction, because I-Ching's prediction depends on the people's first thought)\n")

continued = "yes"
while continued == "yes":
    print("Prediction choice")
    print("1. Normal Things")
    print("2. About family")
    print("3. About household")
    print("4. About love")
    print("5. About birth")
    print("6. About diet")
    print("7. About a plan")
    print("8. About career")
    print("9. About wealth")
    print("10. About people who lost( or pets)")
    print("11. About appointment")
    print("12. About lost items(more details ask for author)")
    print("13. About disease")
    print("14. About lawsuit")

    choice = int(input("Please choose the index of thing you want to know > "))
    print("")
    num = input("Please tpye two numbers as the following pattern (number1 number2) > ")
    num1,num2 = num.split(" ")
    Diagrams = byNum(int(num1),int(num2))
    Main = Diagrams[0]
    Changed = Diagrams[1]
    TiYong = judgeDiagrams(Main,Changed)
    print(Diagrams)
    MainFP_Ti,MainFP_Yong,ChangedFP_Ti,ChangedFP_Yong = fiveProperty(Main,Changed,TiYong)
    mainResult,changedResult = produce_overcome(MainFP_Ti,MainFP_Yong,ChangedFP_Ti,ChangedFP_Yong)

    if choice == 1:
        print(normalThings(mainResult,changedResult))
    elif choice == 2:
        print(family(mainResult,changedResult))
    elif choice == 3:
        print(house(mainResult,changedResult))
    elif choice == 4:
        print(love(mainResult,changedResult))
    elif choice == 5:
        print(birth(mainResult,changedResult))
    elif choice == 6:
        print(diet(mainResult,changedResult))
    elif choice == 7:
        print(plan(mainResult,changedResult))
    elif choice == 8:
        print(career(mainResult,changedResult))
    elif choice == 9:
        print(wealth(mainResult,changedResult))
    elif choice == 10:
        print(lostPeople(mainResult,changedResult))
    elif choice == 11:
        print(appointment(mainResult,changedResult))
    elif choice == 12:
        print(lostStuff(mainResult,changedResult))
    elif choice == 13:
        print(disease(mainResult,changedResult))
    elif choice == 14:
        print(lawsuit(mainResult,changedResult))

    continued = input("Would you like to know other things? (Yes or No)")
    continued = continued.lower()


