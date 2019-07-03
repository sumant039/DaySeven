#!/usr/bin/python
class Test:
    pass


class MyClass:
  x = 5

#Create an object to access function and data of class
p1 = MyClass()
print(p1.x)


#Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p2 = Person("John", 36)

print(p2.name)
print(p2.age)



class Person_P:
  def __init__(self, pname, page):
    self.pname = pname
    self.page = page

  def myfunc(self):
    print("Hello my name is " + self.pname)

p3 = Person_P("John", 36)
p3.myfunc()


#It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

class Person_Pe:
    def __init__(mysillyobject, Pename, Peage):
        mysillyobject.Pename = Pename
        mysillyobject.Peage = Peage

    def myfunc(abc):
        print("Hello my name is " + abc.Pename)

p4 = Person_Pe("John", 36)
p4.myfunc()


#Any class can be a parent class, so the syntax is the same as creating any other class:

#student was a kid ,doesnt have its own function or data
class Student(Person_Pe):
  pass

x = Student("Mike", 32)
x.myfunc()



#Add Func and Properties

class StudentN(Person_Pe):
  def __init__(self, fname, lname, year):
    self.fname=fname
    self.lname=lname
    Person_Pe.__init__(self, fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.fname, self.lname, "to the class of", self.graduationyear)


x1=StudentN("Robert","Singh","2019")

x1.welcome()


#Func overloading 

class Human:

    def sayHello(self, name=None):

        if name is not None:
            print 'Hello ' + name
        else:
            print 'Hello '

# Create instance
obj = Human()

# Call the method
obj.sayHello()

# Call the method with a parameter
obj.sayHello('Guido')

#Design a class which defines two property name and age and define function to access them 
#Design a class country and state as its derived class using concept of inheritance and define function of states and country
#Create a class  to distinguihs between internal employee and external employee
#create a class to demonstarte concept of inheritance
#Create a class Automobile and inherit 2 classes Bus and car and define functions and access them
#Design a class Restaurant and use multiple inheritance ,also use function overloading to define serve() function 



