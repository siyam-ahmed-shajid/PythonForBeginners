#String Concatenation

first_name = "Jenny"
last_name = "Bakers"
message = "Hello " + first_name + " " + last_name + "!"
age = 34

print("Hello " + first_name + " " + last_name + "!")
print(message)
print("Your age is " + str(age))

#Working with String

message = "Hello World"
print(message [6])
print(message [-7])
print(len(message))
print(message.find("e"))

print(message.replace("ld", "if"))
print(message.lower())
print(message.upper())
print(message.capitalize())

#Working with Numbers
print(9+3)
print(9+3.3)
print(5-2.4)
print(5*2)
print(5/2)
print(5%3)
print(5+4*3/2)
print(round(5.55))
print(round(5.45))
print(round(4.5678, 3))
print(abs(-34))
print(pow(5, 3))

#Input Function

name = input("What is your name?")
age = input("What is your age?")
print("Hi " + name + "! " + "You are " + age + " years old")
print("My age is " + age)