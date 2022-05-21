from turtle import color
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

#Dogs, height, weight 
data = pd.read_csv('dogs.csv')

fig, ax = plt.subplots()
ax.bar(data.index, data["height_cm"], color = 'green')
ax.set_xticklabels(data.index, rotation = 90)
ax.set_ylabel("Breed of Dogs")
ax.set_xlabel("Number of Dogs")
ax.set_title("Number of Dogs per Breed")
plt.show()

#Dogs, height, weight 
fig, ax = plt.subplots()
ax.bar(data.index, data["height_cm"], label = "Height in cm ")
ax.bar(data.index, data["height_cm"], bottom = data["weight_kg"], label = "Weight in kg")
ax.legend()
plt.show()

#Data comparisons: histograms
fig, ax = plt.subplots()
ax.bar("Poodle", data["height_cm"].mean())
ax.bar("Labrador", data["height_cm"].mean())
ax.set_ylabel("Heigh (cm) of dogs")
plt.show()

#Introducing histograms
fig, ax = plt.subplots()
ax.hist(data["height_cm"], label = "Height in cm", bins = 5)
ax.hist(data["weight_kg"], label = "Weight in kg", bins = 5)
ax.set_xlabel("Number of Dogs")
ax.set_ylabel("Height (cm)")
ax.legend()
plt.show()