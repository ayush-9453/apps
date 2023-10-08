questions =[
    ['5+2=',7,8,9,4,1],
    ['3*4=',12,31,45,9,1 ],
    ['33-2=',31,36,43,51,1],
    ['55+11=',66,72,45,78,1],
    ['55+11=',66,72,45,78,1],
    ['55+11=',66,72,45,78,1],
    ['55+11=',66,72,45,78,1],
    ['55+11=',66,72,45,78,1],
    ['55+11=',66,72,45,78,1]
]

level = [1000, 2000, 3000,5000,10000,50000,80000,120000,160000]
win = 0
i =0
for i in range(0,len(questions)):
    question =questions[i]
    print(f"Question for Rs.{level[i]}")
    print(f"Q{i+1}. {question[0]}")
    print(f"a.{question[1]}    b.{question[2]}")
    print(f"c.{question[3]}    b.{question[4]}")
    reply =int(input("Enter the answer :"))
    if (reply == question[-1]):
        print(f"Correct answer , you won {level[i]}")
        if(i ==4):
           win =  10000
        elif(i==8):
           win =  160000
    else :
        print("Worng answer, you lost")
        break


print(f"The money you win : {win}")
