n = int(input("enter a month (1-12):"))
if n==1:
    print("january")
elif n==2:
    print("february")
elif n==3:
    print("march")
elif n==4:
    print("april")
elif n==5:
    print("may")
elif n==6:
    print(" june")
elif n==7:
    print("july")
elif n==8:
    print("august")
elif n==9:
    print("september")
elif n==10:
    print("october")
elif n==11:
    print ("november")
elif n==12:
    print("december")
else:
    print("invaild month  number")





# 2nd question
#<a>
a = int(input("enter first number:"))
b = int(input ("enter a second number :"))
#<b>
if a == b:
    print(" both are equal number")
else :
    print(" both are not equal to ")  
if a>b:
    print("first numer is biggest")
elif b>a:
    print("second numer is biggest")
else:
    print("both are equal") 
# <c>
if a<=b:
    print("first number is smaller or equal to second number" )
else:
    print("first nuber is grater than second")  
 
 # <d>
if a>b:
  for i in  range(5):
     print("firstname")  
else:
  for i in range(3):
     print("surname")       




# 3rd Question 
# <1>
s1 = input("enter a first string")
s2 = input("enter a second string ") 
if s1 == s2:
    print("string equal to using ==") 
else:
    print("string are not equal to using ==") 

 #<2>
if s1 is s2:
    print("string are equal to using is")
else:
    print("string are not equal to using is") 


# 4th question 
a = int(input("enter a first string:")) 
b = int(input("enter a second string:"))   
print("even number are:")
for i in range(a,b+1):
    if i%2 ==0:
        print(i,end="")

# 5th question
n = int(input("enter a number:"))
total = 0
for i in range(1,n+1):
    total += i
print("sum=",total)

# 6th question 
n = int(input("enter a number:"))  
print("even number are:")
for i in range(2, n+1,2):
    print(i,end=",")

 #7th question
num = int(input("enter a number:"))
op = input("enter OP(+ or -):")
if op =="+":
  for  i  in range(0,num):
      print(i,end=",") 
elif op =="-":
  for i in range(num,o,-1):
      print(i, end=",")
else:
      print("invalid operator")

