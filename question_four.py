#N0.4(i) a)
# Object Oriented Programming is a program that uses methods to perform operations on given data.

#Significances
#It is used for modelling an object or data.
#OOP brings the object and its behaviour together through the call of the method.

#N0.4(i) b)
# A class is a blue print for an object, whereas
# An object is the one that contains attributes and methods.


#N0.4(ii)
sentence = "python exam"
words = sentence.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)


#N0.4(iii)
def sum():
    a = int(input("Enter the first_number: "))
    b = int(input('Enter the second_number: '))
    sum = a+b
    print(f"Their sum is {sum}")
sum()


#N0.4(iv)

class Car:
    def __init__(self, brand, name, color):
        self.brand = brand
        self.name =name
        self.color = color

p1 = Car("Toyota", "RAV4", "Blue")
print(p1.brand)
print(p1.name)
print(p1.color)


#N0.4(v)

class Car:
    def __init__(self, start_engine):
        self.start_engine = start_engine
data = Car("The engine of the car has started.")
print(data.start_engine)        
        