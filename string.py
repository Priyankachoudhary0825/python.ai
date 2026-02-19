# 1 question 
s=input("enter a string:")
if len(s)<2:
    print("not a valid string")
else:
    print(s[0:2])+s[-2:])

 # 2nd question
s1= input("enter first string:")
s2=input("enter second string:")
result=s2[0]+s1[1:]+""+s1[0]+s2[1:]
print(result)


# 3rd question
s=input("enter a string:")
if len(s)<3:
    print(s)
elif s[-3:]=="ing":
    print(s+"ly")
else:
    print(s+"ing")        