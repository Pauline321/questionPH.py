# question.py by Pauline
# Question 1 - Correct Answer is (1)

#initialize variables
q1 = """what is 3 + 3?
1) 6
2) 9
3) 5
4) 0
"""
a1 = int (0)
check1 = bool(False)
score = int(0)

#question 1
print(q1)

#start of while loop
while check1 == False:
  try:
        a1 =int(input(" choose the answer you think is correct. "))
        if a1 == 1:
           print("Thanks") #acceptable answer
           score = int(score+1)
           check1 = True
        elif 0 < a1 < 1: #acceptble answer
           print( "Thanks") 
           check1 = True
        else: 
           print(" Your choice needs to be between 1 and 4.") #unacceptable answer
  except ValueError:
           print("Your answer has to be a whole number")
            
#score
print("quiz score: " , score* 100, "%")
                 
