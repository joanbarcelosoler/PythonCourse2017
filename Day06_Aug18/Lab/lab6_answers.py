#Exercise 1
#Write a function to calculate the greatest common divisor of two numbers

def max_divisors(num1, num2):
    div_num1 = []
    div_num2 = []
    if num1==0:
        div_num1.append("0")
    elif num2==0:
        div_num2.append("0")
    else:
        for x in range (1, num1+1):
            if num1 % x == 0:
                div_num1.append(x)
            else:
                pass
        for x in range (1, num2+1):
            if num2 % x == 0:
                div_num2.append(x)
            else:
                pass
    list_common = []
    for x in div_num1:
        if x in div_num2:
            list_common.append(x)
    print "Input list is {0}".format(div_num1)
    print "Input list is {0}".format(div_num2)
    print max(list_common)

max_divisors(15, 65)

#Exercise 2
#Write a function that returns prime numbers less than 121

def primes():
    for num in range(1,121):
        prime = True
        for i in range(2,num):
            if (num%i==0):
                prime = False
        if prime:
            print num


#Exercise 3
#Write a function that gives a solution to Tower of Hanoi game
#https://www.mathsisfun.com/games/towerofhanoi.html



 