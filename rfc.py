import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
data= pd.read_csv("mnist.csv")
data.head()
a=data.iloc[3,1:].values
a=a.reshape(28,28).astype('uint8')
plt.imshow(a)
df_x=data.iloc[:,1:]
df_y=data.iloc[:,0]
from sklearn.model_selection import train_test_split
x_train, x_test ,y_train ,y_test = train_test_split(df_x,df_y,test_size=0.2,random_state=4)
x_train.head()
from sklearn.ensemble import RandomForestClassifier
rf=RandomForestClassifier(n_estimators=100)
rf.fit(x_train, y_train)
pred=rf.predict(x_test)
print(pred)
s=y_test.values
count =0
for i in range(len(pred)):
  if pred[i]==s[i]:
    count=count+1
count
accuracy=count/len(pred)
print(accuracy)
    
