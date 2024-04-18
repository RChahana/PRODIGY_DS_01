import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("movies.csv")
print(df.shape)
print(df.info())
#Removing duplicate records
df=df.drop_duplicates("MOVIES",keep='first')
print(df.shape)
print(df.info())
#Cleaning Data 
#filling Null value for Numeric data and Catogorical data separately
#Numerical Data
df.isnull().sum()
df['RATING'].fillna(df['RATING'].mean(),inplace=True)
df['VOTES'].fillna(df['VOTES'].mean(),inplace=True)
df['RunTime'].fillna(df['RunTime'].mean(),inplace=True)
#Catorgorical Data
print(df['MOVIES'].value_counts())  #No missing values
print(df['ONE-LINE'].value_counts())
print(df['Gross'].value_counts())
print(df['GENRE'].value_counts())
print(df['YEAR'].value_counts())
df['ONE-LINE'].fillna("X",inplace=True)
df['Gross'].fillna("$0.01M",inplace=True)
df['GENRE'].fillna("Comedy",inplace=True)
df['YEAR'].fillna("2020",inplace=True)
print(df.isnull().sum())

genre_series = df['GENRE'].str.split(',').explode().str.strip()
# Count the frequency of each genre
genre_counts = genre_series.value_counts()
# Plotting the distribution of genres
plt.figure(figsize=(12,8 ))
genre_counts.plot(kind='bar', color='lavender', edgecolor='black')

# Adding labels and title
plt.xlabel('Genre')
plt.ylabel('Frequency')
plt.title('Distribution of Movie Genres')

# Displaying the plot
plt.tight_layout()
plt.show()
