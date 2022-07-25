#this line uses double quotation mark because it has a single inside. Strings can be referenced indistinctl using double or single
from logging import StringTemplateStyle

name=input("What's your name \n")
print ('hello ' +name) #strings concatenate with +

# Strings

sentence='The dog is named Sammy'
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())

#custom formatting strings
    
first_name=name
last_name='Sanchez'
output='Hello, {} {} '.format(first_name,last_name)
print(output)
output='Hello, {0} {1} '.format(first_name,last_name)
print(output)
output=f'Hello, {first_name} {last_name}' 
print(output)

#numbers
first_number= 6
second_number= 2
print (first_number+second_number-first_number)
print (first_number**second_number) #exponent
print (first_number/second_number*first_number)

print (str(first_number) + ' is the first number') #to print convert 

first_num=input('Enter the first number')
second_num=input ('Enter the second number')
print (int(first_num)+int(second_num)) #in this case had to convert to int the input as was a string