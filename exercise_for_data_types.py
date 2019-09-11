# Exercise 1
# The little mermaid (for 3 days), 
# Brother Bear (for 5 days, they love it), 
# and Hercules (1 day, you don't know yet if they're going to like it). 
# If price for a movie per day is 3 dollars, how much will you have to pay?
price_per_day = 3

brother_bear_days = 5
little_mermaid_days = 3
hercules_days = 1

brother_bear_cost = price_per_day * brother_bear_days
little_mermaid_cost = price_per_day * little_mermaid_days
hercules_cost = price_per_day * hercules_days

total_cost = brother_bear_cost + little_mermaid_cost + hercules_cost


# Exercise 2
# Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. 
# Google pays 400 dollars per hour, Amazon 380, and Facebook 350. 
# How much will you receive in payment for this week? 
# You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.
google_rate = 400
amazon_rate = 380
facebook_rate = 350
facebook_hours = 10
google_hours = 6
amazon_hours = 4
total = amazon_hours*amazon_rate + google_hours*google_rate + facebook_hours*facebook_rate

# Exercise 3
# A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.
class_has_space = False
schedule_works = True

# short-circuit behavior with a sequence of ands. we return false on the very first False
# short-circuit behavior with a sequence of ors: we return true on the first true
student_can_be_enrolled = class_has_space and schedule_works


# Exercise 4
# A product offer can be applied only if people buys more than 2 items, and the offer has not expired. 
# Premium members do not need to buy a specific amount of products.
is_premium_member = True
person_bought_more_than_two_items = False
offer_has_not_expired = False

offer_can_be_applies = offer_has_not_expired and (person_bought_more_than_two_items or is_premium_member)



# Exercise 5
# Use the following code to follow the instructions below:
# Create a variable that holds a boolean value for each of the following conditions:
#     the password must be at least 5 characters
#     the username must be no more than 20 characters
#     the password must not be the same as the username
#     bonus neither the username or password can start or end with whitespace

username = 'codeup'
password = 'notastrongpassword'

password_at_least_five_characters = len(password) >= 5
username_has_less_than_twenty_characters = len(username) <= 20
password_and_username_different = username != password

username_starts_or_ends_with_whitespace = username[0] == " " or username[-1] == " "
password_starts_or_ends_with_whitespace = password[0] == " " or password[-1] == " "
any_credential_starts_or_ends_with_whitespace = username_starts_or_ends_with_whitespace or password_starts_or_ends_with_whitespace

