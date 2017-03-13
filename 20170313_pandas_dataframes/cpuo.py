import pandas as pd


df = pd.read_csv('cpuo.csv')


# Filter Pandas Dataframe rows by exact match?
# print ("Entire Dataframe: \n", df)

# Filter Pandas Dataframe rows by exact match?
print (df[df['Precinct / Command'].str.contains("Transit")])


# print ( df.str.match('Transit', axis=0 ) )



























'''

# How many rows are in the DataFrame?
print "Rows in Dataframe: ", len(df.index)

# What columns are included in the DataFrame?
print "\nList of Columns:\n", list(df.columns.values)


# Which NYC police precinct received the most complaints in a single year?
print "\nPrecinct w/most complaints in a year:\n", df[['Precinct / Command', 'Complaints Count']].max()


# What is the average number of complaints against a police precinct in a year?
years = [2009, 2010, 2011]
df_2009 = df[df['Year'] == years[0]]
df_2010 = df[df['Year'] == years[1]]
df_2011 = df[df['Year'] == years[2]]
print "\nAverage Complaints in 2009: ", df_2009['Complaints Count'].mean()
print "Average Complaints in 2010: ", df_2010['Complaints Count'].mean()
print "Average Complaints in 2011: ", df_2011['Complaints Count'].mean()


# What is the standard deviation from that average?
print "\nStandard Deviation (2009): ", df_2009['Complaints Count'].std()
print "Standard Deviation (2010): ", df_2010['Complaints Count'].std()
print "Standard Deviation (2011): ", df_2011['Complaints Count'].std()


# What is the total complaints count, and the total number of officers subject to complaint?
print "\nTotal complaints: ", df['Complaints Count'].sum()
print "Total officers subject to complaint: ", df['Number Of Subject Officers'].sum()


# What command, in what year, receieved zero complaints?
zero = df.loc[df['Complaints Count'] == 0]
print "\nYear & Command with zero complaints:\n", zero[['Year', 'Precinct / Command']]


# What is the command to insert your DataFrame into a SQLite database?
conn = sqlite3.connect("police.db") #possibly put at top
#(table_name, connect)
df.to_sql("police", conn)

'''


