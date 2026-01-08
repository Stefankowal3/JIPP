name = input("What is your name?: ")
age = input("What is your age?: ")
city = input("What is your city?: ")
interest = input("What is your interest?: ")

string = "Hi {}, you are {} years old. You live in {} and you love {}!"

output = string.format(name,age,city,interest)

print(output)

