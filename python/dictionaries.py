from random import randint

animal_young = {
    "lion" : "cub",
    "dog" : "puppy",
    "human" : "baby",
    "goat" : "kid"
}

print(animal_young["goat"])      # BAD PRACTICE
print(animal_young.get("goat"))  # GOOD PRACTICE

animal_young["lion"] = "lion cub"
print (animal_young.keys())
print (animal_young.values())
print (animal_young.items())

print(animal_young.setdefault("cat", "kitten")) # adds a new key:value pair

animal_young.update({"hedghog":"hoglet", "owl": "owlet"}) # merges two dictionaries
animal_young.pop("cat") # deletes a key:value pair

print(animal_young)

challenger1 = {
    "strength" : 75,
    "speed" : 50,
    "health" : 80
}


challenger2 = {
    "strength" : 80,
    "speed" : 60,
    "health" : 65
}


challenger3 = {
    "strength" : 89,
    "speed" : 43,
    "health" : 87
}

challengers = [challenger1, challenger2, challenger3]

your_challenger = challengers[randint(0,2)]

print(your_challenger)