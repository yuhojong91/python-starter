def main():
    # ex2()
    # ex3()
    # ex4()
    # ex5()
    # ex6()
    # ex7()
    # ex8()
    # ex9()
    ex10()
    
def ex2 ():
    userInputWidth = input("Enter width:")
    width = float(userInputWidth)
    userInputHeight = input("Enter height:")
    height = float(userInputHeight)
    userInputLength = input("Enter length:")
    length = float(userInputLength)
    print(f"Volume is: {round(width*height*length, 2)}")

def ex3 ():
    userInput = input("Enter list of numbers: ")
    userInputList = userInput.split(',')
    firstNum = int(userInputList[0])
    lastNum = int(len(userInputList)-1)
    print(firstNum == lastNum)
        
def ex4():
    userInput = input("Write your paragragh: ")
    splitByWord = userInput.split(' ')
    count = 0
    for word in splitByWord:
        if word.lower() == 'Python'.lower():
            count += 1
    print(count)
    
def ex5():
    myList = [1,2,3]
    mySet = {3,4,5}
    mySet.union(myList)
    print(mySet.union(myList))
    
def ex6():
    myList = [11, 100, 101, 999, 1001]
    # resultList = []
    # for num in reversed(myList):
    #     resultList.append(num)

    # for num in range(len(myList)-1, -1, -1):
    #     resultList.append(myList[num])
    
    print(myList[::-1]) # create new list using slice method
    
def ex7():
    userInput = input("Enter Your Number: ")
    if int(userInput) < 10:
        print("you lose")
    elif int(userInput) > 10 and int(userInput) < 50:
        print("try again")
    else:
        print("you win")    
        
def ex8():
    myList = [6,2,7,3,77,7,1]
    myMin = myList[0]
    for val in myList:
        if val < myMin:
            myMin = val
    print(myMin)

    
def ex9():
    userInput = input("Enter here: ")
    for str in userInput:
        if(str.isupper()):
            continue
        else:
            print(False)
            break

def ex10():
    userInput = input("Enter here: ")
    numOfVowels = 0
    numOfCons = 0
    for val in userInput:
        if val in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
            numOfVowels += 1
        else:
            numOfCons += 1
    print(f"Vowels: {numOfVowels}")
    print(f"Consonants: {numOfCons}")
# def ex11():
# def ex12():
# def ex13():

    
main()