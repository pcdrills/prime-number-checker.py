print("\t PRIME NUMBER OR NOT? LET'S CHECK")
print('''--------------------------------------
******** * Welcome to prime number checker * ***********
----> written by pcdrills -> github.com/pcdrills
----> You Input a Number and the program checks if it's prime or not
--------------------------------------------------''')

#by default all values are prime until they are not. :D
#we only check half of the values because if it has a factor greater than it's half then it will also have less than it's half
#exempt 1 and 2 from the list of checks, since 1 isn't prime and 2 ist and it can be haneled by our for loop
def prime_checker(number):
    is_prime = True        #values are prime by default 
    if number is 1:         #exempt 1 and 2 from the checks
        is_prime = False
    elif number is 2:
        is_prime = True;
    else:
        for i in range(2, int(number/2)):     #check half of the values for in the range  
            if (number % i) == 0:
                is_prime = False
                break;                         #once proven not to be prime, just break the loop and no further checking

    if is_prime:
        print("It's a prime number")
    else:
        print("It's not a prime number")  

# options to implement iteration in execution
option = 'y'
quit = False

while not quit:
    if option == 'y':
        #Get user number
        n = int(input("Input your number: "))
        prime_checker(number=n)
    elif option == 'n':
        print("You opted to quit....")
        quit = True
        break;
    else:
        print("invalid option -> use: (y/n)")
    print("-=--check again? y->yes / n->no")
    option = input("==> ").lower()

print("See you later.......")