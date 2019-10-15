# take an input and assign it to a variable called numberone
numberone = input("First number ") 
# take an input and assign it to a variable called numbertwo
numbertwo = input("Second number ")

#inputs are ALWAYS strings. Before using them as numbers, they have to be converted to Integers, 
#you do this by "typecasting", as this, where "numberone" is converted to the int-variable "n_one" and
#"numbertwo" is converted to the int-variable "n_two":
n_one=int(numberone)
n_two=int(numbertwo)

#after the conversion, we can use these inputs in matemathical expressions
number = n_one+n_two


print (number)

#prints the result of numberone + numbertwo

