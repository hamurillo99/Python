#Merge Ordered (Time seriess data)
from numpy import append
import pandas as pd 
import matplotlib.pyplot as plt 
df1 = 1
df2 = 4
appl = 70
mcd = 44.4
visa = 89.55
ibm = 45
data = 23
social_fin = 45

pd.merge_ordered(appl, mcd, on ='date', suffixes = ('_appl', '_mcd'))
pd.merge_ordered(df1,df2)

#Forward Fill (Fills missing with previous values)
pd.merge_ordered(appl, mcd, on ='date',
                 suffixes = ('_appl', '_mcd'),
                 fill_method= 'ffill')

#Merge_asof(Data sampled from a process, developing a training set(no data leakage))
pd.merge_asof(visa, ibm, on = 'data_time',
                suffixes=('_visa','_ibm'))

pd.merge_asof(visa, ibm, on = 'data_time',
                suffixes=('_visa','_ibm')
                direction = 'forward'))

#Reshaping data with .melt()
social_fin_tall = social_fin.melt(id_vars = ['financial', 'company'])
print(social_fin_tall.head(10))

social_fin_tall = social_fin.melt(id_vars = ['financial', 'company'],
                                  value_vars = ['2018', '2017'])
print(social_fin_tall.head(9))

social_fin_tall = social_fin.melt(id_vars = ['financial', 'company'],
                                  value_vars = ['2018', '2017'],
                                  var_name = ['year'], value_name = 'dollars')
print(social_fin_tall.head(8))

#Wide Format 
#Long Format 

#EXAMPLE
# Use merge_ordered() to merge gdp and sp500, interpolate missing value
gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on='year', right_on='date', 
                             how='left',  fill_method='ffill')

print (gdp_sp500)

# Use merge_ordered() to merge inflation, unemployment with inner join
inflation_unemploy = pd.merge_ordered(inflation, unemployment, 
                                      on='date', how='inner') 
print(inflation_unemploy)

# Plot a scatter plot of unemployment_rate vs cpi of inflation_unemploy
inflation_unemploy.plot(kind='scatter', x='unemployment_rate', y='cpi')
plt.show()

# Use merge_asof() to merge jpm and wells
jpm_wells = pd.merge_asof(jpm, wells, on='date_time', 
                          suffixes=('', '_wells'), direction='nearest')

# Use merge_asof() to merge jpm_wells and bac
jpm_wells_bac = pd.merge_asof(jpm_wells, bac, on='date_time', 
                              suffixes=('_jpm', '_bac'), direction='nearest')

price_diffs = jpm_wells_bac.diff()

# Plot the price diff of the close of jpm, wells and bac only
price_diffs.plot(y=['close_jpm','close_wells','close_bac'])
plt.show()

#Selecting data with .query()
data.query('stock == "disney" or (stock == "nike" and close < 90))
           
# Merge gdp and pop on date and country with fill
gdp_pop = pd.merge_ordered(gdp, pop, on=['country','date'], fill_method='ffill')

# Add a column named gdp_per_capita to gdp_pop that divides the gdp by pop
gdp_pop['gdp_per_capita'] = gdp_pop['gdp'] / gdp_pop['pop']

# Use melt on ten_yr, unpivot everything besides the metric column
bond_perc = ten_yr.melt(id_vars='metric', var_name='date', value_name='close')

# Use query on bond_perc to select only the rows where metric=close
bond_perc_close = bond_perc.query('metric == "close"')

# Merge (ordered) dji and bond_perc_close on date with an inner join
dow_bond = pd.merge_ordered(dji, bond_perc_close, on='date', 
                            suffixes=('_dow', '_bond'), how='inner')

# Plot only the close_dow and close_bond columns
dow_bond.plot(y=['close_dow', 'close_bond'], x='date', rot=90)
plt.show()

