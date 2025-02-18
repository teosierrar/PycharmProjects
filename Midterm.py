import http

a = 6

a = a - 2

print(a*2)

a = a * 2

print(a+1)

a = a // 3

print(a)

print(2+3*6/2)

import datetime

a = 3
b = 4
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "abc" * (c // 3)
print(d)

def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False


print(palindrome("2704702208931031198668911301398022074072"))
print(palindrome("7798338247658278460338648728567428338977"))
print(palindrome("0974101607733149676776769413377061014790"))
print(palindrome("4257304920394478392772938744930294037524"))


list1 = [1, 2, 3, 4, 5]
str1 = "abc"
print(list1[0])
print(str1[0])
list1.remove(3)
try:
    str1 [0] = "z"
except TypeError:
    print("Cannot change a string")
print(list1)
print(str1)


import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))
# continue here
for i in range(10):
    if random_numbers[i] > 80:
        random_numbers[i] = -random_numbers[i] #we get the negative of value of the ith number
    elif random_numbers[i] < 40:
        random_numbers[i] = sum(int(digit) for digit in str(random_numbers[i])) #we add the digits of the number

print(random_numbers) #we print the list

def valid_url(url):
    if "http" in url and "." in url and "://" in url:
        return True
    else:
        return False
        print(f"invalid url")

print(valid_url("https://www.google.com/search?q=http+vs+https&sca_esv=e5ef21b71770b976&rlz=1C5CHFA_enES1073ES1074&ei=Zaq0Z5qVLKeskdUP-IKFyQc&oq=http&gs_lp=Egxnd3Mtd2l6LXNlcnAiBGh0dHAqAggAMgsQABiABBiRAhiKBTILEAAYgAQYkQIYigUyChAAGIAEGEMYigUyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAESIoTUIoDWO4IcAF4AZABAJgBwAGgAYIFqgEDMC40uAEByAEA-AEBmAIFoAKaBagCA8ICExAAGIAEGEMYtAIYigUY6gLYAQHCAgsQLhiABBjRAxjHAcICCBAuGIAEGNQCwgIFEC4YgASYAwnxBSqEIDu0TaYougYECAEYB5IHAzEuNKAHpx4&sclient=gws-wiz-serp"))

#question 9
year_born= (input("Enter your date of birth: (DD/MM/YYYY)"))
year_born = year_born[6:]
difference = [18-year_born[0:1], 13-year_born[2:3], 2025-year_born[4:5]]
print(difference)
