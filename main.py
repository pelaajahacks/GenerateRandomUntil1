import random
import time

number_count = 0
funny_numbers = []


def print_time():
    sec = secs2 % (24 * 3600)
    hour = sec // 3600
    sec %= 3600
    minutes = sec // 60
    sec %= 60
    print(f"It took {hour} hours {minutes} minutes {secs:0.3f} seconds")


start = time.perf_counter()

print("The number is now loading...")

while True:
    number = random.randint(1, 9999999)
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
        print_time()
        print("1 digit numbers:", *funny_numbers)
        print("")
        print("How many 1 digit numbers:", len(funny_numbers))
        print("Sleeping...")
        time.sleep(60)
        break
    elif len(str(number)) == 1:
        funny_numbers.append(number)
    number_count += 1
