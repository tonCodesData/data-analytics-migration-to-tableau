cols_94 = df_ls[-3].columns.tolist()
print(cols_94)
cols_95 = df_ls[-2].columns.tolist()
print(cols_95)
add_col_ls = [x for x in cols_95 if x not in cols_94]
print(add_col_ls)


#%% 
for i in range(len(cols_95)):
    print(cols_95[i], i)

add_col_dict = {'TailNum':10, 'AirTime':13, 'TaxiIn':19, 'TaxiOut':20}
#%%
for i in range(0,7):
    df_ls[i].insert(10, 'TailNum', 'int8'(0))
    df_ls[i].insert(13, 'AirTime', 'int8'(0))
    df_ls[i].insert(19, 'TaxiIn', 'int8'(0))
    df_ls[i].insert(20, 'TaxiOut', 'int8'(0))



# %% converting TaxiIn to int
for i in range(0,7):
    df_ls[i]['TaxiIn'] = df_ls[i]['TaxiIn'].astype('int64')

# %% converting TaxiOut to int
for i in range(0,7):
    df_ls[i]['TaxiOut'] = df_ls[i]['TaxiOut'].astype('int64')

#%% converting TailNum to object
for i in range(0, 7):
    df_ls[i]['TailNum'] = df_ls[i]['TailNum'].astype(object)