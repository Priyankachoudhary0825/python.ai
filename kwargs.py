
# 2nd question
def filter_details(**Kwargs):
   for key, value in Kwargs.items():
      if type(value)==str:
         print(f"{key}={value}")
filter_details(name="Alice",age=20, city="Bangalore",marks=85)         

         
 # 1st question
def average_marks(*args):
    total = 0
    count = 0
    
    for mark in args:
        if mark >= 0:   
            total += mark
            count += 1
    
    if count == 0:      
        return 0
    
    return total / count 
print("Average Marks:",average_marks(80,50,-20,70))        