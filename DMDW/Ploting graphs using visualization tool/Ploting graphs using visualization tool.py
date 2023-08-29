import pandas as pd
data=pd.read_csv("/content/Iris.csv")
data=print(data.head(10))

import pandas as pd
dataset=pd.read_csv('Iris.csv')

import pandas as pd
import matplotlib.pyplot as plt
import statistics as st
import seaborn as sns
data=pd.read_csv("/content/Iris.csv")
#plt.plot(data.Id,data['PetalLengthCm'],"m--")
v=data['PetalLengthCm']
x=st.mean(v)
y=st.mode(v)
z=st.median(v)
print("Mean is ",x)
print("Mode is ",y)
print("Median is ",z)
stddv=st.stdev(v)
variance=st.variance(v)
print("Variance= ",variance)
print("Standard Deviation= ",stddv)
plt.boxplot(v)
#sns.boxplot(v)
sns.boxplot(x=data['PetalLengthCm'],y=data['SepalLengthCm'])
#sns.boxplot(x=data['PetalLengthCm'],y=data['SepalLengthCm'],hue=data['SepalWidthCm'])
plt.show

import pandas as pd
data=pd.read_csv("/content/Salary_Data.xls")
data=print(data.head(120))
#G=data['Age']
#plt.boxplot(Gender)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("/content/Iris.csv")
d = pd.DataFrame({"Box1": data.PetalLengthCm, "Box2": data.SepalLengthCm})
ax = d[['Box1', 'Box2']].plot(kind='box', title='boxplot')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv("/content/ToyotaCorolla.csv")
print(data.head(2))
plt.scatter(data.Price,data.KM,c="orange")
d = pd.DataFrame ({"Box1": data.Age, "Box2": data.HP, "Box3": data.FuelType, "Box4": data.MetColor})
ax = d[['Box1', 'Box2','Box3','Box4']].plot(kind='box', title='boxplot')
plt.show
plt.rcParams["figure.figsize"] = (10,6)
plt.subplot(2,2,1)
x1=data.Age
y1=data.Price
plt.scatter(x1,y1,c='r')
plt.grid()

plt.subplot(2,2,2)
x1=data.KM
y1=data.Price
plt.scatter(x1,y1,c='r')
plt.grid()

plt.hist(data.CC)
plt.show()
