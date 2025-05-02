class Person :
     def __init__(self,name, age):  # Constructor to initialize the number
        self.name = name
        self.age = age

     def display_info(self):  # Display method corrected
         print("Name:", self.name)
         print("Age:", self.age)

    #create class object of the person class and call the display_info method
person1 = Person("John", 30)
person1.display_info()