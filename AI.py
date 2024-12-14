print("***************************Phil ai***************************")
print("*********************************************************************************")
print("*********************************************************************************")
pyt="Python is an open source programming language."
inpur="Input is a python function that is used to collect data from the user operating the program"
prin="Print is an inbuild funtion that is used to display information from the code to the user that is operating the program"
a1="A variable is a container that holds data"
a2="A list is the equivilent of an array in python that holds multiple data not particular about data type"
a3="Append keyword is used to add new data to a list and set"
a4="Loop in python is a syntax used to iterate a specific block of code, there 2 ways to loop, i-While lopp, ii-For loop."
a5="While loop is one of the 2 ways to loop, and it uses a variable as a counter to keep track of the amount of iterations it must undego."
a6="A for loop is a type of loop that usually makes use of an array or the python equivilent which are the lsit, tupple and set. They make use of those in order to keep track of the iteration of the block of code"
a7="A function in python is a block of code that is written outside the running code and can only be accessed by the system if it is called in the code by the Coder."
a8="A conditional statement in python is a piece of code or a syntax that runs when a specific condition is met."
a9="An if statement is a conditional statement that is used to run a code specifc to the condition it was given"
a10="Else if is an extention of the if statement, it is used when there are multiple codes that need to complete different conditions in which only one condition can be met at an instance."
a11="A nested if statement is an if statement inside another if statement or inside an else if statement."
a=0

while a < 29:
    
#-------------------------------------------------------------------------
    print(a)
    if a > 0:
     
     print("Do you wish to continue?")
     print("(1)yes (2)No")
     b=int(input("Enter your choice: "))
     if b==1:
            print("Continue on")
     elif b==2:
         break
     else:
         print("")
    a+=1
#-------------------------------------------------------------------------
    print("------------------------------------------------")
    print("Ask the Phil ai a question:")
    q=input("What is your question: ")
    q1=q.lower()
    words=q1.split()
#-------------------------------------------------------------------------    
    if "python"in words:
        print("Is your question, what is python?")
        print("(1)yes (2)No")
        b=int(input("Enter your choice: "))
        if b==1:
             print("Phil ai has found an answer")
             print("Your answer is as follows: ")
             print(pyt)
             continue
        elif b==2:
            print("Your next question?")
            
        else:
            break
    else:
      print("")
#-------------------------------------------------------------------------
    if "print" in words:
        print("Is your question, what is print in python?")
        print("(1)yes (2)No")
        b=int(input("Enter your choice: "))
        if b==1:
             print("Phil ai has found an answer")
             print("Your answer is as follows: ")
             print(prin)
             continue
        elif b==2:
            print("Your next question?")
            
        else:
            break
    else:
        print("")
#-------------------------------------------------------------------------
    if "input" in words:
        print("Is your question, what is input in python?")
        print("(1)yes (2)No")
        b=int(input("Enter your choice: "))
        if b==1:
             print("Phil ai has found an answer")
             print("Your answer is as follows: ")
             print(inpur)
             continue
        elif b==2:
            print("Your next question?")
            
        else:
            break
    else:
        print("")
#-------------------------------------------------------------------------
    if "variable" in words:
        print("Is your question, what is a variable in python?")
        print("(1)yes (2)No")
        b=int(input("Enter your choice: "))
        if b==1:
             print("Phil ai has found an answer")
             print("Your answer is as follows: ")
             print(a1)
             continue
        elif b==2:
            print("Your next question?")
            
        else:
            break
    else:
        print("")
#-------------------------------------------------------------------------
    if "list"in words:
        print("Is your question, what is list in python?")
        print("(1)yes (2)No")
        b=int(input("Enter your choice: "))
        if b==1:
             print("Phil ai has found an answer")
             print("Your answer is as follows: ")
             print(a2)
             continue
        elif b==2:
            print("Your next question?")
            
        else:
            break
    else:
        print("")
#-------------------------------------------------------------------------
    if "append"in words:
        print("Is your question, what is append in python?")
        print("(1)yes (2)No")
        b=int(input("Enter your choice: "))
        if b==1:
             print("Phil ai has found an answer")
             print("Your answer is as follows: ")
             print(a3)
             continue
        elif b==2:
            print("Your next question?")
            
        else:
            break
    else:
        print("")
#-------------------------------------------------------------------------
    if "loop"in words:
        print("Is your question, what is loop in python?")
        print("(1)yes (2)No")
        b=int(input("Enter your choice: "))
        if b==1:
             print("Phil ai has found an answer")
             print("Your answer is as follows: ")
             print(a4)
             continue
        elif b==2:
            print("Your next question?")
            
        else:
            break
    else:
        print("")
#-------------------------------------------------------------------------
    if "while" in words:
        print("Is your question, what is 'while loop' in python?")
        print("(1)yes (2)No")
        b=int(input("Enter your choice: "))
        if b==1:
             print("Phil ai has found an answer")
             print("Your answer is as follows: ")
             print(a5)
             continue
        elif b==2:
            print("Your next question?")
            
        else:
            break
    else:
        print("")
#-------------------------------------------------------------------------
    if "for" in words:
        print("Is your question, what is 'For' loop in python?")
        print("(1)yes (2)No")
        b=int(input("Enter your choice: "))
        if b==1:
             print("Phil ai has found an answer")
             print("Your answer is as follows: ")
             print(a6)
             continue
        elif b==2:
            print("Your next question?")
            
        else:
            break
    else:
        print("")
#-------------------------------------------------------------------------
    if "function"in words:
        print("Is your question, what is a function in python?")
        print("(1)yes (2)No")
        b=int(input("Enter your choice: "))
        if b==1:
             print("Phil ai has found an answer")
             print("Your answer is as follows: ")
             print(a7)
             continue
        elif b==2:
            print("Your next question?")
            
        else:
            break
    else:
        print("")
#-------------------------------------------------------------------------
    if "condition" in words:
        print("Is your question, what is conditional statement in python?")
        print("(1)yes (2)No")
        b=int(input("Enter your choice: "))
        if b==1:
             print("Phil ai has found an answer")
             print("Your answer is as follows: ")
             print(a8)
             continue
        elif b==2:
            print("Your next question?")
            
        else:
            break
    else:
        print("")
#-------------------------------------------------------------------------
    if "if"in words:
        print("Is your question, what is if statement in python?")
        print("(1)yes (2)No")
        b=int(input("Enter your choice: "))
        if b==1:
             print("Phil ai has found an answer")
             print("Your answer is as follows: ")
             print(a9)
             continue
        elif b==2:
            print("Your next question?")
            
        else:
            break
    else:
        print("")
#-------------------------------------------------------------------------
    if "elif"in words:
        print("Is your question, what is else if in python?")
        print("(1)yes (2)No")
        b=int(input("Enter your choice: "))
        if b==1:
             print("Phil ai has found an answer")
             print("Your answer is as follows: ")
             print(a10)
             continue
        elif b==2:
            print("Your next question?")
            
        else:
            break
    else:
        print("")
#-------------------------------------------------------------------------
    if "nested" and "if" in words:
        print("Is your question, what is input in python?")
        print("(1)yes (2)No")
        b=int(input("Enter your choice: "))
        if b==1:
             print("Phil ai has found an answer")
             print("Your answer is as follows: ")
             print(a11)
             continue
        elif b==2:
            print("Your next question?")
            
        else:
            break
    else:
        print("")

    

    
    
