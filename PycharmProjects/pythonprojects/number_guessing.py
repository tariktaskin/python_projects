import random

random_number=random.randint(1,100)
divisor_list= [a for a in range(1,20) if random_number%a==0]

while True:
    print("some of the divisor of the number are {}".format(random.sample(divisor_list,2)))
    enter_number=int(input("guess the number"))
    if enter_number== random_number:
        print("you have find the number. congratulations")
        break
    else:
        print("try again")