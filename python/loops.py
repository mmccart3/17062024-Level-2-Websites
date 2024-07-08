# from time import sleep
# from playsound import playsound

# def film_check(film):
#     if film.lower() == "ghostbusters":
#         return " ... yay it's Ghostbusters"
#     else:
#         return " ... boo, we want Ghostbusters"
    
# my_fave_films = [
#     "Shawshank Redemption",
#     "Casablanca",
#     "The Longest Day",
#     "It's a wonderful life",
#     "Ghostbusters"
# ]

# for each_film in my_fave_films:
#     print(each_film, film_check(each_film))
    
# for i in range(1,11):
#     print(i)

# for i in range(10,-1,-1):
#     sleep(1)
#     print(i)
# print("Boom")
# playsound("rocket-take-off-sound-90267.mp3")

from random import randint

random_number = randint(1, 100)
print(random_number)

target_number = 67
counter = 1

while random_number != target_number:
    random_number = randint(1, 100)
    print(random_number)
    counter += 1

print(counter)