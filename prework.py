#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.
def hello_name(user_name):
    print("hello_" + user_name+ "!")
user_name = input("What is your username? ")
hello_name(user_name)

#Question 2
##Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    for num in range(1,100):
        if num % 2 != 0:
            return None
first_odds()

#Question 2
#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
def max_num_in_list(a_list):
	maximum = max(a_list)
	print("Max number: ", maximum)

a_list = [0, 888, 77, 390, 182, 2, 70, 10]
print(max_num_in_list(a_list))

#Question 3
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
def is_leap_year(a_year):
	if a_year % 400 == 0:
		return True
	elif a_year % 100 == 0:
		return False
	elif a_year % 4 == 0:
		return True
	else:
		return False

a_year = input("Is it a leap year? Enter year: ")
a_year = int(a_year)
print(is_leap_year(a_year))

#Question 4
#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
def is_consecutive(a_list):
    a_list = [21, 22, 23, 24, 25, 26]
    sorted_list = sorted(a_list)

    range_list=list(range(min(a_list), max(a_list)+1))
    if sorted_list == range_list:
        print("True")
    else:
        print("False")


is_consecutive(a_list)
