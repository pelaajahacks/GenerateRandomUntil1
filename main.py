import random
import time

number_count = 0
funny_numbers = []

start = time.perf_counter()

print("The number is now loading...")

while True:
    number = random.randint(1, 999999)
    if number == 1:
        finish = time.perf_counter()
        secs = finish - start
        secs2 = round(secs)
        print("")
        print("THE NUMBER IS", number)
        print("")
        print("Some data:")
        print("VVVVVV")
        print("it took", str(number_count), "tries")
        sec = secs2 % (24 * 3600)
        hour = sec // 3600
        sec %= 3600
        minutes = sec // 60
        sec %= 60
        print(f"it took {hour} hours {minutes} minutes {secs:0.2f} seconds")
        print("1 digit numbers:", *funny_numbers)
        print("")
        print("How many 1 digit numbers:", len(funny_numbers))
        break
    elif len(str(number)) == 1:
        funny_numbers.append(number)
    number_count += 1
