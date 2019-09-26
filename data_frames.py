""" All the datasets loaded from the pydataset library will be pandas dataframes.

Copy the code from the lesson to create a dataframe full of student grades.

Create a column named passing_english that indicates whether each student has a passing grade in reading.
Sort the english grades by the passing_english column. How are duplicates handled?
Sort the english grades first by passing_english and then by student name. All the students that are failing english should be first, and within the students that are failing english they should be ordered alphabetically. The same should be true for the students passing english. (Hint: you can pass a list to the .sort_values method)
Sort the english grades first by passing_english, and then by the actual english grade, similar to how we did in the last step.
Calculate each students overall grade and add it as a column on the dataframe. The overall grade is the average of the math, english, and reading grades. """

#1a)
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
                   'reading': reading_grades})

df['passing_english'] = df.english > 70
#1b)
df.sort_values(by = 'passing_english')
#1c)
df.sort_values(by = ['passing_english','name'])
#1d)
df.sort_values(by=['passing_english','english'])

df['overall_grade']=df[['math','english','reading']].apply(np.mean,axis=1)


""" 2)Load the mpg dataset. Read the documentation for the dataset and use it for the following questions:

2a)How many rows and columns are there?
2b)What are the data types of each column?
2c)Summarize the dataframe with .info and .describe
2d)Rename the cty column to city.
2e)Rename the hwy column to highway.
2f)Do any cars have better city mileage than highway mileage?
2g)Create a column named mileage_difference this column should contain the difference between highway and city mileage for each car.
2h)Which car (or cars) has the highest mileage difference?
2i)Which compact class car has the lowest highway mileage? The best?
2j)Create a column named average_mileage that is the mean of the city and highway mileage.
2k)Which dodge car has the best average mileage? The worst? """

from pydataset import data
mpg = data('mpg')
#2a)
mpg.shape
#2b,c)
mpg.info()
mpg.describe()
#2d,e)
mpg.rename(columns = {'cty':'city','hwy':'highway'},inplace = True)
#2f)
better_mileage = mpg['city']>mpg['highway']
mpg[better_mileage]
#2g)
mpg['mileage_difference'] = mpg.highway-mpg.city
#2h)
mpg.sort_values(by = 'mileage_difference',ascending=False).head(1)
#2i)
print(mpg[mpg['class'] == 'compact'].sort_values(by='highway',ascending=True).head(1))
print(mpg[mpg['class'] == 'compact'].sort_values(by='highway',ascending=True).tail(1))
#2i)
mpg['average_mileage']=mpg[['highway','city']].apply(np.mean,axis=1)
#2k)
mpg[mpg['manufacturer'] == 'dodge'].sort_values(by='average_mileage',ascending=False).head(1)
mpg[mpg['manufacturer'] == 'dodge'].sort_values(by='average_mileage',ascending=False).tail(1)



""" 3)Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:

3a)How many rows and columns are there?
3b)What are the data types?
3c)Summarize the dataframe with .info and .describe
3d)What is the the weight of the fastest animal?
3e)What is the overall percentage of specials? 
3f)How many animals are hoppers that are above the median speed? What percentage is this? """

mammals=data('Mammals')
mammals.head()
#3a)
mammals.shape
#3b)
mammals.dtypes
#3c)
mammals.info()
mammals.describe()
#3d)
mammals[['weight','speed']].sort_values(by='speed',ascending=False).head(1)
#3e)
sum(mammals.specials==True)/len(mammals)*100
#3f
num_animals=sum((mammals.hoppers == True) & (mammals.speed > mammals.speed.median()))
print(num_animals)
print(round(num_animals/len(mammals)*100,2))
