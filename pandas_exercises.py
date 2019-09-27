import numpy as np
import pandas as pd

from pydataset import data

## Exercise 1
# On average, which manufacturer has the best miles per gallon?
# How many different manufacturers are there?
# How many different models are there?
# Do automatic or manual cars have better miles per gallon?

mpg = data('mpg')

# On average, which manufacturer has the best miles per gallon?
city_and_hwy = mpg.groupby("manufacturer").hwy.agg("max") + mpg.groupby("manufacturer").cty.agg("max")
number_of_manufacturers = len(mpg.manufacturer.unique())
average_mpg = city_and_hwy / 2
best_mpg_manufacturer = average_mpg.idxmax()
best_mpg_manufacturer

# How many different manufacturers are there?
number_of_different_manufacturers = len(mpg.manufacturer.unique())
number_of_different_manufacturers

# How many different models are there?
number_of_different_models = len(mpg.model.unique())
number_of_different_models

# Do automatic or manual cars have better miles per gallon?
mpg["transmission"] = mpg.trans.str.partition("(")[0]
mpg = mpg.drop(columns = ["trans"])
mpg["average_mpg"] = (mpg.cty + mpg.hwy) / 2
mpg
mpg.groupby("transmission").agg(["max"], axis="average_mpg")


mpg_and_transmission_type = mpg[["average_mpg", "transmission"]]
mpg_and_transmission_type.groupby("transmission").mean()
best_mpg_transmission_type = mpg_and_transmission_type.groupby("transmission").mean().idxmax()
best_mpg_transmission_type


## Exercise 2
# Copy the users and roles dataframes from the examples above. 
# What do you think a right join would look like? 
# An outer join? 
# What happens if you drop the foreign keys from the dataframes and try to merge them?
users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})

roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})

right_join = pd.merge(users, roles, left_on="role_id", right_on="id", how="right")
right_join

outer_join = pd.merge(users, roles, left_on="role_id", right_on="id", how="outer")
outer_join

## Exercise 3
# Create a function named get_db_url. It should accept a username, hostname, password, and database name and return a url formatted like in the examples in this lesson.
def get_db_url(user, host, password, database_name):
    url = f'mysql+pymysql://{user}:{password}@{host}/{database_name}'
    return url
    
# Use your function to obtain a connection to the employees database.
from env import host, user, password

employees_db_url = get_db_url(user, host, password, "employees")
query = "select * from employees"
pd.read_sql(query, employees_db_url)

# Once you have successfully run a query:
#     Intentionally make a typo in the database url. What kind of error message do you see?
#     Intentionally make an error in your SQL query. What does the error message look like?

# Read the employees and titles tables into two separate dataframes
query = "SELECT * from employees"
employees = pd.read_sql(query, employees_db_url)

query = "SELECT * FROM titles"
titles = pd.read_sql(query, employees_db_url)

# Visualize the number of employees with each title.
unique_titles = titles.groupby("title").count()

unique_titles.rename(columns={"emp_no": "number_with_title"}, inplace=True)
unique_titles = unique_titles.drop(columns=["from_date", "to_date"])
unique_titles = unique_titles.reset_index()
unique_titles.plot(x ='title', y='number_with_title', kind = 'bar')

# Join the employees and titles dataframes together.
employee_titles = pd.merge(employees, titles, how="inner", left_on="emp_no", right_on="emp_no")
employee_titles.head()

# Visualize how frequently employees change titles.
df = employee_titles.groupby("emp_no").count()
df = df.reset_index()
df = df.rename(columns={"title":"number_of_titles"})
df = df[["number_of_titles", "emp_no"]]
df.head()

df = df.rename(columns={"emp_no":"number_of_employees"})

title_counts = df.groupby("number_of_titles").count()
title_counts = title_counts.reset_index()
title_counts

# This seems to freeze my VSCode right now... 
# df.plot(x ='number_of_titles', y='number_of_employees', kind = 'bar')

# For each title, find the hire date of the employee that was hired most recently with that title.
employee_titles.groupby("title").hire_date.max()

# create a cross tabulation of the number of titles by department. 
# (Hint: this will involve a combination of SQL and python/pandas code)
query = """
    select *
    from departments
    join dept_emp using(dept_no)
    join titles using(emp_no)
    where titles.to_date > now()
    and dept_emp.to_date > now()
"""

df = pd.read_sql(query, employees_db_url)
df.head()

# number of titles per department

number_of_titles_per_dept = pd.crosstab(df.title, df.dept_name)
number_of_titles_per_dept