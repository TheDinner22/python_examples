# sort a list of strings (a-z) ignore ties (aab == aac even though thats wrong)
# crash if the string contains 1234567890!@#$%^&*()_-+=[]{}:;'"?/<>,.~`\|

# handling ties requires extra looping and logic so I did not implement it

char_to_int = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
}

# some names to sort
example_names = [
    "joseph",
    "joe",
    "evan",
    "goodman",
    "nate",
    "nathan",
    "aiden",
    "deez",
    "aabbccddz",
    "aabbccdde",
]

# list that has all of the sorted names
sorted_list = []

# going to loop over each name and compare it to every other name 
# insert the "smallest" into the new, sorted list
sorted = False
while not sorted:
    smallest_names_number = 99999 # place holder
    smallest_name = "place holder"
    for name in example_names:
        # number from the first character in the name
        names_number = char_to_int[name[0]]

        if names_number < smallest_names_number:
            smallest_names_number = names_number
            smallest_name = name

    # add the smallest name to the sorted list and remove it from the unsorted list
    sorted_list.append(smallest_name)
    example_names.remove(smallest_name)

    # if the example_names list is empty, stop looping
    if len(example_names) == 0:
        sorted = True

print(sorted_list)

