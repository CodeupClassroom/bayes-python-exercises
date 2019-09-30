import pandas as pd
import numpy as np
from env import host, user, password


students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades,
                   'classroom': np.random.choice(['A', 'B'], len(students))})

# btw .T transposes dataframes
df.groupby("classroom").describe()

df.groupby("classroom").min()
df.groupby("classroom").agg("min")

df.groupby("classroom").max()
df.groupby("classroom").agg("max")

df.groupby("classroom").idxmax()

df.groupby("classroom").agg(["min", "max", "mean", "count"])
df.groupby("classroom").agg(["min", "max", "mean", "count"]).T

df.groupby("classroom").agg(["std"])

classroom_counts = df.groupby("classroom").agg("count")

# Join employees and salaries from their respective queries
# make a dataframe from select * from employees
# make another dataframe from select * from salaries
database_name = "employees"
url = f'mysql+pymysql://{user}:{password}@{host}/{database_name}'

employees_query = "SELECT * from employees"
employees = pd.read_sql(employees_query, url)
employees.head()

salaries_query = "SELECT * from salaries where to_date > now()"
salaries = pd.read_sql(salaries_query, url)
salaries.head()

# .merge is panda's join 
# .merge defaults to an inner join
# .join default to a left join
# pd.merge(employees, salaries) also works
employee_salaries = pd.merge(employees, salaries, left_on="emp_no", right_on="emp_no", how="inner")
type(employee_salaries)

employee_salaries.head()
