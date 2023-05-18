#%% import modules
import pandas as pd
import os
import numpy as np
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
df_dict_copy = df_dict.copy()
#---------------------------------------------------------------------------------------------------------------------------
# %% m2t2 print the number of records that contain NULL values in any of their columns using Panda's isnull() and isna() functions.
for key in df_dict_copy.keys():
    num_of_null_record = df_dict_copy[key].isnull().any(axis=1).sum()
    print("Number of null records in " + key + " is: " + str(num_of_null_record))

# %% dropping columns and putting the dfs into a list
df_ls = []
removal_cols = ['CancellationCode', 'CarrierDelay', 'WeatherDelay', 'NASDelay', 'SecurityDelay', 'LateAircraftDelay']
for key in df_dict_copy.keys():
    columns_b4 = df_dict_copy[key].columns.tolist()
    print("in " + key + "b4 dropping : " + str(len(columns_b4)))
    df_dict_copy[key] = df_dict_copy[key].drop(removal_cols, axis=1)
    columns_aft = df_dict_copy[key].columns.tolist()
    print("in " + key + "aftr dropping : " + str(len(columns_aft)))
    df_dict_copy[key] = df_dict_copy[key].fillna(int(0))
    df_ls.append(df_dict_copy[key])

#------------------------------------------------------------------------------------------------------------------------------------------
#converting types for making a master df
#%% converting TailNum to object
for i in range(0, 7):
    df_ls[i]['TailNum'] = df_ls[i]['TailNum'].astype(object)
# %% converting CRSElapsedTime to int of df_1996
df_ls[-1]['CRSElapsedTime'] = df_ls[-1]['CRSElapsedTime'].astype('int64')
df_ls[-2]['CRSElapsedTime'] = df_ls[-2]['CRSElapsedTime'].astype('int64')
# %% converting Distance to float of df_1996
df_ls[-1]['Distance'] = df_ls[-1]['Distance'].astype('float64')

# %% converting TaxiIn to int
for i in range(0,7):
    df_ls[i]['TaxiIn'] = df_ls[i]['TaxiIn'].astype('int64')

# %% converting TaxiOut to int
for i in range(0,7):
    df_ls[i]['TaxiOut'] = df_ls[i]['TaxiOut'].astype('int64')

# %% m2t3 integrate all of the dataframes together into one master dataframe.
master_df = pd.concat(df_ls, ignore_index=True)
# %%
master_df.info()
# -------------------------------------------------------------------------------------------------------

# %% m2t4: export the final master dataframe into one file called combined_data.csv
master_df.to_csv("D:\\AiCore\\final_project\\combined_data.csv", index=False)