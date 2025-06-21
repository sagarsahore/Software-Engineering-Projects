#Activity Week7-1: Singleton Design Pattern 
#Run and check there is one instance in the code  and why? see below:
 
 


 
class RentalManager:
    _instance = None
 
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(RentalManager, cls).__new__(cls)
            cls._instance.cars_available = ["Toyota", "Honda", "Ford"]
        return cls._instance
 
    def rent_car(self, car_name):
        if car_name in self.cars_available:
            self.cars_available.remove(car_name)
            print(f"{car_name} has been rented.")
            print(f"Available car: {car_name}: {id(car_name)}: car id: {id(car_name)}")
        else:
            print(f"{car_name} is not available.")
 
    def show_available_cars(self):
        print("Available cars:", self.cars_available)
 
 
manager1 = RentalManager()
manager2 = RentalManager()
 
car_name = input("Enter the name of the car you want to rent: ")
manager1.rent_car(car_name)
manager1.show_available_cars()  # Affects both because it's the same instance
manager2.show_available_cars()  # Affects both because it's the same instance
 
print("Are both managers the same object?", manager1 is manager2)
 
 #Is "car_name" variable is the same location in the memory? Debug the code to get the name of the car from end user? See below code: