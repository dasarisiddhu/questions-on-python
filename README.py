"""EVERY QUESTION HERE IS A STRING AND ANSWER FOLLOWS"""

""" (1a) Reverse a string in Python using slicing."""
s = "rajesh"
o = ''.join(reversed(s))
print(o)

"""(1b)Reverse a string in Python using slicing."""
s = "rajesh"
o = s[:: -1]
print(o)


""" (2) Count the number of vowels and consonants in a given string."""

s = "understanding"
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for char in s:
    if char.isalpha():
        if char in vowels:
            vowel_count +=1
        else:
            consonant_count +=1

print("vowels",vowel_count)
print("consonants",consonant_count)


""" (3) check if it is an armstrong number"""

num = int(input("enter a number: "))  # You can change this to any number
n = len(str(num))
sum_of_powers = sum(int(digit)**n for digit in str(num))

if sum_of_powers == num:
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")

""" (4) Find the second largest element in a list without max()"""
 
l1 = [10,24,56,98,555,87,248,45,78]
l1.sort()
print("the second largest nuumber in the list is: ",l1[len(l1)-2])

""" (5) Remove duplicates from a list without using set()"""
l1 = input("Enter the elements of list separated by space: ").split()

def remove_duplicates(lst):
    l2 = []
    for i in lst:
        if i not in l2:
            l2.append(i)
    return l2

print(remove_duplicates(l1))          


""" (6) Sort a dictionary by values"""
fruits = {
    "apple": 2,
    "brinjal": 5,
    "banana": 1,
}

sorted_dict = dict(sorted(fruits.items(), key=lambda x: x[1]))

print(sorted_dict)

'''(7)check if two strings are anagrams'''

anagrams = {
    "listen" : "silent",
    "evil" : "villa",
    }

def are_anagrams(str1,str2):
    return sorted(str1) == sorted(str2)

for str1,str2 in anagrams.items():
    if are_anagrams(str1,str2):
        print(f"{str1} and {str2} are anagrams")
    else:
        print(f"{str1} and {str2} are not anagrams")


'''(8)find fatorial of a number using recursion'''

def Factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*Factorial(n-1)

n = int(input("enter a number: "))

fact = Factorial(n)

print(fact)

'''(9)Implement binary search on a sorted list.'''
def binary_search(arr,target):
    low = 0
    high = len(arr)-1
    while low <= high :
        mid = (low +high)//2
        geuss = arr[mid]
        if geuss == target:
            print("found at index: ", mid)
            return mid
        if geuss > target:
            high = mid-1
        else:
            low = mid+1
    return None
   
   
numbers = list(map(int, input("enter the list of numbers with spaces: ").split()))
l = sorted(numbers)
t = int(input("enter the number for search: "))
result = binary_search(l,t)
print(result)
print(l)


'''(10)Print a pyramid/star pattern of user choice'''
p = "*"
n = int(input("Enter the number of rows: "))
for i in range(n):
    print(" "*(n-i-1) + p*(2*i+1))

#reverse pyramid
for i in range(n-1,-1,-1):
    print(" "*(n-i-1) + p*(2*i+1))
 















