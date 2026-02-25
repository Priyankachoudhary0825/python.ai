# 1st question 
for i in range (1,51):
   if i%3 == 0 and i%5 == 0:
      print("fizzbuzz")
   elif i%3 == 0:
      print("fizz")
   elif i%5 == 0:
      print("buzz")
   else:
      print(i)  

# 2nd question

for num in range(2,101):
   prime=True
   for i in range(2,num):
      if num %i==0:
         prime = False
         break
   if prime:
      print(num) 

# 3rd question
score=int(input("enter score:"))
if 90 <= score<=100:
  print("grade:A")
elif 80 <= score<=89:
   print("grade:B")
elif 70 <= score<=79:
   print("grade:C")
elif 60 <= score<=69: 
   print("grade:D")    
else:
   print("grade:F")    

#4th question
for i in range(1,11):
   for j in range(1,11):
     print(i,"x",j,"=",i*j)  
     print() 

#5th question
for i in range(2,21,2):
   print(i*i)  

#6th question
year=int(input("enter year:"))
if(year%4==0 and year%100 !=0) or (year%400==0):
   print("leap year")
else:
   print("not a leap year")   

#7th question
a=int(input("side 1:"))
b=int(input("side 2:"))
c=int(input("side 3:"))
if a==b==c:
   print("Equilateral")
elif a==b or b==c or a==c:
   print("Isosceless")
elif a*a+b*b+c*c or a*a+c*c == b*b or b*b+c*c == a*a:
   print("right-angled")
else:
   print("Scalene")        

#8th question
num=int(input("enter number:"))
if num>0:
   print("Postive")
elif num <0:
   print("Negative")
else:
   print("Zero")

#10th question
weight = float(input("enter weight(kg):"))
height = float(input("enter height(m):"))
bmi=weight/(height**2)
print("BMI:",bmi)
if bmi<18.5:
   print("underweight")
elif 18.5<=bmi<=24.9:
   print("Normal weight")
elif 25<=bmi<=29.9:
   print("Overweight")
else:
   print("obesity")

# 11th question
day = int(input("enter day(1-7):")) 
days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturady","Sunday"]
if 1<=day<=7:
   print(days[day-1])
else:
   print("Invail days")   

 # 12th question
price=float(input("enter price:") )
if price>1000:
   discount=price*0.10
elif 500<=price<=1000:
     discount=price*0.05 
else:
   discount=0
   Final_price =price-discount
   print("Original price:$",price)
   print("Discount:$",discount)
   print("Final price after discount:$",Final_price)

 # 13 question
n=int(input("enter n:"))
print("sum:",n*(n+1)//2)

#14 question
emp={"Aman":6000,"Riya":45000,"John":75000}
for name,salary in emp.items():
   if salary>5000:
      print(name)

# 15 question
text=input("Enter string:")
count=0
for ch in text.lower():
   count+=1
   print("vowels:",count)  

# 16 question
num=input("enter number:")
total=0
for digit in num:
   total+=int(digit)
   print("sum of digits:",total)

 # 17question
n=int(input("enter n:")) 
for i in range(1,n+1):
   print("*"*i)

# 18 question
import random
number=random.randint(1,100)
while True:
    guess= int(input("Guess number(1-100):"))
    if guess>number:
       print("Too high!")
    elif guess<number:
       print("Too low!")
    else:
       print("Corrrect!")
       break

# 19 question
n =int(input("Enter n:"))
for  i in range(2,n+1,2):
   print(i)

# 20 question:
numbers=[]
for i in range(10):
   num=int(input("enter number:"))
   numbers.append(num)
   print("List:",numbers)   
   for num in numbers:
      if num%2==0:
         print("Even:",num)

# 21 question:
words=input("Enter words:").split()
print("First word:",words[0])
print("Last word:",words[-1])
longest=max(words,key=len)
print("Longest word:",longest)  
for word in words:
   if len(words)%2==1:
      print("Middle character:",word[len(word)//2])

# 22 question:
print("welcom to calc")
num1=int(input("enter 2nd number for Sum:"))
num2=100
print("sum is ",num1+num2)
