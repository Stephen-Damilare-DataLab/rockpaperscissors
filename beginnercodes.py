# concatenation
first_name = 'Stephen'
last_name = 'Adepoju'
Name = first_name +" "+ last_name
# Greeting = 'Hello' + " " + Name
#print(Greeting)
#print(Greeting.upper())
#print(Greeting.lower()) 
#print(Greeting.title())
#print(Greeting.capitalize())
#print(Greeting.count('s'))
#python is case sensitive

first_name=input('What is your first name? ')
last_name=input('What is your last name? ')
# print('Hello' + " " + first_name.capitalize() + " "\
    #   + last_name.capitalize())

name = input('Please enter your name:')
print('Hello')
print(name)


# CODE FOR READABILITY
# print('Hello world \ni am at the center of Nigeria')

# # debugging your code
# # print('Adding numbers')
# x =10 +15
# print('performing division')
# y =  x/0
# # print('math complete')










# spliting a string
language ='Python programming'
#print(language[0:6])
#print(language[-11:])

#formatting string
# name = 'Stephen'
# age = 22
#print(f'My name is {name} and i am {age} years old')

city = 'London'
age = 23
#print(f'i will travel to {city} when i reach the age of {age} years')


disease = 'Covid-19'
treatment= 'Vaccine'
#print(f'The cure for {disease} is {treatment}')

#splitting a string
# name = 'Stephen Adepoju'

#print(name.split('|'))
sentence = 'I ,am ,a ,data analyst'
words= sentence.split(",")
#print(words)

text =' i love C++ programming language'
updated_text = text.replace('C++','Python')
#print(updated_text)

course = ' I study biochemistry in the university'
updated_course= course.replace('biochemistry','bioinfomatics')   
#print(updated_course)

city_status= 'Ogbomosho is a city in oyo state blessed with Cassava'
updated_city_status= city_status.replace('Cassava','Mango and Cashew')
#print(updated_city_status)

# WORKING WITH REGULAR EXPRESSION

import re
text = 'Contact me on 091-234-5678'
phone = re.findall(r"\d+",text)
#print(phone)

updated_text= re.sub(r"\d","X", text)
#print(updated_text)

hobby = ' i love reading books and playing COD 2025'
year = re.findall(r"\D+",hobby) 
#print(year)

updated_hobby = re.sub(r"\d","2026",hobby)
#print(updated_hobby)


import re 
def clean_text(text):
    text = re.sub(r"[^\w\s]", "", text)
    text = " ".join(text.split())
    return text.lower()
input_text = "   Hello World...^|, i am learning Python Programming Language....    "
cleaned_text= clean_text(input_text)
#print("cleaned text", cleaned_text)


