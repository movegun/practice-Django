import openpyxl
import pandas as pd
from pyexpat import model
import matplotlib as mat
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
mat.rcParams['font.family'] = 'Hancom Gothic'
import numpy as np
from sklearn.linear_model import LinearRegression
import sklearn
# [1] 2012년 엑셀파일 읽기
df_2012 = pd.read_excel("C:/Users/Kosmo/Desktop/파이썬데이터베이스자료실/excels/2012.xlsx", engine="openpyxl")

df_2012.astype({'낱일':'int64','거래금액(만원)':'int64'})

print(df_2012.describe())

df_x = df_2012.groupby('낱일').mean().reset_index()
print(df_x)



x=np.array(df_x['낱일'].tolist())
print(x)
y=np.array(df_x['거래금액(만원)'].tolist())
print(y)

plt.scatter(x,y)
plt.show()

x_train, x_test, y_train, y_test  = train_test_split(x,y,train_size=0.8, test_size=0.2)


my_model = LinearRegression()
my_model.fit(x_train,y_train)


y_predict = my_model.predict(150)
plt.scatter(y_test , y_predict , alpha=0.4)

plt.xlabel('실제값')
plt.ylabel('예측값')

plt.show()
print(my_model.score(x_train,y_train))
