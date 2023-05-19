#%% import modules
import pandas as pd
import os
### m2t1: load the CSV datafiles into Pandas dataframes
# list dirs
csvs = [x for x in os.listdir("D:\\AiCore\\final_project\\data-analytics-files\\")]
# give file names
fnames = ["df_"+os.path.splitext(os.path.basename(csv))[0] for csv in csvs]
# make a df_dict
df_dict = {}
# load each file from the directory as df into the values for each corresponding fname keys
for i in range(len(fnames)):
    df_dict[fnames[i]] = pd.read_csv("D:\\AiCore\\final_project\\data-analytics-files\\" + csvs[i])
#---------------------------------------------------------------------------------------------------------------------------
#%% make a copy to work with for the next tasks
# df_dict = df_dict.copy()
#---------------------------------------------------------------------------------------------------------------------------
# %% m2t2 print the number of records that contain NULL values in any of their columns using Panda's isnull() and isna() functions.
for key in df_dict.keys():
    num_of_null_record = df_dict[key].isnull().any(axis=1).sum()
    print("Number of null records in " + key + " is: " + str(num_of_null_record))

# %% dropping columns and putting the dfs into a list
df_ls = []
removal_cols = ['CancellationCode', 'CarrierDelay', 'WeatherDelay', 'NASDelay', 'SecurityDelay', 'LateAircraftDelay']
for key in df_dict.keys():
    df_dict[key] = df_dict[key].drop(removal_cols, axis=1)
    df_dict[key] = df_dict[key].fillna(int(0))
    df_ls.append(df_dict[key])

#------------------------------------------------------------------------------------------------------------------------------------------

#%% 
#for i in range(7, 9):
#    master_df = master_df.drop(['TailNum', 'AirTime', 'TaxiIn', 'TaxiOut'], axis=1)
# %%
for i in range(len(df_ls)):
    df_ls[i]['CRSElapsedTime'] = df_ls[i]['CRSElapsedTime'].astype('int16')
#%%
for i in range(len(df_ls)):
    df_ls[i]['Distance'] = df_ls[i]['Distance'].astype('float16')
#%%
for i in range(len(df_ls)):
    df_ls[i]['TaxiOut'] = df_ls[i]['TaxiOut'].astype('int16')
    df_ls[i]['TaxiIn'] = df_ls[i]['TaxiIn'].astype('int16')

#%%
for i in range(0,7):
    df_ls[i]['TailNum'] = df_ls[i]['TailNum'].astype(object)

# %% m2t3 integrate all of the dataframes together into one master dataframe.
master_df = pd.concat(df_ls, ignore_index=True)

# %%converting types for making a master df

master_df['Year'] = master_df['Year'].astype('int16')
master_df['Month'] = master_df['Month'].astype('int8')
master_df['DayofMonth'] = master_df['DayofMonth'].astype('int8')
master_df['DayOfWeek'] = master_df['DayOfWeek'].astype('int8')


#%%
master_df['DepTime'] = master_df['DepTime'].astype('int16') 
master_df['CRSDepTime'] = master_df['CRSDepTime'].astype('int16')
master_df['ArrTime'] = master_df['ArrTime'].astype('int16')
master_df['CRSArrTime'] = master_df['CRSArrTime'].astype('int16')
master_df['FlightNum'] = master_df['FlightNum'].astype('int16')
master_df['ActualElapsedTime'] = master_df['ActualElapsedTime'].astype('int16')
master_df['CRSElapsedTime'] = master_df['CRSElapsedTime'].astype('int16')
master_df['Distance'] = master_df['Distance'].astype('float32')
master_df['ArrDelay'] = master_df['ArrDelay'].astype('int16')
master_df['DepDelay'] = master_df['DepDelay'].astype('int16')
master_df['Cancelled'] = master_df['Cancelled'].astype('int8')
master_df['Diverted'] = master_df['Diverted'].astype('int8')


#%%
master_df['AirTime'] = master_df['AirTime'].astype('int16')

# %%
master_df['UniqueCarrier'] = master_df['UniqueCarrier'].astype('category')

#%%
master_df['Origin'] = master_df['Origin'].astype('category')


#%%
master_df['Dest'] = master_df['Dest'].astype('category')


#%%
master_df['Distance'] = master_df['Distance'].astype('float16') 
#%%
master_df.info()

# -------------------------------------------------------------------------------------------------------

# %% m2t4: export the final master dataframe into one file called combined_data.csv
master_df.to_csv("D:\\AiCore\\final_project\\combined_data.csv", index=False)
# %%
