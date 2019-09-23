import json

with open('profiles.json') as f:
    profiles = json.load(f)

###

active_users = [profile for profile in profiles if profile['isActive']]
n_active_users = len(active_users)

###

inactive_users = [profile for profile in profiles if not profile['isActive']]
n_inactive_users = len(inactive_users)

###

def handle_balance(s):
    return float(s[1:].replace(',', ''))

balances = [handle_balance(profile['balance']) for profile in profiles]
total_balance = sum(balances)
average_balance = sum(balances) / len(balances)

###

user_with_the_lowest_balance
user_with_the_lowest_balance = profiles[0]
for user in profiles[1:]:
    if handle_balance(user['balance']) < handle_balance(user_with_the_lowest_balance['balance']):
        user_with_the_lowest_balance = user

###

user_with_the_highest_balance = profiles[0]
for user in profiles[1:]:
    if handle_balance(user['balance']) > handle_balance(user_with_the_highest_balance['balance']):
        user_with_the_highest_balance = user

user_with_the_highest_balance

### Alternative with a custom key function

min(profiles, key=lambda profile: handle_balance(profile['balance']))
def extract_balance(profile):
    return handle_balance(profile['balance'])
min(profiles, key=extract_balance)

###

from collections import Counter
Counter([p['favoriteFruit'] for p in profiles])

fruit_counts = {}
for profile in profiles:
    fruit = profile['favoriteFruit']
    if fruit in fruit_counts:
        fruit_counts[fruit] += 1
    else:
        fruit_counts[fruit] = 1

###

greetings = [profile['greeting'] for profile in profiles]
def extract_digits(s):
    return int(''.join([c for c in s if c.isdigit()]))
n_unread_messages = [extract_digits(greeting) for greeting in greetings]
sum(n_unread_messages)

