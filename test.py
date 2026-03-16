#Task 1- python programming:
#problem 1-Frequency counter
from collections import counter
list=[1,2,2,3,3,3,4,4,4,4]
freq={}
for num in numbers:
    if num is freq:
       freq[num]+=1
    else:
    #   freq[num]=1




#problem 2-dictionary transform:
data={
    "Aman ":[85,90,78],
    "Eakam ":[92,88,95],
    "Kiran ":[70,75,80]

}
averages={}
for student in data:
  scores=data[student]
avg=sum(scores)/len(scores)
averages[student]=avg
print(student+":",round(avg,1))
#top_student
top_student=max(averages,
key=averages.get)
print("Top Student:",top_student)


# 2nd Data Loading & preprocess
import pandas as pd
import numpy as np
df=pd.read_csv("Dataset_Pr_2_ML(1)(1).csv")
df.head()
df.shape()
df.columns()
num_cols = df.select_dtypes(include=['int64','float64']).columns
cat_cols = df.select_dtypes(include=['object']).columns

print("Numerical Columns:", num_cols)
print("Categorical Columns:", cat_cols)


df.isnull().sum()


for col in num_cols:
    df[col].fillna(df[col].mean(), inplace=True)

for col in cat_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)


df = df.drop_duplicates()

df = pd.get_dummies(df, columns=cat_cols)

print("Cleaned Data:")
print(df.head())



# 3rd Exploratory data analysis(EDA)
#Requried visualizations:
import matplotlib.pyplot as plt
import seaborn as sns


df.hist(figsize=(10,8))
plt.show()


plt.figure(figsize=(8,6))
sns.heatmap(df.corr(), annot=True)
plt.show()


sns.countplot(x=df.columns[0], data=df)
plt.show()
sns.boxplot(data=df)
plt.show()

plt.scatter(df.iloc[:,0], df.iloc[:,1])
plt.xlabel(df.columns[0])
plt.ylabel(df.columns[1])
plt.show()
 
 # 4th Feature Engineering
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
df=pd.read_csv("Dataset_pr_2_ML(1(1).csv)")
df=["number_project"]=df=["salary"]+["average_monthly"]+1
df=df.drop[("average_monthly")]
df=df.get_dummies(df,columns=["salary"],drop_first=True)
x=df.drop("Depatment",axis=1)
y=df["Dapatment"]
x_train,x_test,y_train,y_test=train_test_split(x,y,text_size=0.2,random_state=42)
print("Feature engineering ")
print("Training shap:",x_train.shap)

# 5th Machine learinng
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier



data=pd.read_csv("Dataset_pr_2_ML(1)(1).csv"
                 )
data.drop("Outcome",axis=1)
y=data["Outcome"]
x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.2,random_state=42)
scaler=StandardScaler()
x_train=scaler.fit_transform(x_train)
x_test=scaler.fit_transform(x_test)
models={
    "LogisticRegression":
LogisticRegression(),
"Random Forest":
RandomForestClassifier(),
"Decision Tree":

}
results={}
for name,model in models.items():
    model.fit(x_train ,y_train)
    y_pred=model.predict(x_test)
    accuracy=accuracy_score(y_test,y_pred)
    results[name]=accuracy
    print(name,"Accuracy:",accuracy)
    best_model=max(results,key=results.get)
    print("\nbest model:",best_model)
    print("best accuracy:",results[best_model])
    

    