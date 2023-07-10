# ***** BASIC *****

for i in range(0,151):
    print(i)

# **********************
print("*********\nNEXT ASSIGNMENT\n***********")
# ***** MULTIPLES OF FIVE *****

for i in range(5,1001):
    if i%5 == 0:
        print(i)

# **********************
print("*********\nNEXT ASSIGNMENT\n***********")
# ***** COUNTING, THE DOJO WAY *****

for i in range(1,101):
    if i%10 == 0:
        print("Coding Dojo")
    elif i%5 == 0:
        print("Coding")
    else: print(i)

# **********************
print("*********\nNEXT ASSIGNMENT\n***********")
# ***** WHOA. THAT SUCKER'S HUGE *****

sum = 0
for i in range(0,500001):
    if not i%2 == 0:
        sum += i
        # print(i)
print(sum)    

# **********************
print("*********\nNEXT ASSIGNMENT\n***********")
# ***** COUNTDOWN BY FOURS *****

for i in range(2018,0,-4):
    print(i)

# **********************
print("*********\nNEXT ASSIGNMENT\n***********")
# ***** FLEXIBLE COUNTER *****

def flexible_counter(lowNum,highNum,mult):
    for i in range(lowNum,highNum+1):
        if i%mult == 0:
            print(i)
    return None

flexible_counter(2,9,3)