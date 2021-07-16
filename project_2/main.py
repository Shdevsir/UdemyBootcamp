import json
from difflib import get_close_matches
data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("Did you mean %s? " % get_close_matches(word, data.keys())[0])
        answer = input("press yes or no")
        if answer == "yes":
            return data[get_close_matches(word, data.keys())[0]]
        elif answer == "no":
            print("Okey")
        else:
            print("Please, correct input(yes or no)")
    else:
        print("No search word in dictionary")


word = input("Write the word, whay you want to search: ")
output = translate(word)
for item in output:
    print(item)
