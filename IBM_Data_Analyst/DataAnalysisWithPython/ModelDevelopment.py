! mamba install pandas==1.3.3-y
! mamba install numpy=1.21.2-y
! mamba install sklearn=0.20.1-y

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# path of data
path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv'
df = pd.read_csv(path)
df.head()

#Create Single Linear Regression
lm = LinearRegression()
x = df[["highway-mpg"]]
y = df["price"]
lm.fit(x, y)
lm.intercept_ #value of intercept
lm.coef_ #value of coefficient

#Create Multiple Linear Regression
lm = LinearRegression()
z = df[["highway-mpg", "normalized-losses"]]
y = df["price"]
lm.fit(z,y)

#Model Evaluation using Visualization
import seaborn as sns
%matplotlib inline

#Regression plot
width = 12
height = 10

plt.figure(figsize= (wight, height))
sns.regplot(x = "highway-mpg", y = "price", data = df)
plt.ylim(0,)

sns.regplot(x = "peak-rpm", y = "price", data = df)
plt.ylim(0,)

#see correlation between variables
df[["peak-rpm", "highway-mpg", "price"]].corr()

#Residual plot
plt.figure(figsize=(width, height))
sns.residplot(df['highway-mpg'], df['price'])
plt.show()

#Visualizing multiple linear Regression - using distribution plot
Y_hat = lm.predict(z)
plt.figure(figsize=(width, height))
ax1 = sns.distplot(df['price'], hist=False, color="r", label="Actual Value") #plotting dependent variable
sns.distplot(Y_hat, hist=False, color="b", label="Fitted Values" , ax=ax1) #plotting independent variables

#setting title and label names
plt.title('Actual vs Fitted Values for Price')
plt.xlabel('Price (in dollars)')
plt.ylabel('Proportion of Cars')

plt.show()
plt.close()

#Polynomial Regression
def PlotPoly(model, independent_variable, dependent_variable, Name):
    x_new = np.linspace(15, 55, 100)
    y_new = model(x_new)

    plt.plot(independent_variable, dependent_variabble, '.', x_new, y_new, '-')
    plt.title('Polynomial Fit with Matplotlib for Price ~ Length')
    ax = plt.gca()
    ax.set_facecolor((0.898, 0.898, 0.898))
    fig = plt.gcf()
    plt.xlabel(Name)
    plt.ylabel('Price of Cars')

    plt.show()
    plt.close()

x = df['highway-mpg']
y = df['price']

f = np.polyfit(x, y, 3) #fit the third-order polynomial
p = np.poly1d(f) #model
PlotPoly(p, x, y, 'highway-mpg') #plot the polynomial regression

f1 = np.polyfit(x, y, 11) #fit the eleventh-order polynomial
p1 = np.poly1d(f1)
PlotPoly(p1, x, y, 'highway-mpg')

#Measure of in-sample Evaluation - R-squared and Mean Squared Error
lm.fit(x,y)
lm.score(x,y) # r-Squared

from sklearn.metrics import mean_squared_error
Yhat = lm.predict(x)
Yhat[0:4] # first four predicted Value
mse = mean_squared_error(df["price"], Yhat) #Mean squared error (MSE)

#Prediction and Decision Making
import matplotlib.pyplot as plt
%matplotlib inline

new_input=np.arange(1, 100, 1).reshape(-1, 1)
lm.fit(x, y)
yhat=lm.predict(new_input)

plt.plot(new_input, Yhat)
plt.show()
