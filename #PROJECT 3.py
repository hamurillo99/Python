#PROJECT 3
import pandas as pd 
# Loading in the data
pulls_one = pd.read_csv('datasets/pulls_2011-2013.csv')
pulls_two = pd.read_csv('datasets/pulls_2014-2018.csv')
pull_files = pd.read_csv('datasets/pull_files.csv') 

# Append pulls_one to pulls_two
pulls = pulls_one.append(pulls_two, ignore_index = True)
pulls['date'] = pd.to_datetime(pulls['date'], utc= True)

# Merge the two DataFrames
data = pulls.merge(pull_files, on = 'pid')

# Create a column that will store the month
data['month'] = data['date'].dt.month
data['year'] = data['date'].dt.year

# Group by the month and year and count the pull requests
counts = data.groupby(['year', 'month'])['pid'].count()
counts.plot(kind='bar', figsize = (12,4))

# Required for matplotlib
%matplotlib inline

# Group by the submitter
by_user = data.groupby('user').agg({'pid': 'count'})
by_user.hist()

# Identify the last 10 pull requests
last_10 = pulls.sort_values(by = 'date').tail(10)

joined_pr = pull_files.merge(last_10, on = 'pid')
files = set(joined_pr['file'])
print(files)

# This is the file we are interested in:
file = 'src/compiler/scala/reflect/reify/phases/Calculate.scala'

file_pr = data[data['file'] == file]
author_counts = file_pr.groupby('user').count()
print(author_counts.nlargest(3, 'file'))

file = 'src/compiler/scala/reflect/reify/phases/Calculate.scala'

# Select the pull requests that changed the target file
file_pr = pull_files[pull_files['file'] == file]

# Merge the obtained results with the pulls DataFrame
joined_pr = pulls.merge(file_pr, on ='pid')

# Find the users of the last 10 most recent pull requests
users_last_10 = set(joined_pr.nlargest(10,'date')['user'])
print(users_last_10)


%matplotlib inline
# The developers we are interested in
authors = ['xeno-by', 'soc']

# Get all the developers' pull requests
by_author = pulls[pulls['user'].isin(authors)]
counts = by_author.groupby([by_author['user'], by_author['date'].dt.year]).agg({'pid': 'count'}).reset_index()

# Convert the table to a wide format
counts_wide = counts.pivot_table(index='date', columns='user', values='pid', fill_value=0)
counts_wide.plot(kind='bar')