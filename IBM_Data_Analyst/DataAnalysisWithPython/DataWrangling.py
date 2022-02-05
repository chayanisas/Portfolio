import pandas as pd
import matplotlib.pylab as plt
import numpy as np
from matplotlib import pyplot

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df = pd.read_csv(filename, names = headers)

# replace "?" to NaN
df.replace("?", np.nan, inplace = True)
df.head(5)

# check if there is a missing value
missing_data = df.isnull()
missing_data.head(5)

#count how many missing value
for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")

# "normalized-losses": 41 missing data  - replace with mean
avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
df["normalized-losses"].replace(np.nan, avg_norm_loss, inplace=True)

#"num-of-doors": 2 missing data - replace with frequency = four
df["num-of-doors"].value_counts().idmax()
df["num-of-doors"].replace(np.nan, "four", inplace=True)

# "bore": 4 missing data - replace with mean
avg_bore = df["bore"].astype("float").mean(axis=0)
df["bore"].replace(np.nan, avg_bore, inplace=True)

# "stroke" : 4 missing data - replace with mean
avg_stroke = df["stroke"].astype("float").mean(axis=0)
df["stroke"].replace(np.nan, avg_stroke, inplace=True)

# "horsepower": 2 missing data - replace with mean
avg_horsepower = df['horsepower'].astype('float').mean(axis=0)
df['horsepower'].replace(np.nan, avg_horsepower, inplace=True)

# "peak-rpm": 2 missing data - replace with mean
avg_peakrpm=df['peak-rpm'].astype('float').mean(axis=0)
df['peak-rpm'].replace(np.nan, avg_peakrpm, inplace=True)

# "price": 4 missing data - drop the whole row
df.dropna(subset=["Price"], axis=0, inplace=True)
df.reset_index(drop=True, inplace=True)

#convert data into appropriate format
df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")
df[["price"]] = df[["price"]].astype("float")
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")

#convert data and drop column
df["highway-L/100km"] = 235/df["highway-mpg"]
df.drop(["highway-mpg"], axis = 1, inplace=True)

#Normalizing the data
df['length'] = df['length']/df['length'].max()
df['width'] = df['width']/df['width'].max()
df['height'] = df['height']/df['height'].max()

#Plotting the data
df["horsepower"]=df["horsepower"].astype(int, copy=True)
%matplotlib inline
pyplot.hist(df["horsepower"])

#labels and plot title
pyplot.xlabel("horsepower")
pyplot.ylabel("count")
pyplot.title("horsepower bins")

#Binning the Data
bins = np.linspace(min(df["horsepower"]), max(df["horsepower"]), 4)
group_names = ['Low', 'Medium', 'High']
df['horsepower-binned'] = pd.cut(df['horsepower'], bins, labels=group_names, include_lowest=True ) #determine which each value belong to
df[['horsepower','horsepower-binned']].head(20)

#count number of values in each bin
df["horsepower-binned"].value_counts()

# draw historgram of attribute "horsepower" with bins = 3
pyplot.hist(df["horsepower"], bins = 3)
pyplot.xlabel("horsepower")
pyplot.ylabel("count")
pyplot.title("horsepower bins")

#Assigning dummy variables
dummy_variable_1 = pd.get_dummies(df["fuel-type"])
dummy_variable_1.rename(columns={'gas':'fuel-type-gas', 'diesel':'fuel-type-diesel'}, inplace=True)

#merge 2 dataframe (dummy table and original table) and drop orginal column of fuel-type
df = pd.concat([df, dummy_variable_1], axis=1)
df.drop("fuel-type", axis = 1, inplace=True)
