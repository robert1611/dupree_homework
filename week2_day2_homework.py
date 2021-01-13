#Question 1

l_1 = [1,11,14,5,8,9]

def under_10(l_1):
    l_1.sort()
    l_1.pop()
    l_1.pop()
    return(l_1)
    
print(under_10(l_1))

#Question 2

#solved concatenate

l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

def merge_lists(l_1,l_2):
    return sorted(l_1 + l_2)
       
print(merge_lists(l_1,l_2))



