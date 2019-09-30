import pandas as pd 

fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])

fruits.describe()

#  Run the code necessary to produce only the unique fruit names.
fruits.unique()

# Determine how many times each value occurs in the series.
frequencies = fruits.value_counts()
frequencies

# Determine the most frequently occurring fruit name from the series.
most_frequent = frequencies.max() 
fruit = frequencies.idxmax()
print("Most frequently occuring fruit is", fruit, "and it shows up", most_frequent, "times" )

# Determine the least frequently occurring fruit name from the series.
least_frequent = fruits.value_counts().min() # min gives us back the lowest value

# fruits.value_counts()[fruits.value_counts() == least_frequent] is the same as below
# indexing and subsetting 
frequencies = fruits.value_counts()
frequencies[frequencies == least_frequent]

# Write the code to get the longest string from the fruits series.
fruit_names = fruits.unique()
fruit_names = pd.Series(fruit_names)
length_of_longest_string = fruit_names.str.len().max() # the length of the longest string
index_of_longest_string = fruit_names.str.len().idxmax() # the index of the longest string
longest_string = fruit_names[index_of_longest_string]

print("The longest string in the list of fruits is", longest_string, "and it has", length_of_longest_string, "letters")

# another approach to handle multiple longest strings
length_of_longest_string = fruit_names.str.len().max() # the length of the longest string
length_of_longest_string
fruit_names[fruit_names.str.len() == length_of_longest_string]

# Find the fruit(s) with 5 or more letters in the name.
more_than_five_letters = fruits.apply(lambda x: len(x) >= 5)
fruits[more_than_five_letters]

# nice and short
fruits[fruits.str.len() > 5]

# Capitalize all the fruit strings in the series.
fruits.str.capitalize()

# Count the letter "a" in all the fruits (use string vectorization)
counts_of_a = fruit_names.str.count("a")
counts_of_a
fruit_names
counts_of_a

list(zip(fruit_names, counts_of_a))

# another approach to output 2 series 
for i, fruit in enumerate(fruit_names):
    print(fruit, "has", counts_of_a[i], " number of 'a' characters.")


df = pd.DataFrame(list(zip(fruit_names, counts_of_a)))
df.columns = ["fruit_name", "count_of_a"]
df


# Use the .apply method and a lambda function to fin d the fruit(s) containing two or more "o" letters in the name.
with_two_or_more_o = fruit_names.apply(lambda x: x.count("o") >= 2)
fruit_names[with_two_or_more_o]

# Same operation using indexing and subsetting (instead of .apply and lambda)
fruits[fruits.str.count("o") >= 2]

# Write the code to get only the fruits containing "berry" in the name
contains_berry = fruits.apply(lambda x: "berry" in x)
fruits[contains_berry]

# or we can use .str.contains
fruits[fruits.str.contains("berry")]

# Write the code to get only the fruits containing "apple" in the name
contains_apple = fruits.str.contains("apple")
fruits[contains_apple]

# Which fruit has the highest amount of vowels?
# get the highest vowel count first
id_of_max = fruits.apply(count_vowels).idxmax() # gives us the index value of the highest vowel count
fruits[id_of_max]