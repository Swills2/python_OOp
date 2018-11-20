class Bike:
    def __init__(self, price, max_speed, miles = 0):
        self.price = price
        self.max_speed = []
        self.miles = miles

def displayInfo(self, price, max_speed, miles):
    print(price, max_speed, miles)
    return self

def ride(self, miles):
    print("Riding")
    miles += 10
    return self

def reverse(self, miles):
    print("Reversing")
    miles -= 5
    if miles < 0:
        miles = 0
    return self
