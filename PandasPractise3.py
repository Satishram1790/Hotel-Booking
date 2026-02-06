# Import Pandas
import pandas as pd

# Read the file
Hotel_booking=pd.read_csv('hotel_bookings_messy.csv')
pd.set_option('display.max_row',None)

# print(Hotel_booking.head()) # read the top 5 data in the file

# read the columns
# print(Hotel_booking.columns) 

# drop the unnamed column(s)
# Hotel_booking.drop(columns=['Unnamed: 0'],inplace=True)

# rename the column(S) with the same dataframe
Hotel_booking.rename({'adults':'No of adults', 'children':'No of childs','babies':'No of babies'},axis=1,inplace=True)

# Check for NaN value by percentage
Hotel_booking.isnull().sum()*100/len(Hotel_booking)
# print(Hotel_booking.isnull().sum()*100/len(Hotel_booking))

# check for unique value to fill for NaN value which has low percentage instead of droppping
Hotel_booking['agent'].unique()
# check for any specific value, parallel attributes are same any commonality? or not
Hotel_booking[Hotel_booking['agent']==5]

# since not find the unique value/ numeric data, filling the NaN as -1 (placeholder)
Hotel_booking.fillna({'agent':-1},inplace=True)

# check for the NaN for specific column with the parrallel columns
Hotel_booking[Hotel_booking['No of childs'].isna()]

# check for the NaN for specific column with the parrallel specific columns
Hotel_booking[Hotel_booking['country'].isna()][['No of adults','No of childs','No of babies','country']]

# Filling the NaN as 'unknown' for specific column

Hotel_booking.fillna({'country':'unknow'},inplace=True)

# drop the NaN of specific columns, sub columns
Hotel_booking.dropna(subset=['No of childs'],inplace=True)

# drop the specific column since has a more null percentage
Hotel_booking.drop(columns=['company'],inplace=True)

# Again check for NaN percentage
# print(Hotel_booking.isnull().sum()*100/len(Hotel_booking))

# check the data types are good?
# print(Hotel_booking.dtypes)

# changes the dtype for the columns
Hotel_booking=Hotel_booking.astype({'is_canceled':'boolean','is_repeated_guest':'boolean','No of childs':'int'})
# print(Hotel_booking.dtypes)

# now find the unique value for a specific column,- has more number of uniques
Hotel_booking['lead_time'].unique()
# print(Hotel_booking['lead_time'].unique())

# since more number of uniques, check desc to find mean,min,max, std and count etc
Hotel_booking['lead_time'].describe()
# print(Hotel_booking['lead_time'].describe())

# To avoid small vibrations, define the bins and labels for grouping
bins=[0,100,200,300,400,500,600,700,800]
labels=['0-100','101-200','201-300','301-400','401-500','501-600','601-700','701-800']
Hotel_booking['lead_time_binned']=pd.cut(Hotel_booking['lead_time'],bins=bins,labels=labels)
Hotel_booking[['lead_time','lead_time_binned']]
# print(Hotel_booking[['lead_time','lead_time_binned']])


# split the column as new year and month columns
Hotel_booking['arrival_year']=Hotel_booking['arrival_date'].str.split('-',expand=True)[0]
Hotel_booking['arrival_month']=Hotel_booking['arrival_date'].str.split('-',expand=True)[1]

# since createed column will reflect in same dataframe, stored the values in new variable by pop/ remove
move_year_column=Hotel_booking.pop('arrival_year')
move_month_column=Hotel_booking.pop('arrival_month')

# insert the stored data by index number

Hotel_booking.insert(4,'arrival_year',move_year_column)
Hotel_booking.insert(5,'arrival_month',move_month_column)

# now drop the old splited column
Hotel_booking.drop(columns=['arrival_date'],inplace=True)
# print(Hotel_booking.head())

# string cleaning
# check for a special characters  - like @#$%^&*\/!| etc
Hotel_booking['hotel'].unique()

# function know this expresion are regex
Hotel_booking['hotel']=Hotel_booking['hotel'].replace(r"[\*\\\n\@\#\$\%\^\&]",'',regex=True)
# print(Hotel_booking['hotel'].unique())

# check for dulipcates
Hotel_booking.loc[Hotel_booking.duplicated(keep=False)]
# print(Hotel_booking.loc[Hotel_booking.duplicated(keep=False)])

# drop the duplicates, expect the first instance
Hotel_booking.drop_duplicates(keep='first',inplace=True)
# print(Hotel_booking.drop_duplicates(keep='first',inplace=True))


print(Hotel_booking.isnull().sum()*100/len(Hotel_booking))
