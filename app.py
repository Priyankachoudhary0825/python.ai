from fastapi import FastAPI,HTTPException,UploadFile,File,Depends
from pydantic import BaseModel
from typing import List,Optional
app=FastAPI()
#Question 1:
@app.get("/")
def read_root():
    return{"Message":"Welcome to FastAPI"}

#Question 2:
@app.get("/about")
def about():
    return{"Name":"Your Name","Course":"Your Course","College":"Your College"}

# Question 3:
@app.get("/user/{user_id}")
def get_user(user_id:int):
    return{"user_id":user_id}

# Question 4:
@app.get("/search")
def search(q:str):
    return{"query":q}

# Question 6:
users_db=[{"ID":1,"Name":"Ankush","Age":24,"City":"Delhi"}
         ,{"ID":2,"Name":"Rahul","Age":28,"City":"Mumbai"}
         ,{"ID":3,"Name":"Payal","Age":22,"City":"Bangalor"}]

class User(BaseModel):
    id:int
    name:str
    age:int
    city:Optional[str]=None

#Question 5:
@app.post("/user")
def create_user(user:User):
    return user

#Question 7:
@app.get("/users")
def get_users():
    return users_db

#post user to DB
@app.post("/users")
def add_user(user:User):
    return{"Message":"User added","user":user}

# Get user by ID
@app.get("/user/{id}")
def get_user_by_id(id:int):
    for user in users_db:
        if user.id==id:
            return user
        raise HTTPException(status_code=404,detail="User not Found")
    
# Update user
@app.put("/users/{id}")
def update_user(id:int,update_user:User):
    for index,user in enumerate(users_db):
        if user.id==id:
            users_db[index]=update_user
            return{"Message":"User update","user":update_user}
        raise HTTPException(status_code=404,detail="User not Found")

#deleted user:
@app.delete("/user/{id}")
def delete_user(id:int):
    for index, user in enumerate(users_db):
        if user.id==id:
            delete_user=users_db.pop(index)
            return{"Message":"User delete","user":delete_user}    
        raise HTTPException(status_code=404,detail="User not Found")


