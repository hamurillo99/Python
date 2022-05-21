#Inner Join 
import matplotlib.pyplot as plt 
import pandas as pd

movies = 90
taglines = 90
data = 34
data1 = 43
data2 = 45
data3 = 000
df1 = 3
df2 = 9
df3 = 4
df4 = 8
data_name = 98
genre = 78

#Merging tables 
wards_census = data1.merge(data2, on = 'comun_column')
print(wards_census.head(4))

#Suffixes
wards_census = data1.merge(data2, on = 'comun_column', suffixes =('_ward', '_cen'))
print(wards_census.head())
print(wards_census.shape())

#One-to-many (row,column)
data1_data2 = data1.merge(data2, on = 'comun_column', suffixes = ('_data1', '_data2'))
print(data1_data2.head())
print(data1_data2.shape())

#Single Merge 
data1.merge(data2, on = ['comun_column1', 'comun_column2'])

#Merging multiple tables 
data1_data2_data3 = data1.merge(data2, on = ['comun_column1', 'comun_column2']) \
    .merge(data3, on = 'comun_column', suffixes = ('_datan', '_data3'))
data1_data2_data3.head()

data1_data2_data3.groupby('data3').agg('sum').plot(kind = 'bar', y= 'data1')
plt.show()

#Three tables
df1.merge(df2, on ='col') \
    .merge(df3, on = 'col')

#Four tables
df1.merge(df2, on ='col') \
    .merge(df3, on = 'col')\
        .merge(df4, on = 'col')


data1_data2 = data1.merge(data2, on = 'comun_column')
print(data1_data2.loc[data1_data2['column'] == "random_data",
                      ['comun_column1', 'comun_column2']])

#Merge with left join 
data1_data2 = data1.merge(data2, on = 'comun_column', how = 'left')
print(data1_data2.head())

# Count the number of rows in the budget column that are missing
number_of_missing_fin = data['column'].isnull().sum()
print(number_of_missing_fin)

# Merge the toy_story and taglines tables with a inner join
toystory_tag = toy_story.merge(taglines, on='id', how = 'inner')

#Right join 
#Looking at data 
data = data_name[data_name['column'] == 'data']
print(data)

#Filtering the data 
m = data_name['column'] == 'data'
x_variable = data_name[m]
print(x_variable)

#Merge with right join 
y_variable = data1.merge(data2, how = 'right', lef_on = 'id', right_on = 'movie_id')
print(y_variable.head())

#Outer join 
m = data_name['column'] == 'data'
data = data_name[m].head(0-4)

n = data_name['column'] == 'data'
data = data_name[n].head(0-4)

#Merge with outer join 
data1_data2 = data1.merge(data2, on= 'comun_column', how = 'outer', suffixes= ('_fam', '_com'))
print(data1_data2)

# Merge action_movies to the scifi_movies with right join
action_scifi = data1.merge(data2, on='movie_id', how='right',
                                   suffixes=('_act','_sci'))

# From action_scifi, select only the rows where the genre_act column is null
scifi_only = action_scifi[action_scifi['genre_act'].isnull()]

# Use right join to merge the movie_to_genres and pop_movies tables
genres_movies = data1.merge(data2, how='right', 
                                      left_on='movie_id', 
                                      right_on='id')

genre_count = genres_movies.groupby('genre').agg({'id':'count'})

# Plot a bar chart of the genre_count
genre_count.plot(kind='bar')
plt.show()

# Merge iron_1_actors to iron_2_actors on id with outer join using suffixes
data_1_data_2 = data1.merge(data2, 
                                     on='id', 
                                     how='outer', 
                                     suffixes=('_1','_2'))

# Create an index that returns true if name_1 or name_2 are null
m = ((data1['name_1'].isnull()) | 
     (data2['name_2'].isnull()))

# Print the first few rows of iron_1_and_2
print(data_1_data_2[m].head())

#Merging a table to itself 
original_data = data.merge(data, left_on = 'data_column', right_on = 'data_column',
                           suffixes = ('_org', '_seq'))
print(original_data.head())

#Continue format results 
print(original_data[,['title_org','title_seq']].head())

#Merging a table to itself with left join 
# Hierarchical relationships, sequential relationships, graph data
original_data = data.merge(data, left_on = 'column', right_on = 'column',
                           how = 'left', suffixes = ('_org', '_seq'))
print(original_data.head())

# Merge the crews table to itself
crews_self_merged = data.merge(data, on='id', how='inner',
                                suffixes=('_dir','_crew'))

# Create a boolean index to select the appropriate rows
boolean_filter = ((crews_self_merged['job_dir'] == 'Director') & 
                  (crews_self_merged['job_crew'] != 'Director'))
direct_crews = crews_self_merged[boolean_filter]

# Print the first few rows of direct_crews
print(direct_crews.head())

#Merging on indexes
#Setting an index
data = pd.read_csv('dogs', index_col = ['id'])
print(data.head())

movies_taglines = movies.merge(taglines, on = 'id', how = 'left')
print(movies_taglines.head())

#Multilndex datasets 
samuel = pd.read_csv('samuel.csv', 
                     index_col = ['movie_id',
                                  'cast_id'])
print(samuel.head())

casts = pd.read_csv('cast.csv',
                    index_col = ['movie_id',
                                  'cast_id'])
print(casts.head())

samuel_casts = samuel.merge(casts, on = ['movie_id', 'cast_id'])
print(samuel_casts.head())
print(samuel_casts.shape)

#Index merge with left_on and right_on
movies_genres = movies.merge(genre, left_on = 'id', left_index = True, 
                             right_on = 'movie_id', right_index = True)

#Filtering joins 
#Step 1 (Semi join)
data1_data2 = data1.merge(data2, on = 'comun_column')
print(data1_data2.head())

#Step 2 (Semi join)
data1['comun_column'].isin(data1_data2['comun_column'])

#Step 3 (Semi join)
top_genres = data1[data1['comun_column'].isin(data1_data2['comun_column'])]
print(top_genres.head())

#Anti join (1)
data1_data2 = data1.merge(data2, on = 'comun_column', how = 'left', indicator = True)
print(data1_data2)

#Anti join (2) (3)
comun_column_list = data1_data2.loc[data1_data2['_merge'] == 'left_only', 'comun_column']
non_top_data1 = data1[data1['comun_column'].isin(comun_column_list)]
print(comun_column_list.head())


#Concatenate two tables vertically 
#inv_jan (top)
#inv_feb (middle)
#inv_mar (bottom)

#Basic concatenation
pd.concat([inv_jan, inv_feb, inv_mar])

#Setting labels to original tables
pd.concat([inv_jan, inv_feb, inv_mar],
          ignore_index = False,
          keys = ['jan','feb', 'mar'])

#Concatenate tables with different column names
pd.concat([inv_jan, inv_feb],
          sort = True)

pd.concat([inv_jan, inv_feb],
          join = 'inner')

#Append the tables 
inv_jan.append([inv_feb, inv_mar],
               ignore_index = True,
               sort = True)

#Verifying integrity 
data.merge(validate = None)

#Merge validate: one_to_one
data1.merge(data2, on= 'comun_column',
            validate = 'one_to_one')


#Merge validate: one_to_many
data1.merge(data2, on='comun_column',
            validate = 'one_to_many')

#Verifying concatenations
data.concat(verify_integrity = False)
pd.concat([inv_feb, inv_mar],
          verify_integrity= True)
pd.concat([inv_feb, inv_mar],
          verify_integrity= False)