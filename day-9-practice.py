programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that can be reused",
}
#retrieving info
print(programming_dictionary["Bug"])

#adding new items
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

#create empty dictionary
empty_dictionary = {}

#wipe a existing dictionary
# programming_dictionary = {}

#looping through dictionary

###########################################
## nesting dictionaries within dictionaries
travel_log = {
    "Canada": {"cities_visited": ["Vancouver", "Toronto", "Vancouver Island"], "Total Visits": 10},
    "Australia": {"cities_visited": ["Sydney", "Melbourne", "Perth"], "Total Visits": 1}
}

# nesting dictionaries within list
travel_log = [
    {
        "country": "Canada", 
        "cities_visited": ["Vancouver", "Toronto", "Vancouver Island"], 
        "Total Visits": 10 
    },
    {
        "country": "Australia", 
        "cities_visited": ["Sydney", "Melbourne", "Perth"], 
        "Total Visits": 1
    },
]