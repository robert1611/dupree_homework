#exercise 1
#iterate through 1000, cubing each number
#iterate through all the numbers.  when you hear iterate, think for loop
#cube each number

for i in range(1001):
    print (i * i * i)

#exercise 2
#prime numbers up to 100
#set range at 1 more than desire ceiling
#nest for loop within if statement so 1 is ignored
#see Codewars question on prime numbers for a more challenging exampe

for num in range(101):
    if num >1:
        for i in range (2, num):
            if (num% i) == 0:
                break
        else:
            print(num)

#exercise 3
#simple if, elif, else question
#go in ascending order to you can do a simple lesser than

age = int(input("How old are you?: "))
if age < 18:
    print("kids")
elif age < 66:
    print("adults")
else:
    print("seniors")


            