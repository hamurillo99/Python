import pandas as pd 
import matplotlib.pyplot as plt 

#DATA VISUALIZATION
data = pd.read_csv('dogs.csv')
print(data.head())

data1 = 30
data2 = 89

#Adding data to axes
fig, ax = plt.subplots()
ax.plot(data["height_cm"], data["name"])
ax.plot(data["weight_kg"], data["name"])
plt.show()

#Customizing plots (markers = v, linestyle = None)
ax.plot(data["height_cm"], 
        data["name"],
        marker = "o", linestyle = "--", color = "r")
ax.set_xlabel("Data Labels")
ax.set_ylabel("Data Labels")
ax.set_title("Data Labels")
plt.show()

#Small multiples
rows = 2
columns = 3

fig, ax = plt.subplots()
fig, ax = plt.subplots(rows, columns)
plt.show()

fig, ax = plt.subplots(2, 1)
ax[0].plot(data["height_cm"], data["name"], color = 'b')
ax[1].plot(data["height_cm"], data["name"], color = 'b')

ax[0].set_xlabel("Data Labels")
ax[0].set_ylabel("Data Labels")
ax[0].set_title("Data Labels")

ax[1].set_xlabel("Data Labels")
ax[1].set_ylabel("Data Labels")
ax[1].set_title("Data Labels")
plt.show()

#Sharing the y-axis range (This means that they are sharing the same column)
fig, ax = plt.subplots(2, 1, sharey= True)

#Plotting time-series data
sixties = data["1960-01-01":"1969-12-31"]
fig, ax = plt.subplots()
ax.plot(sixties.index, data['columns'])
ax.set_xlabel("Data Labels")
ax.set_ylabel("Data Labels")
plt.show()

#Plotting time-series with different variables
data = pd.read_csv('dogs.csv',
                   parse_dates = ["date"],
                   index_col= "date")

#Using twin axes (Share same x axis)
fig, ax = plt.subplots()
ax.plot(data.index, data["columns"], color = 'blue')
ax.set_xlabel("Data Labels")
ax.set_ylabel("Data Labels", color = 'blue')
ax.tick_params('y', colors = 'blue')
ax2 = ax.twinx()
ax2.plot(data.index, data["column"], color  = 'red')
ax2.set_ylabel("Data Labels", color = 'red')
ax2.tick_params('y', colors = 'red')
plt.show()

def plot_timeseries(axes, x, y, color, xlabel, ylabel):
    axes.plot(x,y, color = color)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel, color=color)
    axes.tick_params('y', colors = color)
    
#Plotime series function
plot_timeseries(axes, x, y, color, xlabel, ylabel)
    
#Annotating time-series data 
ax2.annotate(">1 degree", 
             xy = (pd.Timestamp("2015-10-06"), 1))

#Positioning the text 
ax2.annotate(">1 degree", 
             xy = (pd.Timestamp("2015-10-06"), 1),
             xytext = (pd.Timestamp('2008-10-06'), -0.2))

#Adding arrows to annotation
ax2.annotate(">1 degree", 
             xy = (pd.Timestamp("2015-10-06"), 1),
             xytext = (pd.Timestamp('2008-10-06'), -0.2),
             arrowprops = {})

#Customizing arrow properties
ax2.annotate(">1 degree", 
             xy = (pd.Timestamp("2015-10-06"), 1),
             xytext = (pd.Timestamp('2008-10-06'), -0.2),
             arrowprops = {"arrowstyle":"->", "color":"gray"})
 
# EXAMPLE
fig, ax = plt.subplots(2, 1, sharey=True)

# Plot Seattle precipitation in the top axes
ax[0].plot(data["MONTH"], data["MLY-PRCP-NORMAL"], color='b')
ax[0].plot(data["MONTH"], data["MLY-PRCP-25PCTL"], color='b', linestyle='--')
ax[0].plot(data["MONTH"], data["MLY-PRCP-75PCTL"], color='b', linestyle='--')

# Plot Austin precipitation in the bottom axes
ax[1].plot(data["MONTH"], data["MLY-PRCP-NORMAL"], color='r')
ax[1].plot(data["MONTH"], data["MLY-PRCP-25PCTL"], color='r', linestyle='--')
ax[1].plot(data["MONTH"], data["MLY-PRCP-75PCTL"], color='r', linestyle='--')

