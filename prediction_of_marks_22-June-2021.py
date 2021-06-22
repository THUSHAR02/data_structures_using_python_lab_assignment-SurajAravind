##  A simple attempt to predict module 2 Test marks

# importing libraries
import numpy as np
import pandas as pd
import sklearn     #free software machine learning library
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error , r2_score

dataset = pd.read_csv("data_set.csv")
#print(dataset.head())

registration_numbers = dataset.iloc[:,0].values
names = dataset.iloc[:,1].values
mid_1_marks = dataset.iloc[:,2].values
mid_2_marks = dataset.iloc[:,3].values

array_1 = mid_1_marks.reshape(-1,1)
#print (array)

array_2 = mid_2_marks.reshape(-1,1)

from sklearn.model_selection import train_test_split
mid_1_marks_train, mid_1_marks_test, mid_2_marks_train, mid_2_marks_test = train_test_split(array_1,mid_2_marks,test_size=.25,random_state=5)

lm = LinearRegression()
lm.fit(mid_1_marks_train,mid_2_marks_train)
mid_2_train_pred = lm.predict(mid_1_marks_train)
mid_2_test_pred = lm.predict(mid_1_marks_test)

predicted_list_01 = mid_2_train_pred.tolist()
predicted_list_02 = mid_2_test_pred.tolist()

predicted_list_01.append(predicted_list_02)
print(predicted_list_01)

df = pd.DataFrame(mid_2_test_pred,mid_2_marks_test)

mse = mean_squared_error(mid_2_marks_test,mid_2_test_pred)
print(mse)


plt.scatter(mid_2_marks_train, mid_2_train_pred, c='blue', marker = 'o', label='Training data')
plt.scatter(mid_2_marks_test, mid_2_test_pred, c='red', marker = '*', label='Test data')
plt.xlabel('Marks Obtained')
plt.ylabel('Predicted Marks')
plt.title('Obtained Marks vs Predicted Marks')
plt.legend(loc = 'upper left')
plt.plot()
plt.show()


