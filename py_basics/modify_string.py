a = "Hello World"
# captial case
print(a.upper())

# small case
print(a.lower())

# remove whitespace
print(a.strip())

# replace string
print(a.replace("H", "J"))

# split string
print(a.split(","))

# string concatenation
a = "hello"
b = "world"
c = a+b
print(c)

c = a + " " + b
print(c)

# string format
age = 36
txt = "My name is John, and I am {}"  
print(txt.format(age))

quantity = 3
item_no = 339
price = 49.95

myOrder = "I want {} pieces of item {} for {} dollars."
print(myOrder.format(quantity, item_no, price))

# using index numbers to be sure the arguments are places in the correct placeholders
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, item_no, price))