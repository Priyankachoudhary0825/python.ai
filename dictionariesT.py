#1st question
sentence="python is easy and python is very easy"
words=sentence.split()
freq={}
for word in words:
    freq[word]=freq.get(word,0)+1

sorted_freq =dict(sorted(freq.item(),key=lambda x:x[1],reverse=True))  
print(sorted_freq)

#2nd question
marks={
    "alice":85,
    "bob":70,
    "charline":90,
    "david":60
}
average=sum(marks.value())/len(marks)
print("average marks:",average)
print("student scoring above average:")
for name,score in marks.item():
    if score>average:
        print(name)

#3rd question
d1={'a':50,'b':30,'c':70}
d2={'b':60,'c':65,'d':40}
result=d1.copy()
for key,value in d2.item():
    if key in result:
        result[key]=max(result[key]),value)
    else:
        result[key]=value          
        print(result)

 #4th question

data={
 'name':'alice',
 'city':'bangalore',
 'course':'data science'
 }    
max_key=max(data,key=lambda k:len(data[k]))
print(max_key)

#5th question
data={
    's':5,
    'p':20,
    'k':35,
    'b':60,
    'e':45
}
filtered={}
for key,value in data.item():
    if 10<=value<=50:
        filtered[key]=value
        print(filtered)

#6th question
votes=["j","k","j","r","k","j"]
count={}
for vote in votes:
    count[vote]=count.get(vote,0)+1
winner=max(count,key=count.get)
print("votes:",count)
print("winter:", winner)

#7th question
data{'a':10,'b':20,'c':30}
update={'b':200,'c':300}
for key in update:
    if key in update:
        data[key]=update[key]
        print(data)
        


