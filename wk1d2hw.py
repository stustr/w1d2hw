stops = ["Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket"]

# 1. Add "Edinburgh Waverley" to the end of the list
stops.append("Edinburgh Waverley")
# 2. Add "Glasgow Queen St" to the start of the list
stops.insert(0, "Glasgow Queen St")
# 3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
stops.insert(4, "Polmont")
# 4. Print out the index position of "Linlithgow"
print(stops.index("Linlithgow"))
# 5. Remove "Livingston" from the list using its name
stops.remove("Livingston")
# 6. Delete "Cumbernauld" from the list by index
del stops[2]
# 7. Print the number of stops there are in the list
print(len(stops))
# 8. Sort the list alphabetically
stops.sort()
# 9. Reverse the positions of the stops in the list
stops.sort(reverse=True)
# 10 Print out all the stops using a for loop
for i in stops:
    print(i)


users = {
    "Jonathan": {
        "twitter": "jonnyt",
        "lottery_numbers": [6, 12, 49, 33, 45, 20],
        "home_town": "Stirling",
        "pets": [
            {"name": "fluffy", "species": "cat"},
            {"name": "fido", "species": "dog"},
            {"name": "spike", "species": "dog"},
        ],
    },
    "Erik": {
        "twitter": "eriksf",
        "lottery_numbers": [18, 34, 8, 11, 24],
        "home_town": "Linlithgow",
        "pets": [
            {"name": "nemo", "species": "fish"},
            {"name": "kevin", "species": "fish"},
            {"name": "spike", "species": "dog"},
            {"name": "rupert", "species": "parrot"},
        ],
    },
    "Avril": {
        "twitter": "bridgpally",
        "lottery_numbers": [12, 14, 33, 38, 9, 25],
        "home_town": "Dunbar",
        "pets": [{"name": "monty", "species": "snake"}],
    },
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
jonathan_twitter = users["Jonathan"]["twitter"]
# 2. Get Erik's hometown
erik_hometown = users["Erik"]["home_town"]

# 3. Get the list of Erik's lottery numbers
erik_lotto = users["Erik"]["lottery_numbers"]

# 4. Get the species of Avril's pet Monty
monty_species = users["Avril"]["pets"][0]["name"]

# 5. Get the smallest of Erik's lottery numbers
erik_lotto.sort()
smallest_erik_lotto = erik_lotto[0]

# 6. Return an list of Avril's lottery numbers that are even
av_lot_list = users["Avril"]["lottery_numbers"]
av_even_lot = []
for i in av_lot_list:
    if i % 2 == 0:
        av_even_lot.append(i)
print(av_even_lot)

# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
erik_lotto.append(7)

# 8. Change Erik's hometown to Edinburgh
users["Erik"]["home_town"] = "Edinburgh"

# 9. Add a pet dog to Erik called "fluffy"
users["Erik"]["pets"].append({"name": "fluffy", "species": "dog"})

# 10. Add another person to the users dictionary
users["Steve"] = {}


united_kingdom = [
    {"name": "Scotland", "population": 5295000, "capital": "Edinburgh"},
    {"name": "Wales", "population": 3063000, "capital": "Swansea"},
    {"name": "England", "population": 53010000, "capital": "London"},
]

# 1. Change the capital of Wales from `"Swansea"` to `"Cardiff"`.
united_kingdom[1]["capital"] = "Cardiff"

# 2. Create a dictionary for Northern Ireland and add it to the `united_kingdom` list (The capital is Belfast, and the population is 1,811,000).
united_kingdom.append(
    {"name": "Northern Ireland", "population": 5295000, "capital": "Belfast"}
)

# 3. Use a loop to print the names of all the countries in the UK.
for i in range(len(united_kingdom)):
    print(united_kingdom[i]["name"])

# 4. Use a loop to find the total population of the UK.
total_pop_uk = 0
for i in range(len(united_kingdom)):
    total_pop_uk += united_kingdom[i]["population"]

print(total_pop_uk)


# For the following list of numbers:

from operator import le
from re import L
from tkinter import N


numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
evens = []
for i in numbers:
    if i % 2 == 0:
        evens.append(i)
print(evens)


# 2. Print the difference between the largest and smallest value:
sorted = sorted(numbers)
print(sorted[-1] - sorted[0])


# 3. Print True if the list contains a 2 next to a 2 somewhere.
for i in range(len(numbers) - 1):
    if numbers[i] == numbers[i + 1]:
        print(True)


# 4. Print the sum of the numbers,
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#
#    So [11, 6, 4, 99, 7, 11] would have sum of 22
sum_list = []
on = True
for i in numbers:
    if i == 6:
        on = False
    if on:
        sum_list.append(i)
    if i == 7 and on == False:
        on = True

print(sum(sum_list))

# 5. HARD! Print the sum of the numbers.
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5.

length = len(numbers)
total = 0
i = 0
while i < length:
    if numbers[i] == 13:
        i += 2
    else:
        total += numbers[i]
        i += 1

print(total)
