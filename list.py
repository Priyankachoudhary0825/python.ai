#1st question of list 
friends=["kajal","ajay","payal","sourav","riya"]
name=input("enter another friend:")
friends.append(name)
print(friends)
imp=input("most important friend:")
pos=int(input("enter position:"))
friends.insert(pos,imp)
print(friends)

#2nd question
numbers=list(range(1,11))
print(numbers)

#3rd question
list=[1,10,100,3,6,8]
list.insert(3,59)
list.append(5)
print(list)
print("length",len(list))


#4th question
words=["mango","bat","cat","apple","table"]
for w in words:
 if len(w) < 4:
  print(w)

#5th question
r=[]
for i  in range(20):
 if i%2==0:
   r.append("even")
else:
   r.append("odd")
   print(r)
     

  #6th question
for i in range(1,1000):
  if i%7==0:
    print(i)   

 #7th question 
s=input("enter a string:")
count=0
 
for ch in s:
  if ch==" ":
    count+=1
    print("number of space:",count) 


#8th question
list_a=[1,2,3,4]
list_b=[2,3,4,5]
common=[]
for i in list_a:
  if i in list_b:
    common.append(i)
    print("common numbers:",common)
    