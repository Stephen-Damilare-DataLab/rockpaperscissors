# name = input('Please enter your name:')
# print('Hello')
# print(name)

# working with concatenation of strings
# first_name = 'Soriyan'
# last_name= 'Olakunle'
# output= 'Dreams are bigger than imagination said by {1} {0}'.format(first_name ,  last_name)
# print(output)
# output2= f'Dreams are bigger than imagination said by {first_name} {last_name}'
# print(output2)

# days_in_feb = 28
# print(f'The number of days in febuary is {days_in_feb}')
days_in_feb = 28
# print(str( days_in_feb) +' days in febuary')

# storing numbers as strings
first_num ='5'
second_num = '6'
# print(first_num + second_num) # 56

# before math calculation, numbers must be converted to numeric values
# print(int(first_num) + int(second_num))
# print(float(first_num) + float(second_num))

from datetime import datetime,timedelta
# current_date = datetime.now()
# today = datetime.now()
# # print('Today date is: ',str(current_date))

#  working with timedelta
# timedelta helps to add  or remove day, month, weeks to the current date
# yesterday = today - timedelta(days=1)
# print('Yesterday was:' , str(yesterday))
# one_week = timedelta(weeks= 1)
# a_week_ago = today- one_week
# print('i was in church on:', a_week_ago)

# today= datetime.now()
# print('Day:'+ str(today.day))
# print('month:' + str(today.month))
# print('Hour:' + str(today.hour))

# handling conditions

# price =12.00
# if price >= 1.00:
#     tax =.07
#     print(tax)
# else:
#     tax = 0
#     print(tax)

# price = input('Enter the price of the item:')
# price = float(price)
# if price >= 1.00:
#     tax =.07
#     print(tax)
# else:
#     tax = 0
#     print(tax)



# price= input('Enter the price of the item:')
# price = float(price)
#  if price >= 1.00:
#      tax = .07
#      print('Tax rate is: ',str(tax))
# else:
#     tax = 0
#     print('Tax rate is: ',str(tax))

    
# country = input('Enter your country:')
# country = country.lower()
# country= str(country)
# if country== Nigeria:
#     tax =20  
# elif country == America:
#     tax = 15
# elif country == China:
#     tax = 10
# print('Tax rate is: ',str(tax))


# providence = input('What providence do you live in?:')
# tax = 0
# if providence == 'Alberta': 
#     tax=0.05
# if providence == 'Nunavut':
#     tax=0.07
# if providence == 'Quebec':
#     tax=0.13
# print(tax)


# providence = input('What providence do you live in?:')
# tax = 0
# if providence == 'Alberta': 
#     tax=0.05
# elif providence == 'Nunavut':
#     tax=0.07
# elif providence == 'Quebec':
#     tax=0.13
# print(tax) adding elif statement

# providence = input('What providence do you live in?:')
# tax = 0
# if providence == 'Alberta': 
#     tax=0.05
# elif providence == 'Nunavut':
#     tax=0.07
# elif providence == 'Quebec':
#     tax=0.13
# else:
#     tax = 0.15 adding else statement
# print(tax)


# providence = input('What providence do you live in?:')
# tax = 0
# if providence == 'Alberta' or providence == 'Nunavut':  adding or statement
#     tax=0.05
# elif providence == 'Quebec':
#     tax=0.13
# else:
#     tax = 0.15 
# print(tax)

country = input('Enter your country:')
country= country.lower()
if country == 'canada':
    providence = input('What providence do you live in?:')
    tax = 0
    if providence == 'Alberta' or providence == 'Nunavut':
        tax=0.05
    elif providence == 'Quebec':
        tax=0.13
    else:
        tax = 0.15
else:
    tax =0.00
print(tax)