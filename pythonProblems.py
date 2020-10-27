# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# house_price = 1000000
# credit_good = True
# credit_bad = False
#
# if credit_good:
#     down_payment = house_price / 10
# elif credit_bad:
#     down_payment = house_price / 20
# else:
#     down_payment = house_price / 15
#
# print(f'Down payment:', {down_payment})
#
# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count = guess_count + 1
#     if guess == secret_number:
#         print('You Won')
#         break
#     else:
#         print('You are out of guesses')
#
# command = ""
# started = False
# while True:
#     command = input('> ').lower()
#     if command == "start":
#         if started:
#             print("Car already started")
#         else:
#             started = True
#             print('Car Started')
#     elif command == "stop":
#         if not started:
#             print('Car is already stopped')
#         else:
#             started = False
#             print("Car Stopped")
#     elif command == "help":
#         print("""
#         start - to start the car
#         stop - to stop the car
#         quit - to quit
#         """)
#     elif command == "quit":
#         break
#     else:
#         print('sorry I dont understand that')

# prices = [10, 20, 30]
# total = 0
# for item in prices:
#     total += item
#     print(f'total: {total}')

# numbers = [1, 2, 3, 4, 5]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)

# numbers = [1, 7, 2, 2, 3, 6, 4, 4, 5, 5]
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)

coordinates = (1, 2, 3)
x, y, z = coordinates
print(y)

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
print(customer["name"])

phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
    print(output)
