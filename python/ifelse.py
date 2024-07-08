# Challenge 1
# -----------

# password = input("Type your new password: ")

# if len(password) < 8:
#     print(f"The password {password} is too short")
# else:
#     print(password)
    
    
# Challenge 2
# -----------

# num = int(input("Please enter the number: "))

# if (num % 3 == 0) or (num % 5 == 0):
#     print(f"The number {num} is divisible by 3 or 5")
# else:
#     print(f"The number {num} is not divisble by 3 or 5")
    
# Challenge 3
# -----------
# from random import randint

# num = randint(1,100)
# print(num)

# if (num % 3 == 0) and (num % 7 == 0):
#     print(f"FizzBuzz!")
# elif (num % 3 == 0):
#     print(f"fizz!")
# elif (num % 7 == 0):
#     print(f"Buzz")
# else:
#     print(num)

# Challenge 4
# -----------

# my_string = input("Type string to be checked here: ")

# if my_string[0] == my_string[-1]:
#     print("True")
# else:
#     print("False")
    
# Challenge 6
# -----------
# num1 = int(input("Number1: "))
# num2 = int(input("Number2: "))

# if ((num1+num2) % 2 == 0):
#     print("Success")
# else:
#     print("Failure")
    
# Challenge 7
# -----------

# num = input("Number to check: ")

# reverse_num = num[-1::-1]

# if num == reverse_num:
#     print(f"{num} is a palindrome")
# else:
#     print(f"{num} is not a palindrome")
    
# Challenge 8
# -----------

my_string = "jrfndklhgfndjkjlkgperfijfhdknsadcvjhiiohjfkledsopiuhgtyujwsdxcvhgfdjhiopiwquhejkdsoiufghedjwshigaffffh"

reverese_my_string = my_string[-1::-1]

a_pos = reverese_my_string.find("a")
e_pos = reverese_my_string.find("e")
i_pos = reverese_my_string.find("i")
o_pos = reverese_my_string.find("o")
u_pos = reverese_my_string.find("u")

first_pos = a_pos
if e_pos < first_pos:
    first_pos = e_pos
if i_pos < first_pos:
    first_pos = i_pos
if o_pos < first_pos:
    first_pos = o_pos
if u_pos < first_pos:
    first_pos = u_pos
    
print(first_pos)

string_length = len(my_string)
last_vowel_pos = string_length - first_pos -1

print(string_length)
print(last_vowel_pos)

print(last_vowel_pos, my_string[last_vowel_pos])    
    
