"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Radek Marval
email: marvalradek@seznam.cz
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

users = {
    "bob": "123",
    "ann": "pass123", 
    "mike": "password123", 
    "liz": "pass123"
}

line = ("-" * 40)

username = input("Enter username: ")
password = input("Enter password: ")

if username.lower() in users and users[username] == password:
    print(line)
    print(f"Welcome to the app, {username}")
    
else:
    print(line)
    print("unregistered user, terminating the program..")
    print(line)
    exit()

print("We have 3 texts to be analyzed.")
print(line)
text_selection = input("Enter a number btw. 1 and 3 to select: ")
print(line)

words = 0
titlecase_words = 0
uppercase_words = 0
lowercase_words = 0
numeric_words = 0
sum_numbers = 0

if text_selection.isdigit():
    if int(text_selection) in (1,2,3):
        for word in TEXTS[int(text_selection)-1].split():
            words += 1
            if word.istitle() and word.isalpha():
                titlecase_words += 1
            if word.isupper() and word.isalpha():
                uppercase_words += 1
            if word.islower() and word.isalpha():
                lowercase_words += 1
            if word.isnumeric():
                numeric_words += 1
                sum_numbers += int(word)
    else:
        print("Enter a number from 1 to 3!")
        exit()
else:
    print("Invalid value! Enter a number from 1 to 3!") 
    exit()

print(f"""
There are {words} words in the selected text.
There are {titlecase_words} titlecase words.
There are {uppercase_words} uppercase words.
There are {lowercase_words} lowercase words.
There are {numeric_words} numeric strings.
The sum of all the numbers is {sum_numbers}.
""".strip())

word_groups = {}

for word_2 in TEXTS[int(text_selection)-1].split():
    without_punctuation = ""
    for letter in word_2:
        if letter.isalnum():
            without_punctuation += letter
    
    sum_letters = len(without_punctuation)
    if sum_letters > 0:
        if sum_letters not in word_groups:
            word_groups[sum_letters] = 1
        else:
            word_groups[sum_letters] += 1

print(f"""
{line}
{"LEN|":<5} {"OCCURENCES":^5} {"|NR.":>5}
{line}
""".strip())

for word_lenght in sorted(word_groups.keys()):
    print(
        f"{word_lenght:>3}|" 
        f"{word_groups[word_lenght]* "*":<14}|"
        f"{word_groups[word_lenght]:<3}"
        )

print("ahoj")

