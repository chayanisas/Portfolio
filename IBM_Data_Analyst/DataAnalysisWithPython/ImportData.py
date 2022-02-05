
! mamba install pandas==1.3.3  -y
! mamba install numpy=1.21.2 -y
import pandas as pd
import numpy as np

# Read the online file by the URL, and assign it to variable "df"
other_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
df = pd.read_csv(other_path, header=None)

# show the first 5 rows
print("The first 5 rows of the dataframe")
df.head(5)

#Check the bottom 10 rows of data frame "df".
print("The last 10 rows of the dataframe\n")
df.tail(10)

#Add headers to the columns
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
df.columns = headers
df.head(10)

# replace the "?" symbol with NaN
df1 = df.replace('?',np.NaN)

# drop row which contain missing value in price column
df = df1.dropna(subset=["price"], axis=0)

# save the dataset
df.to_csv("automobile.csv", index=False)

# See data types
df.dtypes

#Descriptive Statistics of the dataset
df.describe(include ="all")
df[['length', 'compression-ratio']].describe()
df.info()
