#exercise 1
#iterate through 1000, cubing each number
#iterate through all the numbers.  when you hear iterate, think for loop
#cube each number

#for i in range(1001):
#    print (i * i * i)

#exercise 2
#prime numbers up to 100
#set range at 1 more than desire ceiling
#nest for loop within if statement so 1 is ignored
#see Codewars question on prime numbers for a more challenging exampe

#for num in range(101):
#    if num >1:
#        for i in range (2, num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)

#exercise 3
#simple if, elif, else question
#go in ascending order to you can do a simple lesser than

#age = int(input("How old are you?: "))
#if age < 18:
#   print("kids")
#elif age < 66:
#    print("adults")
#else:
#    print("seniors")


#extra exercise 1
# Create a while loop that displays the names of 
# the 30th to the 44th President - Hint create a list first


president_list = ["Calvin Coolidge", "Herbert Hoover", "Franklin Roosevelt",
        "Harry Truman", "Dwight Eisenhower", "John Kennedy", 
        "Lyndon Johnson", "Richard Nixon", "Gerald Ford", "Jimmy Carter"
        "Ronald Reagan", "George HW Bush", "Bill Clinton", "George W Bush", 
        "Barack Obama"]

for president in president_list:
    print(president)

#extra exercise 2
# multiply all the numbers in a list
#example [1, 2, 3, -4]

def multiply_num_list(num_list):
    result = 1
    for num in num_list:
        result = result * num
    return result

lista = [1,2,3,-4]
listb = [10, 14,-15,-3, 29, 8]
listc = [22, 43, 64, 45, 23]
listd = [12,66, 75, 90]

print(multiply_num_list(lista))
print(multiply_num_list(listb))
print(multiply_num_list(listc))
print(multiply_num_list(listd))

#extra exercise #3





#extra exercise #4
 
def add_it_up(n):
    if isinstance (n, float):
        return
    elif isinstance (n, str):
        return 0
    elif isinstance (n, bool):
        return 0
        return 0
    else:
        sum = 0 
        for i in range(n): 
	        sum = sum + i
        return sum

print(add_it_up(20))









            