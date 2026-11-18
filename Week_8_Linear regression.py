# Importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

#Read the datasets
dataset = pd.read_csv("weight-height.csv")

print(dataset.head())

print(dataset.isnull().sum())
print(dataset.shape)

#check if null values is present in dataset or not.....
plt.scatter(dataset["Height"], dataset["Weight"])
plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("Height vs Weight")
plt.show()
#Plot Gender vs Weight............
x1 = dataset.iloc[:, 0].values
y1 = dataset.iloc[:, 2].values
plt.scatter(x1,y1,label='Gender',color='Green',s=50)
plt.xlabel('Gender')
plt.ylabel('Weight')
plt.title('Gender vs Weight')
plt.legend()
plt.show()

#Plot Height vs Weight............
x2 = dataset.iloc[:, 1].values
y2 = dataset.iloc[:, 2].values
plt.scatter(x2,y2,label='Height',color='Orange',s=50)
plt.xlabel('Height')
plt.ylabel('Weight')
plt.title('Height vs Weight')
plt.legend(loc="lower right")
plt.show()