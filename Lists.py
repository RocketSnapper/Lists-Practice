def first_value(cars):
    print(cars[0])
    return cars[0]

one_car = first_value(['Mustang', 'Viper', 'Camaro'])

def color_check(colors):
    user_color = input('Pick a color')
    for color in colors:
        if user_color == color:
            print('You found my chosen color!')
        
color_check(['Red', 'White', 'Blue', 'Purple'])

def combine_numbers(numbers):
    number_sum = 0
    for number in numbers:
        number_sum = number_sum + number
    if number_sum % 2 == 0:
        return(f'{number_sum} is even')
    else:
        return(f'{number_sum} is odd')
    
even_or_odd = combine_numbers([6, 8, 3, 8])
print(even_or_odd)

def find_greater_values(numbers, the_number):
    for number in numbers:
        if number > the_number:
            print(number) 

find_greater_values([5, 8, 13, 27], 4)