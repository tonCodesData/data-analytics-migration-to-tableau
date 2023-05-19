#%%
import pandas as pd
fdf = pd.read_csv("D:\\AiCore\\final_project\\combined_data.csv")
# %%
fdf.info()
# %%
fdf['Year'] = fdf['Year'].astype('int16')
#%%
fdf['Month'] = fdf['Month'].astype('int8')
#%%
fdf['DayofMonth'] = fdf['DayofMonth'].astype('int8')
#%%
fdf['DayOfWeek'] = fdf['DayOfWeek'].astype('int8')
# %%
fdf['DepTime'] = fdf['DepTime'].astype('unit16') 

# %%
fdf['CRSDepTime'] = fdf['CRSDepTime'].astype('uint16')
fdf['ArrTime'] = fdf['ArrTime'].astype('uint16')
fdf['CRSArrTime'] = fdf['CRSArrTime'].astype('uint16')
fdf['CRSElapsedTime'] = fdf['CRSElapsedTime'].astype('uint16')
# %%
fdf['ActualElapsedTime'] = fdf['ActualElapsedTime'].astype('int16')
 # %%
fdf['ArrDelay'] = fdf['ArrDelay'].astype('int16')
fdf['DepDelay'] = fdf['DepDelay'].astype('int16')

# %%
fdf['Cancelled'] = fdf['Cancelled'].astype('int8')

# %%
fdf['Diverted'] = fdf['Diverted'].astype('int8')