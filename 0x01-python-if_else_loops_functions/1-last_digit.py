#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdig = abs(number) % 10
if lastdig > 5 and number > 0:
    print("Last digit of", number, "is", lastdig, "and is greater than 5")
elif lastdig < 6 and lastdig != 0 and number > 0:
    print("Last digit of", number, "is", lastdig, "and is less than 6 and not 0")
elif lastdig == 0 and number > 0:
    print("Last digit of", number, "is", lastdig, "and is 0")
elif lastdig > 5 and number < 0:
    print("Last digit of", number, "is", -lastdig, "and is greater than 5")
elif lastdig < 6 and lastdig != 0 and number < 0:
    print("Last digit of", number, "is", -lastdig, "and is less than 6 and not 0")
else:
    print("Last digit of", number, "is", lastdig, "and is 0")