fig, ax = plt.subplots()

ax.plot(data.index, data["relative_temp"])
ax.set_xlabel('Time')
ax.set_ylabel('Relative temperature (Celsius)')
plt.show()

fig, ax = plt.subplots()

# Plot the CO2 levels time-series in blue
plot_timeseries(ax, data.index, data["co2"], 'blue', "Time (years)", "CO2 levels")
ax2 = ax.twinx()
plot_timeseries(ax2, data.index, data['relative_temp'], 'red', "Time (years)", "Relative temperature (Celsius)")
ax2.annotate(">1 degree", xy = (pd.Timestamp("2015-10-06"), 1))
plt.show()

# Quantitative comparisons: bar-charts
data = pd.read_csv('dogs.csv', index_col= 0)
fig, ax = plt.subplots()
ax.bar(data.index, data["Greed"])
plt.show()

#Visualizing the other data
fig, ax = plt.subplots()
ax.bar(data.index, data["Greed"])
ax.bar(data.index, data["Greed"], bottom = data["name"])
ax.set_xticklabels(data.index, rotation = 90)
ax.set_ylabel("Title of Chart")
plt.show()

#Visualizing all three with legend
fig, ax = plt.subplots()
ax.bar(data.index, data["Greed"])

ax.bar(data.index, data["Greed"], bottom = data["name"],
       label = "Title data")
ax.bar(data.index, data["1st_column"],
       bottom = data["2nd_column"] + data["3rd_column"],
       label = "Title data")

ax.set_xticklabels(data.index, rotation = 90)
ax.set_ylabel("Title of chart")
plt.show()

# Quantitative comparisons:histograms 
fig, ax = plt.subplots()
ax.bar("Data_1", data["column"].mean())
ax.bar("Data_2", data["column"].mean())
ax.set_ylabel("Title")
plt.show()
 
#Introducing histograms
fig, ax = plt.subplots()
ax.hist(data["column"], label = "Title", bins = "n")
ax.hist(data["column"], label = "Title", bins = "n")
ax.set_xlabel("Title")
ax.set_ylabel("Title")
ax.legend()
plt.show()

#Customizing histograms: setting bin boundaries (transparency)
ax.hist(data["column"], label = "Title", 
        bins = [1, 2, 3, 4, "n...."],
        histtype= "step")
ax.hist(data["column"], label = "Title", 
        bins = [1, 2, 3, 4, "n...."]
        histtype= = "step")

ax.set_xlabel("Title")
ax.set_ylabel("Title")
ax.legend()
plt.show()

#Statistical plotting 
fig, ax = plt.subplots()
ax.bar("data1",
       data["column"].mean(),
       yerr = data1["column"].std())

ax.bar("data2",
       data["column"].mean(),
       yerr = data2["column"].std())

ax.set_ylabel("Height (cm)")
plt.show()

#Adding error-bars to a plot
fig, ax = plt.subplots()

# Add Seattle temperature data in each month with error bars
ax.errorbar(data1_xlabel["MONTH"],
            data1_ylabel["MLY-TAVG-NORMAL"], 
            data1_yerr["MLY-TAVG-STDDEV"])

# Add Austin temperature data in each month with error bars
ax.errorbar(data2_xlabel["MONTH"], 
            data2_ylabel["MLY-TAVG-NORMAL"], 
            data2_yerr["MLY-TAVG-STDDEV"])

ax.set_ylabel("Title")
plt.show()

#Adding boxplots
fig, ax = plt.subplots()
ax.boxplot([data1["column"],
            data2["column"]])
ax.set_xticklabels(["Name_data_1", "Name_data_2"])
ax.set_ylabel("Title")
plt.show()

#Scatter plots 
ax.scatter(data["column_name"], data["column_name"])
ax.set_xlabel("Title")
ax.set_ylabel("Title")
ax.legend()
plt.show()

#Encoding a third variable by color 
ax.scatter(data["column_name"], data["column_name"],
           c = data.index)
ax.set_xlabel("Title")
ax.set_ylabel("Title")
plt.show()
