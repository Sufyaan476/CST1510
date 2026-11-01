"""
RECORD CHECK  -  my version
===========================

Name  :  Nunkoo Sufyaan
Lane  :  AI 
Date  :  30/10/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd

# ==================================================================== LOAD
# 1. Read your data file with pd.read_csv(). Make your own CSV, header row
#    plus at least 5 data rows: label,value,limit (or your lane's own field
#    names - same shape, different words).


# creating my own CSV file called 'my_file.csv' and populating it with my own data
with open("my_file.csv", "w") as f:
    f.write(f"dataset_name,rows_loaded,rows_expected\n")
    f.write(f"survey-2017,872,1981\n")
    f.write(f"survey-2019,120,9839\n")
    f.write(f"survey-2020,932,22\n")
    f.write(f"survey-2021,283,23\n")
    f.write(f"survey-2023,3923,31445\n")
    f.write(f"survey-2024,987,1050")

# loading data from 'my_file.csv' into a dataframe
df = pd.read_csv("my_file.csv")


# ================================================================= PROCESS
# 2. Add a "percent" column: (value / limit) * 100.
#
#    Typical and above: also add a "status" column using .apply() with a
#    lambda - "OVER LIMIT" (100%+), "WARNING" (90%+), otherwise "OK".

# new column percent is 'added'
df["percent"] = (df["rows_loaded"]/df["rows_expected"])*100

# new column 'status' is added
df["status"] = df["percent"].apply(lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK")
                                  

# ================================================================== OUTPUT
# 3. Print the DataFrame.
#
#    Threshold : print it as-is, with the percent column.
#    Typical   : also filter to show only the rows that are not "OK", using a
#                boolean condition in [] - not a loop.
#    Excellent : also group by "status" and print a count per group, save
#                the full DataFrame to a new CSV with .to_csv(), and save
#                one bar chart of the counts per status.


print("THE NEW DATAFRAME")
print(df)

# 'not_ok' is a dataframe that holds the rows that do not have "OK" status
not_ok = df[df["status"] != "OK"]
print("")
print("THE ROWS THAT DO NOT HAVE 'OK' STATUS")
print(not_ok)


# 'grouped' is a dataframe that is grouped by status 
grouped = df.groupby("status")

# 'new_grouped' keeps count of the number of occurences of each group
new_grouped = grouped["status"].value_counts()
print("")
print("NUMBER OF OCCURENCES OF EACH GROUP")
print(new_grouped)

# the new dataframe is saved to a new csv file named 'new_file.csv'
df.to_csv("new_file.csv", index= False)


# a bar chart that shows status against count
import matplotlib.pyplot as plt
df["status"].value_counts().plot(kind="bar")
plt.title("STATUS")
plt.savefig("status_count.png")
plt.show()


# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case
