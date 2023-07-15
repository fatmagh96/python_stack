# 1. Countdown

def countdown(num):
    l = []
    for i in range(num,-1,-1):
        l.append(i)
    return l
print(countdown(5))

# 2. Print and Return

def print_and_return(list):
    print(list[0])
    return list[1]

print(print_and_return([1,2]))

# 3. First Plus Length

def first_plus_length(list):
    return list[0] + len(list)

print(first_plus_length([1,2,3,4,5]))

# 4. Values Greater than Second

def values_greater_than_second(list):
    new_list = []
    if len(list)<2 :
        return False
    else:
        for i in list:
            if i > list[1]:
                new_list.append(i)
        print("Number of Values Greater than Second: ", len(new_list))
        return new_list
    
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

# 5. This Length, That Value 

def length_and_value(size,val):
    list = []
    for i in range(size):
        list.append(val)
    return list

print(length_and_value(4,7))
print(length_and_value(6,2))