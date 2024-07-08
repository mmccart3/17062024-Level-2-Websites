# from random import randint

# music = "90s"

# if music == "Classical":
#     print("Please no classical music!")
#     print("It is too boring")
# elif music == "Country":
#     print("Please never Country")
#     print("switch it off!")
# elif music == "80s":
#     print("YES!")
#     print("Turn it up")
# elif music == "90s":
#     print("Lets Rave!")
# elif music == "00s":
#     print("Cool")
# else:
#     print("I do not recognise that music!")

# my_number = randint(1,20)
# print(my_number)

# if my_number >= 15:
#     print("Great Score you win")
# elif my_number < 15:
#     print("You lost")
from colorama import Fore, Back

# age = int(input("What is your age: "))
# print(age)
# country = input("Are you in the UK or US? ".lower())
# print(country)
# country = country.strip(" ")
# print(country)

# if (age >=18 and country == "uk") or (age >= 21 and country == "us"):
#     print(f"{Fore.GREEN} {Back.BLUE} Yes sir I can serve you!")
# else:
#     print(f"{Fore.RED}You are too young go away!")
    
# place = input("Where are you? ")
# weather = input("What is the weather like now? ")

# if place == "Manchester" and weather != "raining":
#     print("It always rains in Manchester check again")
# elif place == "Ibiza" and weather == "Sunny":
#     print("As always the weather in Ibiza is fantastic")
# elif place == "Manchester" and weather == "raining":
#     print("What do you expect it is always raining in Manchester")
# elif place == "Ibiza" and weather != "Sunny":
#     print("that's unlucky!")

my_string = "The quick brown fox"
print(my_string[0])
print(my_string[-1])

print(my_string[-1::-1])