import random

all_numbers = []

for item in range(0,10):

    # Generate a random number
    mystery_num = random.randint(a=1, b=200)
    all_numbers.append(mystery_num)

all_numbers.sort()
print(all_numbers)
