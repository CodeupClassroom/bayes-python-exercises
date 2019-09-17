def keep_long_words(words):
    '''
    >>> keep_long_words(['ls', 'codeup', 'code', 'pip', 'bayes'])
    ['codeup', 'bayes']
    >>> keep_long_words(['cd', 'ls', 'pwd'])
    []
    >>> keep_long_words(['python', 'algorithm'])
    ['python', 'algorithm']
    '''
    long_words = []
    # loop through the words list
    for word in words:
    # check if each word is longer than 4 chars
        if len(word) > 4:
            # if it is, add it to a new list
            long_words.append(word)
    # return the list of long words
    return long_words

def make_model(cars):
    '''
    >>> cars = []
    >>> cars.append({'make': 'Toyota', 'model': 'Camry'})
    >>> cars.append({'make': 'Honda', 'model': 'Accord'})
    >>> cars.append({'make': 'Ford', 'model': 'Fiesta'})
    >>> cars.append({'make': 'Ford', 'model': 'F-150'})
    >>> make_model(cars)
    ['Toyota Camry', 'Honda Accord', 'Ford Fiesta', 'Ford F-150']
    '''
    makes_and_models = []
    for car in cars:
        makes_and_models.append(car['make'] + ' ' + car['model'])
    return makes_and_models

def extract_time_components(s):
    '''
    >>> extract_time_components('21:30:00')
    {'hours': 21, 'minutes': 30, 'seconds': 0}
    >>> extract_time_components('09:01:53')
    {'hours': 9, 'minutes': 1, 'seconds': 53}
    '''
    parts = s.split(':')
    hours = parts[0]
    minutes = parts[1]
    seconds = parts[2]

    time_dict = {}
    time_dict['hours'] = int(hours)
    time_dict['minutes'] = int(minutes)
    time_dict['seconds'] = int(seconds)

    return time_dict