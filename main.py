import random
import time

number_count = 0
funny_numbers = []

start = time.perf_counter()

print("The number is now loading...")

while True:
    number = random.randint(1, 9999999)
    list1.append(number)
    if number == 1:
        finish = time.perf_counter()
        print("")
        print("THE NUMBER IS", number)
        print("")
        print("it took", str(number_count), "tries")
        print("")
        print(f"it took {finish - start:0.4f} seconds")
        print("")
        print("1 digit numbers:", *funny_numbers)
        break
    elif len(str(number)) == 1:
        funny_numbers.append(number)
    number_count += 1
