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
#removal_cols = ['CancellationCode', 'CarrierDelay', 'WeatherDelay', 'NASDelay', 'SecurityDelay', 'LateAircraftDelay']
for key in df_dict.keys():
    df_dict[key] = df_dict[key].dropna(axis=1, how='all')
    df_dict[key] = df_dict[key].fillna(int(0))
    df_ls.append(df_dict[key])

#------------------------------------------------------------------------------------------------------------------------------------------

#%% 
for i in range(7, 9):
    df_ls[i] = df_ls[i].drop(['TailNum', 'AirTime', 'TaxiIn', 'TaxiOut'], axis=1)

# %%converting types for making a master df
# %% converting CRSElapsedTime to int of df_1996
df_ls[-1]['CRSElapsedTime'] = df_ls[-1]['CRSElapsedTime'].astype('int64')
df_ls[-2]['CRSElapsedTime'] = df_ls[-2]['CRSElapsedTime'].astype('int64')
# %% converting Distance to float of df_1996
df_ls[-1]['Distance'] = df_ls[-1]['Distance'].astype('float64')


# %% m2t3 integrate all of the dataframes together into one master dataframe.
master_df = pd.concat(df_ls, ignore_index=True)
# %%
master_df.info()
# -------------------------------------------------------------------------------------------------------

# %% m2t4: export the final master dataframe into one file called combined_data.csv
master_df.to_csv("D:\\AiCore\\final_project\\combined_data.csv", index=False)
# %%
