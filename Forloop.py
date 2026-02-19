#1st question
name=input("enter your name")
print(len(name))
for i in range(0,len(name)):
    print(name)
 

 #2nd question
n=int(input("enter the  n:"))
sum=0
for i in range(1,n+1):
    sum+=1
    print("the sum of first n natural number is:",sum)

#3rd question
num=int(input("enter a number:"))
for i in range(1,10):
    print(num,"*",i,"=",num*i)   


# 4th question
n=int(input("enter number"))
print(n**0.5)
if n<=1:
    print("false")
else:
    prime=True
    for i in range(2,n):
        if n%i==0:
            prime=False
            print(prime)

       

 #5th question
num=int(input(enter a number:))
if num=num[::-1]:
  print("palindrome")
else
  print("not palindrome")
            
           
 # 6th question
 for i in range(1,101:)
 if i%3==0 and i%5==0:
  print("fizzbuzz")
 elif i%3==0:
  print("fizz")
 elif i%5==0:
  print("buzz")
 else:
  print(i)    

                
                        
