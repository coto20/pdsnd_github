
# Display a Breakdown of User Types

#There are different types of users specified in the 
#"User Type" column. Find how many there are of each 
#type and store the counts in a pandas Series in the 
#user_types variable. Hint: What pandas function returns 
#a Series with the counts of each unique value in a column?


import pandas as pd

file_name = 'chicago.csv'

# load data file into a dataframe
df = pd.read_csv(file_name)

# print value counts for each user type
user_types = df['User Type'].value_counts()

print(user_types)
