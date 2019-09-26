import pandas as pd
from env import host, user, password

database_name = "sakila"

url = f'mysql+pymysql://{user}:{password}@{host}/{database_name}'

query = """SELECT * FROM actor"""

df = pd.read_sql(query, url)

print(df)
