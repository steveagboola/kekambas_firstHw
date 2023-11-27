# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below. def hello_name(user_name):
# ..... 

def hello_name(user_name):
    print ("Hello " + user_name)
hello_name("steve")

#or

def hello_name(user_name):
    print(f"Hello_{user_name.upper()}!")


# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing def first_odds():
# ..... 

def first_odds():
    for number in range(1, 101, 1):  # I guess i can technically stop at 100?
        if number % 2 != 0:
            print(number)


# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below. def max_num_in_list(a_list):
# ..... 

def max_num_in_list(a_list):
    maximum = a_list[0]
    for num in a_list:
        if num > maximum:
            maximum = num
    return maximum

# print(max_num_in_list([1,2,34,24,424,435,4,3]))


# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400. The return should be boolean Type (true/false). def is_leap_year(a_year):
# ..... 

#(divisible by 4 AND not divisible by 100 has to be true)
def is_leap_year(a_year):
    if (a_year % 4 == 0 and a_year % 100 != 0) or (a_year % 400 == 0):
        return True
    return False


# Question 5

# Write a function to check to see if all numbers in the list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type. def is_consecutive(a_list):

def is_consecutive(a_list):
    num = 0
    if num >= (len(a_list) -1):
        return True
    if num <= (len(a_list) +1):
        return True
    else:
        return False
    
    #Cant figure this one out.