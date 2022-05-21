import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

#CREATING DATAFRAMES 

#DICTIONARIES OF LISTS 
dict_of_lists = {
    "name": ["Rocky", "Chimuelo"],
    "breed": ["German shepherd", "Poug"],
    "height_cm": [45, 23],
    "weight_kg": [30, 12],
    "date_of_birth": ["2019-03-14", "2020-06-23"]
}
new_dogs1 = pd.DataFrame(dict_of_lists)
print(new_dogs1)

#LIST OF DICTIONARIES
list_of_dicts = [
    {"name": "Rocky", "breed": "German shepherd", "height_cm": 45, 
     "weight_kg": 30, "date_of_birth":"2019-03-14"},
    {"name": "Chimuelo", "breed": "Poug", "height_cm": 23, 
     "weight_kg": 12, "date_of_birth":"2020-06-23"}
    
]
new_dogs = pd.DataFrame(list_of_dicts)
print(new_dogs)

#READING AND WRITING CSVs

#DataFrame to CSV 
new_dogs.to_csv("variable_created.csv")

# From previous steps
airline_bumping = pd.read_csv("airline_bumping.csv")
print(airline_bumping.head())
airline_totals = airline_bumping.groupby("airline")[["nb_bumped", "total_passengers"]].sum()
airline_totals["bumps_per_10k"] = airline_totals["nb_bumped"] / airline_totals["total_passengers"] * 10000
print(airline_totals)

# Create airline_totals_sorted
airline_totals_sorted = airline_totals.sort_values("bumps_per_10k", ascending=False)
print(airline_totals_sorted)
airline_totals_sorted.to_csv("airline_totals_sorted.csv")