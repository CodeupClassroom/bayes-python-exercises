
import pandas as pd
import numpy as np

np.random.seed(123)

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

df.head()


# In[5]:


pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})


# In[6]:


pd.DataFrame([[1, 2, 3], [4, 5, 6]])


# In[7]:


data = np.array([[1, 2, 3], [4, 5, 6]])

pd.DataFrame(data, columns=['a', 'b', 'c'])




# we can build up a DataFrame
# and assign collections like arrays or lists

df = pd.DataFrame()
df["students"] = ['Sally',  'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']
df["math_grades"] = np.random.randint(low=60, high=100, size=len(students))
df["english_grades"] = np.random.randint(low=60, high=100, size=len(students))
df["letter_grades"] = ["C", "B", "B", "B", "C", "C", "D", "C", "C", "B", "C", "C"]
df







