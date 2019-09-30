import pandas as pd
from pydataset import data

mpg = data("mpg")
mpg.head()

# .loc and .iloc
mpg.iloc[0]

# .iloc's slice range is exclusive of the end
mpg.iloc[0:4]

# .loc
# [rows, columns]
mpg.loc[:, "model":"trans"].head()

# pipe method
# .pipe is a method that takes in a function definion
# .pipe works on the dataframe and the funciton must return a dataframe
def mpg_avg(df):
    df["average_mpg"] = (df.cty + df.hwy) / 2
    return df

def rename_columns(df):
    df = df.rename(columns={"trans":"transmission", "displ": "displacement"})
    return df

# working from the left to the right
df = mpg.pipe(mpg_avg).pipe(rename_columns)

# working from the inside out
mpg_avg(rename_columns(mpg))

