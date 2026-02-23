 #excercise 1
numbers = [ ]
while True:
    user_input = input("Enter a number (or press Enter to quit): ")  
    if user_input == "":
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
numbers.sort(reverse=True)
top_five = numbers[:5]

print("The five greatest numbers are:")
for num in top_five:
    print(num)

  
  #excercise 2
number = int(input("Enter a number: "))
if number // number == 1 and number // 1 == number and number > 1:
    print(f"{number} is a prime number.")
else:    print(f"{number} is not a prime number.")

 
    
#excercise 3
cities = []
for i in range(5):
    city = input(f"Enter the name of city {i+1}: ")
    cities.append(city)
print("\nThe cities you entered are:")
for city in cities:
    print(city)


#excercise 4
def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
user_input = input("Enter a list of numbers separated by commas: ")
number_list = [float(num.strip()) for num in user_input.split(",")]
print(f"The sum of the numbers is: {sum_of_list(number_list)}")


#excercise 5
def remove_odd_numbers(numbers):
    new_list = []
    for num in numbers:
        if num % 2 == 0:
            new_list.append(num)
    return new_list
user_input = input("Enter a list of numbers separated by commas: ")
number_list = [int(num.strip()) for num in user_input.split(",")]
even_numbers = remove_odd_numbers(number_list)
print(f"The list with odd numbers removed is: {even_numbers}")


