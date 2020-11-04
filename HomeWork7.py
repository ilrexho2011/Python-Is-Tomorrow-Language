
                    # HomeWork #7: Dictionaries and Sets

'''
Refactor the code from first assignment so every variable and its corresponding value
become key value pairs in a dictionary. then loop through each item in the dictionary
to print out the key and value

Extra bonus: Create a function that allows someone to guess the value of any key in the dictionary,
and find out if they were right or wrong. This function should accept two parameters: Key and Value.
If the key exists in the dictionary and that value is the correct value, then the function should return True.
Otherwise, it should return False
'''

myFavoriteSong = {
    'title': 'The day before you came',
    'released': (1986, 10, 12),
    'year recorded': 1985,
    'author': 'ABBA',
    'album': 'Waterloo',
    'recorder': 'BMG',
    'genre': 'Pop',
    'labels': ['ABA Records', 'Sony'],
    'producer': 'Fa Studios',
    'text writers': ['Björn Ulvaeus', 'Benny Andersson', 'Agnetha Fältskog', 'Anni-Frid Lyngstad', 'Lasse Berghagen'],
    'effect studios': {'Stockholm': 'Viking Studios', 'Göttenbörg': 'EMI Recording Studios'},
    'lengths in min': {'album': 5.46, 'disco edit': 4.37, 'radio': 5.46}
}

# print values which are strings, numbers or tuples:
[print(f"* {k.title()}: {v}") for k, v in myFavoriteSong.items() if isinstance(v, (str, int, tuple))]

# print values that are lists or dictionaries
[print(f"* {k.title()}: {(', '.join(v)).title()}") for k, v in myFavoriteSong.items() if isinstance(v, (list, dict))]


# ***************************    Part extra   ************************************

def review_guesses(topic, guess):
    if myFavoriteSong.get(topic.lower()):
        your_entry = myFavoriteSong[topic.lower()]

        if isinstance(your_entry, dict):
            if guess in str(your_entry.values()):
                return True
            else:
                return False
        elif isinstance(your_entry, (int, str)):
            if guess.title() == str(your_entry):
                return True
            else:
                return False
        elif isinstance(your_entry, (list, tuple)) and guess.title() in str(your_entry):
            return True
        else:
            return False       
    else:
        print('The topic is not supported for my favorite song.')

print(review_guesses(input('Enter your topic: '), input('Enter your guess: ')))












