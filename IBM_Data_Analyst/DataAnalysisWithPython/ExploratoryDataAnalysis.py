import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
%matplotlib inline


path='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv'
df = pd.read_csv(path)

#calculate the correlation between variables
df.corr()
df[["bore", "stroke", "compression-ratio", "horsepower"]].corr()

#Plot the scatter plot and find the relationship
sns.regplot(x="engine-size", y="price", data=df)
plt.ylim(0,) # the result indicates positive  correlation
df[["engine-size", "price"]].corr()

#look at the relationship using boxplot
sns.boxplot(x="body-style", y="price", data=df)
sns.boxplot(x="engine-location", y="price", data=df)
sns.boxplot(x="drive-wheels", y="price", data=df)

#counting number of each type
drive_wheels_counts = df['drive-wheels'].value_counts().to_frame()
drive_wheels_counts.rename(columns={'drive-wheels': 'value_counts'}, inplace=True)
drive_wheels_counts.index.name = 'drive-wheels'

engine_loc_counts = df['engine-location'].value_counts().to_frame()
engine_loc_counts.rename(columns={'engine-location': 'value_counts'}, inplace=True)
engine_loc_counts.index.name = 'engine-location'

#Grouping
df['drive-wheels'].unique() #check the unique categories in the column = 'rwd', 'fwd', '4wd'
df['body-style'].unique() #'convertible', 'hatchback', 'sedan', 'wagon', 'hardtop'
df_group_one = df[['drive-wheels','body-style','price']]
grouped_test1 = df_group_one.groupby(['drive-wheels','body-style'],as_index=False).mean()

#creating pivot table
grouped_pivot = grouped_test1.pivot(index='drive-wheels',columns='body-style')
grouped_pivot = grouped_pivot.fillna(0) #fill missing values with 0

#plot heatmap
fig, ax = plt.subplots()
im = ax.pcolor(grouped_pivot, cmap='RdBu')
#label names
row_labels = grouped_pivot.columns.levels[1]
col_labels = grouped_pivot.index
#move ticks and labels to the center
ax.set_xticks(np.arange(grouped_pivot.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(grouped_pivot.shape[0]) + 0.5, minor=False)
#insert labels
ax.set_xticklabels(row_labels, minor=False)
ax.set_yticklabels(col_labels, minor=False)
#rotate label if too long
plt.xticks(rotation=90)
fig.colorbar(im)
plt.show()

#calculate pearson correlation coefficient and p-value
pearson_coef, p_value = stats.pearsonr(df['wheel-base'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)
